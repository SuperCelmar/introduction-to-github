# 04 — Templates de contact

Tous les templates utilisent des **placeholders** entre `{{...}}`. Les remplir
manuellement OU laisser le mail-merge le faire automatiquement (cf.
[`automatisations/`](automatisations/)).

Placeholders disponibles : `{{prenom_agent}}`, `{{nom_agence}}`, `{{ref_annonce}}`, `{{adresse_annonce}}`.

---

## EMAIL-AGENCE-FR — Premier contact agence (français)

**Objet** : Recherche studio meublé Eixample/Gràcia – VIE Hello Pomelo, dossier solide

Bonjour {{prenom_agent}},

Je m'appelle Florent Lin, j'ai 24 ans, et je rejoins l'entreprise Hello Pomelo
(Carrer de Mallorca, 100) le **1er juin** dans le cadre d'un VIE de 12 mois
(Volontariat International en Entreprise, contrat sponsorisé par l'État
français).

Je recherche un **studio meublé avec climatisation**, budget **1000–1300 €/mois
charges incluses**, idéalement à Eixample, Gràcia, Sant Antoni ou Poblenou,
pour une **prise de possession entre le 20 et le 31 mai**. Je privilégie un
**contrato de arrendamiento de vivienda habitual** (12 mois ou plus).

**Mon dossier locataire** :
- Indemnité VIE : **2500–3000 €/mois nets**, contrat ferme de 12 mois
- **Garante** : ma mère, revenus ≈ 5000 €/mois nets, capable de signer un aval
- Documents disponibles immédiatement : contrat VIE, bulletins de salaire de
  la garante, avis d'imposition, pièce d'identité
- **RDV NIE** confirmé au consulat espagnol le **21 mai** (justificatif disponible)
- Aval bancaire (3–6 mois bloqués) possible si nécessaire

Je serai à Barcelone du **17 au 20 mai** et je peux organiser des visites en
journée comme en soirée. Auriez-vous des biens correspondant à mon profil que
nous pourrions visiter pendant ces 4 jours ?

Je communique en français, anglais et espagnol basique.

Bien cordialement,
**Florent Lin**
📧 1florentlin@gmail.com
📱 +33 7 81 63 66 63

---

## EMAIL-AGENCE-EN — Same in English

**Subject**: Furnished studio search Eixample/Gràcia – VIE at Hello Pomelo, strong file

Hi {{prenom_agent}},

My name is Florent Lin, I'm 24, and I'm joining Hello Pomelo (Carrer de
Mallorca, 100) on **June 1st** under a 12-month VIE contract (a French
state-sponsored international internship/employment program).

I'm looking for a **furnished studio with air conditioning**, budget
**€1,000–1,300/month all included**, preferably in Eixample, Gràcia, Sant
Antoni or Poblenou, with a **move-in date between May 20 and 31**. I'd
prefer a **habitual residence lease** (12+ months) rather than a
temporada contract.

**My tenant profile**:
- VIE allowance: **€2,500–3,000/month net**, fixed 12-month contract
- **Guarantor**: my mother, ≈ €5,000/month net income, ready to co-sign
- Documents ready: VIE contract, guarantor's payslips, tax return, ID
- **NIE appointment** confirmed at the Spanish consulate on **May 21** (proof available)
- Bank guarantee (3–6 months deposit) possible if required

I'll be in Barcelona from **May 17 to 20**. I can attend viewings any time
during these 4 days. Do you have any properties matching this profile that we
could visit?

I speak French, English, and basic Spanish.

Best,
**Florent Lin**
📧 1florentlin@gmail.com
📱 +33 7 81 63 66 63

---

## EMAIL-AGENCE-ES — Mismo en español

**Asunto**: Búsqueda estudio amueblado Eixample/Gràcia – VIE en Hello Pomelo, dossier sólido

Buenos días {{prenom_agent}},

Me llamo Florent Lin, tengo 24 años y me incorporo a la empresa Hello Pomelo
(Carrer de Mallorca, 100) el **1 de junio** con un contrato VIE de 12 meses
(programa francés de empleo internacional respaldado por el Estado).

Busco un **estudio amueblado con aire acondicionado**, presupuesto
**1.000–1.300 €/mes gastos incluidos**, preferentemente en Eixample, Gràcia,
Sant Antoni o Poblenou, con **entrada entre el 20 y el 31 de mayo**.
Prefiero un **contrato de arrendamiento de vivienda habitual** (12 meses
o más) en lugar de temporada.

**Mi perfil**:
- Asignación VIE: **2.500–3.000 €/mes netos**, contrato fijo 12 meses
- **Avalista**: mi madre, ingresos ≈ 5.000 €/mes netos
- Documentos listos: contrato VIE, nóminas de mi avalista, declaración de la
  renta, DNI
- **Cita previa NIE** confirmada en el consulado español el **21 de mayo** (justificante disponible)
- Aval bancario (3–6 meses) posible si es necesario

Estaré en Barcelona del **17 al 20 de mayo**. ¿Tendrían algún piso que pudiera
visitar durante esos 4 días?

Hablo francés, inglés y español básico.

Un saludo,
**Florent Lin**
📧 1florentlin@gmail.com
📱 +34 disponible / +33 7 81 63 66 63

---

## IDEALISTA-FR — Message court particulier (français)

> Idealista limite souvent à ~500 caractères dans le formulaire de contact.

Bonjour, je m'appelle Florent Lin, 24 ans, je commence un VIE de 12 mois chez
Hello Pomelo (Carrer de Mallorca 100) le 1er juin. Indemnité 2500–3000 €/mois
+ garante (ma mère, 5000 €/mois). Studio meublé idéal pour moi.
Réf : {{ref_annonce}}. Je suis à Barcelone du 17 au 20 mai pour visiter,
disponible 9h–21h. Move-in 20–31 mai. Dossier complet (contrat VIE, fiches
de paie garante, ID) prêt à envoyer. Pourrions-nous fixer une visite ?
Merci ! Florent — 1florentlin@gmail.com — +33 7 81 63 66 63

---

## IDEALISTA-EN — Short owner message (English)

Hi, I'm Florent Lin, 24, starting a 12-month VIE contract at Hello Pomelo
(Carrer de Mallorca 100) on June 1st. Net allowance €2,500–3,000/month +
guarantor (my mother, €5,000/month). Looking for a furnished studio.
Listing: {{ref_annonce}}. I'll be in Barcelona May 17–20 to visit, available
9am–9pm. Move-in May 20–31. Full dossier (VIE contract, guarantor payslips,
ID) ready to send. Could we book a viewing? Thanks — Florent —
1florentlin@gmail.com — +33 7 81 63 66 63

---

## IDEALISTA-ES — Mensaje corto al propietario

Hola, soy Florent Lin, 24 años, empiezo un VIE de 12 meses en Hello Pomelo
(Carrer de Mallorca 100) el 1 de junio. Asignación 2.500–3.000 €/mes +
avalista (mi madre, 5.000 €/mes). Busco estudio amueblado.
Ref: {{ref_annonce}}. Estaré en Barcelona del 17 al 20 de mayo, disponible
9h–21h. Entrada 20–31 mayo. Dossier completo (contrato VIE, nóminas del
avalista, DNI) listo. ¿Podríamos concertar una visita? Gracias — Florent —
1florentlin@gmail.com — +34 / +33 7 81 63 66 63

---

## RELANCE-J3 — Email de relance (FR)

**Objet** : Relance — recherche studio Barcelone (Florent Lin, VIE Hello Pomelo)

Bonjour {{prenom_agent}},

Je me permets de relancer ma demande envoyée le {{date_envoi}}. Je serai à
Barcelone dans {{nb_jours}} jours pour visiter, et je tenais à vérifier que
vous aviez bien reçu mon dossier.

Si rien ne correspond actuellement à mon profil, je suis preneur de toute
suggestion (autres quartiers, légère adaptation budget, etc.).

Merci d'avance,
Florent Lin — +33 7 81 63 66 63

---

## SCRIPT-TEL — Appel téléphonique 30 secondes (FR/EN)

> Si l'agence répond en espagnol, demande poliment "*¿Habla inglés o francés, por favor?*"

**FR** :
> Bonjour, je m'appelle Florent Lin. Je vous ai envoyé un email il y a quelques
> jours pour la recherche d'un studio meublé. Je commence un VIE chez Hello
> Pomelo le 1er juin et je serai à Barcelone du 17 au 20 mai pour visiter.
> Avez-vous reçu mon dossier ? Auriez-vous des biens à me proposer ?

**EN** :
> Hello, my name is Florent Lin. I emailed you a few days ago about a furnished
> studio. I'm starting a VIE at Hello Pomelo on June 1st and I'll be in Barcelona
> May 17 to 20 for viewings. Did you receive my file? Do you have any properties
> to suggest?

---

## CONFIRMATION-VISITE — Après accord (FR/EN)

**FR** :
Bonjour {{prenom_agent}}, je confirme la visite du **{{date_visite}}** à
**{{heure_visite}}** au {{adresse_annonce}} (réf {{ref_annonce}}). Mon
téléphone sur place : +33 7 81 63 66 63 (WhatsApp activé). À très vite !

**EN** :
Hi {{prenom_agent}}, confirming the viewing on **{{date_visite}}** at
**{{heure_visite}}** at {{adresse_annonce}} (ref {{ref_annonce}}). My phone:
+33 7 81 63 66 63 (WhatsApp on). See you soon!

---

## OFFRE-VISITE — Email post-visite avec dossier (FR)

**Objet** : Candidature ferme — {{adresse_annonce}} — Florent Lin

Bonjour {{prenom_agent}},

Je vous remercie pour la visite de ce {{date_visite}} au {{adresse_annonce}}.
**Le bien me correspond parfaitement et je souhaite officiellement candidater.**

Vous trouverez en pièces jointes :
1. Contrat VIE Hello Pomelo (lettre d'embauche)
2. 3 derniers bulletins de salaire de ma garante (ma mère)
3. Avis d'imposition de ma garante
4. Pièces d'identité (ma carte / passeport + celui de ma garante)
5. Lettre d'engagement de la garante signée

**Conditions** :
- Loyer demandé : {{loyer}} €/mois charges incluses
- Caution : 1 + 2 mois (ou aval bancaire si requis)
- Date d'entrée souhaitée : {{date_entree}}
- Frais d'agence acceptés selon barème usuel

Je suis prêt à signer dès cette semaine et à effectuer le virement de la
caution sous 24 h après accord.

Bien cordialement,
Florent Lin — 1florentlin@gmail.com — +33 7 81 63 66 63
