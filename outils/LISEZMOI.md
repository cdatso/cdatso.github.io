# outils

## `fond.py` — le fond dessiné de l'accueil

Générateur du fichier `fond.svg` posé en fond de `index.html` (variable CSS `--fond`) : un grand anneau de traits très
fins, centré, sans figure pleine ni texte. Python 3.12, bibliothèque standard seule ; graine fixée par variante — la même
commande réécrit le même fichier, octet pour octet.

**Régénérer le fond en service** (depuis la racine du dépôt) :

```
python outils/fond.py --variante 5 --traitement c --sortie fond.svg
```

Combinaison retenue par Christo Datso le 11/10/2026 (n°15, second tour) : variante 5 « tissé » (graine 1405, 480
cordes, trait 0,6), traitement c (or `#b8993f` et gris `#8a8578`, opacité du groupe 0,50, un seul fichier pour les deux
thèmes), cadre carré 1300 × 1300 où l'anneau tient entier. Dans `index.html`, l'anneau prend la plus petite dimension de
l'écran (`background-size: min(100vw, 100vh)`) : il s'affiche en entier sur bureau comme sur mobile.
Empreinte SHA-256 du fichier attendu :
`f6e9ae41b768d724def282ca26f1bbe26a62435990d838a2bb15c3b7aa098564` (11 643 o).

Options : `--variante 1..5` (régulier, brisé, double, dispersé, tissé), `--traitement a|b|c` (gris neutre ; encre par
thème, avec `--theme clair|sombre` ; or et gris), `--sortie <fichier.svg>`, `--largeur` (référence 1300).

## Licence et crédit

Dessin généré, © Christo Datso. Œuvre nouvelle, inspirée des dessins de Tiziana Alocci et CS Projects (*Rendah Mag*
n°14) ; aucune image du magazine n'est copiée, recadrée ni vectorisée. Le crédit figure au pied de l'accueil.
