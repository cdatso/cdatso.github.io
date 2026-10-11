# cdatso.github.io

Dépôt racine du domaine **[www.cdatso.be](https://www.cdatso.be)**, servi par
GitHub Pages.

## Rôle

Ce dépôt porte trois choses, et rien d'autre :

- **`CNAME`** — la liaison du domaine personnalisé `www.cdatso.be` à GitHub
  Pages. Ce fichier ne se supprime jamais : sans lui, le domaine cesse de
  répondre.
- **`index.html`** — la page d'accueil : portail d'auteur, quatre entrées.
- **`fond.svg`** et **`outils/`** — le fond dessiné de l'accueil (un anneau de
  traits fins, posé par la variable CSS `--fond`) et son générateur
  `outils/fond.py` ; la commande de régénération est dans
  `outils/LISEZMOI.md`.

## Projets servis sous le domaine

| Chemin | Projet | Dépôt |
|---|---|---|
| `/analyses-de-films/` | Analyses de films — critiques et études de cinéma sourcées | [cdatso/analyses-de-films](https://github.com/cdatso/analyses-de-films) |
| `/filmographie/` | Filmographie — inventaire de films (prototype) | [cdatso/filmographie](https://github.com/cdatso/filmographie) |
| `/chatbot-catalogue/` | Chatbot catalogue — questions sur les analyses publiées | [cdatso/chatbot-catalogue](https://github.com/cdatso/chatbot-catalogue) |
| `/comprendre-ia/` | Comprendre et discuter l'IA — conférences, dossiers et documentation | [cdatso/comprendre-ia](https://github.com/cdatso/comprendre-ia) |
| `demande.cdatso.be` | Demander une analyse de film — formulaire public (sous-domaine) | service de demande |
| `/bibliographie/` | Bibliographie — textes publiés, page générée depuis le classeur de référence | [cdatso/bibliographie](https://github.com/cdatso/bibliographie) |

Chaque projet vit dans son propre dépôt, publié comme *project site* GitHub
Pages ; ce dépôt-ci ne fait qu'ancrer le domaine et l'accueil.

## Notes de tenue

- Le domaine est enregistré chez un registrar externe ; le DNS pointe vers
  GitHub Pages, le certificat HTTPS est provisionné par GitHub.
- L'architecture est volontairement portable : l'hébergeur est interchangeable
  sans changer les adresses publiques.
