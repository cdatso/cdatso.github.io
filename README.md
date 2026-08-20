# cdatso.github.io

Dépôt racine du domaine **[www.cdatso.be](https://www.cdatso.be)**, servi par
GitHub Pages.

## Rôle

Ce dépôt porte deux choses, et rien d'autre :

- **`CNAME`** — la liaison du domaine personnalisé `www.cdatso.be` à GitHub
  Pages. Ce fichier ne se supprime jamais : sans lui, le domaine cesse de
  répondre.
- **`index.html`** — une page d'accueil provisoire, qui renvoie vers le
  premier projet publié sous le domaine.

## Projets servis sous le domaine

| Chemin | Projet | Dépôt |
|---|---|---|
| `/analyses-de-films/` | Analyses de films — critiques et études de cinéma sourcées | [cdatso/analyses-de-films](https://github.com/cdatso/analyses-de-films) |
| `/filmographie/` | Filmographie — inventaire de films (prototype) | [cdatso/filmographie](https://github.com/cdatso/filmographie) |

Chaque projet vit dans son propre dépôt, publié comme *project site* GitHub
Pages ; ce dépôt-ci ne fait qu'ancrer le domaine et l'accueil.

## Notes de tenue

- Le domaine est enregistré chez un registrar externe ; le DNS pointe vers
  GitHub Pages, le certificat HTTPS est provisionné par GitHub.
- L'architecture est volontairement portable : l'hébergeur est interchangeable
  sans changer les adresses publiques.
