# 03 — Agences immobilières à contacter

> Liste indicative. Vérifie chaque site/email avant envoi : les coordonnées
> peuvent évoluer. Toutes les agences ci-dessous opèrent à Barcelone et ont
> été choisies pour leur compatibilité expat (FR/EN) ou leur volume Eixample
> / Gràcia / Poblenou en meublé.
>
> Pour automatiser l'envoi, utilise [`automatisations/mail_merge.py`](automatisations/mail_merge.py)
> avec le CSV [`automatisations/agences.csv`](automatisations/agences.csv).
> Vérifie / corrige les emails dans le CSV avant de lancer le script.

## Tier 1 — Agences expat-friendly (priorité maximale)

| Agence | Spécialité | Site |
|---|---|---|
| **ShBarcelona** | Meublé court/moyen/long terme, FR/EN/ES, expat-friendly | shbarcelona.com |
| **Apartment Barcelona** | Meublé moyen/long terme, EN | apartmentbarcelona.com |
| **Barcelona Home** | Meublé multilingue (FR/EN/ES/DE) | barcelona-home.com |
| **Friendly Rentals** | Meublé qualité, EN | friendlyrentals.com |
| **aTemporal Barcelona** | Meublé temporada (1–11 mois), multilingue | atemporalbarcelona.es |
| **HomeRunner BCN** | Long terme expat, EN | homerunner.com |
| **Eixample Flats** | Spécialiste Eixample meublé | eixampleflats.com |
| **Lasose Properties** | Relocation expat, FR/EN | lasose.com |

## Tier 2 — Agences locales avec offre meublée

| Agence | Spécialité | Site |
|---|---|---|
| **Engel & Völkers Barcelona** | Premium, plusieurs bureaux Eixample | engelvoelkers.com (cherche "Barcelona Eixample") |
| **Lucas Fox** | Premium meublé, anglophone | lucasfox.com |
| **Fincas Eva** | Local, équipe anglophone | fincaseva.com |
| **Casamona** | Long terme + meublé, EN/FR | casamona.com |
| **Habitat Apartments** | Meublé moyen/long terme | habitatapartments.com |
| **Smart Move BCN** | Search + relocation expat | smartmovebcn.com |
| **Vivendex** | Réseau local Barcelone, gros volume | vivendex.com |
| **Tecnocasa Barcelona** | Réseau d'agences indépendantes par quartier | tecnocasa.es |
| **Inmobiliaria Sergi Barcelona** | Eixample / Gràcia | (chercher Idealista profil pro) |
| **Forcadell** | Long terme, sérieux | forcadell.com |

## Tier 3 — Agences "francophones" Barcelone (à confirmer)

Vérifier l'activité courante (certaines disparaissent / fusionnent) :

- **Tour Eiffel Immobilier** (BCN, focus francophones)
- **Le Cabinet d'Eugénie** / autres cabinets francophones répertoriés sur l'Annuaire de la Chambre Française de Commerce et d'Industrie de Barcelone (CCFE)
- **French Connection Barcelona** (réseau expats français)

> 💡 **Astuce** : la **CCFE Barcelone** ([www.lachambre.es](https://www.lachambre.es)) tient un annuaire des entreprises francophones, dont des agences. Demande-leur la liste, c'est gratuit.

## Comment construire ta liste finale

1. Ouvre [`automatisations/agences.csv`](automatisations/agences.csv)
2. Pour chaque ligne sans email : vas sur le site, copie l'email "info@" / "rentals@" / "alquiler@"
3. Si pas d'email, note l'URL du **formulaire de contact** dans la colonne `form_url`
4. Garde au moins **15 agences** avec email valide pour le mail-merge

## Approche de contact

- **Premier contact** : email mass-mailing personnalisé (cf. [`04-templates.md`](04-templates.md), template *EMAIL-AGENCE-FR*)
- **Relance J+3 si pas de réponse** : appel téléphonique court (script dans `04-templates.md`)
- **À Barcelone** : passer en personne dans 2–3 agences clés du tier 1 (Eixample), ça change tout — beaucoup d'annonces ne sortent jamais en ligne.
