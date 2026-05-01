#!/usr/bin/env python3
"""
Mail-merge personnalisé pour contacter les agences immobilières de Barcelone.

Usage :
    python mail_merge.py --dry-run    # prévisualise sans envoyer
    python mail_merge.py               # envoie pour de vrai

Configuration :
    - Renseigner les variables SMTP_USER et SMTP_PASS (App Password Gmail)
      via variables d'environnement OU directement plus bas.
    - Vérifier `agences.csv` à côté de ce fichier.
"""

import argparse
import csv
import getpass
import os
import smtplib
import ssl
import sys
import time
from datetime import date
from email.message import EmailMessage
from pathlib import Path

# ---------- À PERSONNALISER ----------

USER = {
    "prenom": "Florent",
    "nom": "Lin",
    "email": "1florentlin@gmail.com",
    "tel": "+33 7 81 63 66 63",
    "age": 24,
    "nationalite": "française",
    "employeur": "Hello Pomelo",
    "adresse_bureau": "Carrer de Mallorca, 100, 08013 Barcelona",
    "vie_min": 2500,
    "vie_max": 3000,
    "garante_revenu": 5000,
    "loyer_min": 1000,
    "loyer_max": 1300,
    "move_in": "20 au 31 mai",
    "voyage": "17 au 20 mai",
    "duree_vie_mois": 12,
}

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465
SMTP_USER = os.environ.get("GMAIL_USER", USER["email"])
SMTP_PASS = os.environ.get("GMAIL_APP_PASSWORD")  # remplir si pas en env var

DELAY_BETWEEN_EMAILS_SEC = 5  # anti rate-limit Gmail

# ---------- TEMPLATES ----------

SUBJECT_FR = "Recherche studio meublé Eixample/Gràcia – VIE Hello Pomelo, dossier solide"
SUBJECT_EN = "Furnished studio search Eixample/Gràcia – VIE at Hello Pomelo, strong file"
SUBJECT_ES = "Búsqueda estudio amueblado Eixample/Gràcia – VIE en Hello Pomelo, dossier sólido"


def body_fr(agent_name: str, agence: str) -> str:
    salut = f"Bonjour {agent_name}," if agent_name else f"Bonjour l'équipe de {agence},"
    return f"""{salut}

Je m'appelle {USER['prenom']} {USER['nom']}, j'ai {USER['age']} ans, et je rejoins
l'entreprise {USER['employeur']} ({USER['adresse_bureau']}) le 1er juin dans le
cadre d'un VIE de {USER['duree_vie_mois']} mois (Volontariat International en
Entreprise, contrat sponsorisé par l'État français).

Je recherche un studio meublé avec climatisation, budget {USER['loyer_min']}–{USER['loyer_max']}
€/mois charges incluses, idéalement à Eixample, Gràcia, Sant Antoni ou Poblenou,
pour une prise de possession entre le {USER['move_in']}.

Mon dossier locataire :
- Indemnité VIE : {USER['vie_min']}–{USER['vie_max']} €/mois nets, contrat ferme de 12 mois
- Garante : ma mère, revenus ≈ {USER['garante_revenu']} €/mois nets, capable de signer un aval
- Documents disponibles immédiatement : contrat VIE, bulletins de salaire de
  la garante, avis d'imposition, pièce d'identité
- Aval bancaire (3–6 mois bloqués) possible si nécessaire

Je serai à Barcelone du {USER['voyage']} et je peux organiser des visites en
journée comme en soirée. Auriez-vous des biens correspondant à mon profil que
nous pourrions visiter pendant ces 4 jours ?

Je communique en français, anglais et espagnol basique.

Bien cordialement,
{USER['prenom']} {USER['nom']}
{USER['email']}
{USER['tel']}
"""


def body_en(agent_name: str, agence: str) -> str:
    salut = f"Hi {agent_name}," if agent_name else f"Hi {agence} team,"
    return f"""{salut}

My name is {USER['prenom']} {USER['nom']}, I'm {USER['age']}, and I'm joining
{USER['employeur']} ({USER['adresse_bureau']}) on June 1st under a 12-month
VIE contract (a French state-sponsored international employment program).

I'm looking for a furnished studio with air conditioning, budget €{USER['loyer_min']}–{USER['loyer_max']}/month
all included, preferably in Eixample, Gràcia, Sant Antoni or Poblenou, with a
move-in date between May 20 and 31.

My tenant profile:
- VIE allowance: €{USER['vie_min']}–{USER['vie_max']}/month net, fixed 12-month contract
- Guarantor: my mother, ≈ €{USER['garante_revenu']}/month net income, ready to co-sign
- Documents ready: VIE contract, guarantor's payslips, tax return, ID
- Bank guarantee (3–6 months deposit) possible if required

I'll be in Barcelona May 17–20. I can attend viewings any time during these 4 days.
Do you have any properties matching this profile that we could visit?

I speak French, English, and basic Spanish.

Best regards,
{USER['prenom']} {USER['nom']}
{USER['email']}
{USER['tel']}
"""


def body_es(agent_name: str, agence: str) -> str:
    salut = f"Buenos días {agent_name}," if agent_name else f"Buenos días equipo de {agence},"
    return f"""{salut}

Me llamo {USER['prenom']} {USER['nom']}, tengo {USER['age']} años y me incorporo
a la empresa {USER['employeur']} ({USER['adresse_bureau']}) el 1 de junio con
un contrato VIE de 12 meses (programa francés de empleo internacional respaldado
por el Estado).

Busco un estudio amueblado con aire acondicionado, presupuesto {USER['loyer_min']}–{USER['loyer_max']}
€/mes gastos incluidos, preferentemente en Eixample, Gràcia, Sant Antoni o Poblenou,
con entrada entre el 20 y el 31 de mayo.

Mi perfil:
- Asignación VIE: {USER['vie_min']}–{USER['vie_max']} €/mes netos, contrato fijo 12 meses
- Avalista: mi madre, ingresos ≈ {USER['garante_revenu']} €/mes netos
- Documentos listos: contrato VIE, nóminas de mi avalista, declaración de la
  renta, DNI
- Aval bancario (3–6 meses) posible si es necesario

Estaré en Barcelona del 17 al 20 de mayo. ¿Tendrían algún piso que pudiera
visitar durante esos 4 días?

Hablo francés, inglés y español básico.

Un saludo,
{USER['prenom']} {USER['nom']}
{USER['email']}
{USER['tel']}
"""


def build_email(agence_row: dict) -> tuple[str, str]:
    langue = (agence_row.get("langue") or "fr").lower()
    agent = (agence_row.get("prenom_agent") or "").strip()
    agence = (agence_row.get("nom_agence") or "").strip()
    if langue == "en":
        return SUBJECT_EN, body_en(agent, agence)
    if langue == "es":
        return SUBJECT_ES, body_es(agent, agence)
    return SUBJECT_FR, body_fr(agent, agence)


def send_smtp(to_addr: str, subject: str, body: str) -> None:
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = to_addr
    msg["Reply-To"] = USER["email"]
    msg.set_content(body)

    ctx = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=ctx) as smtp:
        smtp.login(SMTP_USER, SMTP_PASS)
        smtp.send_message(msg)


def main() -> int:
    parser = argparse.ArgumentParser(description="Mail-merge agences immo Barcelone")
    parser.add_argument("--dry-run", action="store_true", help="Prévisualise sans envoyer")
    parser.add_argument("--csv", default="agences.csv", help="Chemin du CSV (défaut: agences.csv)")
    parser.add_argument("--limit", type=int, default=0, help="Limiter à N envois (0 = tous)")
    args = parser.parse_args()

    csv_path = Path(args.csv)
    if not csv_path.is_absolute():
        csv_path = Path(__file__).parent / csv_path
    if not csv_path.exists():
        print(f"❌ CSV introuvable : {csv_path}", file=sys.stderr)
        return 1

    with csv_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    fieldnames = list(rows[0].keys()) if rows else []
    sent_count = 0
    skipped_count = 0

    global SMTP_PASS
    if not args.dry_run and not SMTP_PASS:
        SMTP_PASS = getpass.getpass(
            "Gmail App Password (16 chars, ne sera pas affiché) : "
        ).strip().replace(" ", "")

    for row in rows:
        email = (row.get("email") or "").strip()
        statut = (row.get("statut") or "").strip().lower()
        agence = (row.get("nom_agence") or "").strip()
        if not email:
            print(f"⏭️  {agence}: pas d'email, skip")
            skipped_count += 1
            continue
        if statut == "envoye":
            print(f"⏭️  {agence}: déjà envoyé le {row.get('date_envoi')}, skip")
            skipped_count += 1
            continue
        if args.limit and sent_count >= args.limit:
            print(f"🛑 Limite atteinte ({args.limit})")
            break

        subject, body = build_email(row)

        if args.dry_run:
            print("=" * 60)
            print(f"To: {email}  ({agence})")
            print(f"Subject: {subject}")
            print("-" * 60)
            print(body)
            print()
            sent_count += 1
            continue

        try:
            send_smtp(email, subject, body)
            row["statut"] = "envoye"
            row["date_envoi"] = date.today().isoformat()
            sent_count += 1
            print(f"✅ {agence}: envoyé à {email}")
        except Exception as exc:  # noqa: BLE001
            print(f"❌ {agence}: échec ({exc})", file=sys.stderr)

        time.sleep(DELAY_BETWEEN_EMAILS_SEC)

    if not args.dry_run:
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    print()
    print(f"Total prévisualisé/envoyé : {sent_count}")
    print(f"Skippés : {skipped_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
