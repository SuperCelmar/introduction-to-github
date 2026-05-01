# Automatisations — recherche appart Barcelone

Trois outils complémentaires pour multiplier ton volume de contacts sans perdre
en personnalisation :

| Outil | Effort setup | Volume traité | Recommandé |
|---|---|---|---|
| [`mail_merge.py`](mail_merge.py) | 10 min | 15–50 emails agences en 1 commande | ✅✅✅ |
| [`idealista-prefill.user.js`](idealista-prefill.user.js) | 5 min (Tampermonkey) | 1 click par annonce Idealista | ✅✅✅ |
| [`tracker-template.csv`](tracker-template.csv) | 2 min (import Sheets) | Suivi de toutes les pistes | ✅✅✅ |

## ⚠️ Cadre éthique et limites

- **Agences (mail-merge)** : envoi groupé d'emails personnalisés à des
  contacts professionnels publics — **pratique standard**, totalement légitime.
- **Idealista (user-script)** : le script **pré-remplit** le formulaire de
  contact dans **ton navigateur**. C'est **toi qui cliques sur "Envoyer"**. Pas
  de scraping, pas de bot d'envoi automatique. Conforme aux CGU d'Idealista
  qui interdit les bots envoyeurs mais autorise l'autocomplétion côté
  utilisateur.
- **Pas de scraping massif** d'Idealista : leur anti-bot est agressif et leur
  ToS l'interdit. Tu te ferais bannir et perdrais ton compte.

## Ordre d'exécution recommandé

1. Installer Tampermonkey + le user-script (cf. ci-dessous)
2. Importer `tracker-template.csv` dans Google Sheets
3. Compléter `agences.csv` avec les emails (voir liste dans
   [`../03-agences.md`](../03-agences.md))
4. Lancer `mail_merge.py --dry-run` pour vérifier
5. Lancer `mail_merge.py` pour envoyer
6. Au fil des annonces Idealista intéressantes : ouvrir l'annonce → cliquer
   le bouton vert "📋 Pré-remplir mon message" du user-script → relire →
   envoyer → logger dans le tracker

---

## 1. `mail_merge.py` — Mailing personnalisé via Gmail

### Pré-requis

- Python 3.9+ (déjà installé sur Mac/Linux ; sur Windows, `python.org`)
- Un compte Gmail (le tien : `1florentlin@gmail.com`)
- Un **mot de passe d'application Gmail** (PAS ton mot de passe principal) :
  1. Activer la **double authentification** sur ton compte Google si ce n'est
     pas fait
  2. Aller sur https://myaccount.google.com/apppasswords
  3. Créer un mot de passe pour "Mail" → Other → "BCN Apartment Search"
  4. Copier le code à 16 caractères (style `xxxx xxxx xxxx xxxx`) — c'est ton
     mot de passe SMTP

### Préparation

1. Édite [`agences.csv`](agences.csv) — vérifie/complète les emails.
2. Édite la signature et le corps du template directement en haut du script
   `mail_merge.py` si tu veux personnaliser au-delà du template par défaut.

### Exécution

```bash
# Dry-run : prévisualise sans envoyer
python mail_merge.py --dry-run

# Envoi réel
python mail_merge.py
```

Le script :
- Lit `agences.csv`
- Pour chaque ligne avec `email` non vide ET `statut` ≠ `envoye`
- Envoie un email personnalisé (FR par défaut, EN si `langue=en`)
- Met à jour `agences.csv` avec `statut=envoye` et `date_envoi`
- Pause de 5 s entre chaque envoi (pour éviter le rate-limit Gmail)

### Limites Gmail

- 500 emails/jour pour un compte Gmail standard. Très largement suffisant.
- Pour rester sous le radar anti-spam, **ne pas dépasser 50 emails/h**.

---

## 2. `idealista-prefill.user.js` — User-script Tampermonkey

### Installation

1. Installer **Tampermonkey** : https://www.tampermonkey.net (extension
   Chrome / Firefox / Edge / Safari)
2. Cliquer sur l'icône Tampermonkey → "Créer un nouveau script"
3. Coller le contenu de [`idealista-prefill.user.js`](idealista-prefill.user.js)
4. Sauvegarder (Ctrl+S)

### Utilisation

1. Aller sur n'importe quelle annonce Idealista
   (ex. `https://www.idealista.com/inmueble/12345/`)
2. Un bouton vert **"📋 Pré-remplir mon message"** apparaît en haut à droite
3. Ouvrir le formulaire de contact (bouton "Contactar" sur la page)
4. Cliquer le bouton vert → ton message est inséré, langue auto-détectée
   selon la langue de l'annonce
5. **Tu** relis et **tu** cliques "Envoyer"

### Personnalisation

En haut du fichier `.user.js`, tu peux modifier :
- Tes coordonnées (`USER_INFO`)
- Le texte du message FR/EN/ES
- La position du bouton (CSS)

---

## 3. `tracker-template.csv` — Suivi des candidatures

### Import dans Google Sheets

1. Ouvre Google Sheets (sheets.new)
2. Fichier → Importer → Importer → Téléverser → choisis
   `tracker-template.csv`
3. Type d'importation : **Remplacer la feuille** + séparateur **Virgule**

### Colonnes

- `id` — n° unique
- `source` — `idealista` / `habitaclia` / `agence` / `spotahome` / autre
- `lien` — URL de l'annonce ou de l'agence
- `quartier` — Eixample / Gràcia / Sant Antoni / Poblenou / etc.
- `loyer` — €/mois charges incluses
- `surface_m2` — m²
- `meuble` — oui/non
- `ac` — oui/non
- `etage` — niveau
- `contact` — nom + tel + email
- `date_contact` — date du 1er message
- `statut` — `envoye` / `repondu` / `visite_caleee` / `visite_faite` / `offre_envoyee` / `accepte` / `refuse` / `abandon`
- `score_visite` — score sur 25 (cf. checklist)
- `date_visite` — date prévue
- `notes` — libre

### Astuce : conditional formatting

Dans Sheets, applique une mise en forme conditionnelle sur la colonne
`statut` :
- `accepte` → fond vert
- `offre_envoyee` → fond jaune
- `visite_caleee` → fond bleu clair
- `refuse` / `abandon` → fond rouge clair

Tu visualises immédiatement où tu en es.

---

## Dépannage

| Problème | Solution |
|---|---|
| Gmail SMTP refuse la connexion | Vérifier que tu utilises un **App Password**, pas ton mdp principal |
| Le script Python ne trouve pas le CSV | Le lancer depuis le dossier `automatisations/` ou ajuster le chemin |
| Le user-script n'apparaît pas | Vérifier que Tampermonkey est activé sur idealista.com (icône doit afficher 1) |
| Erreur encoding CSV | Sauvegarder le CSV en UTF-8 dans ton éditeur |
