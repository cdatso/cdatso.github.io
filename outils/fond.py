#!/usr/bin/env python3
# fond.py -- generateur SVG du fond dessine de l'accueil www.cdatso.be
# (BKL-CDC-021, lot 2). Python 3.12, bibliotheque standard seule.
#
# Le dessin : un grand anneau de traits tres fins, centre, sans figure pleine
# ni texte. Cinq variantes (caracteres), trois traitements de couleur :
#   a  un seul fichier, gris neutre, pour les deux themes ;
#   b  deux fichiers, encre du theme clair / encre du theme sombre ;
#   c  un seul fichier aux couleurs du site (or et gris).
# Graine fixee par variante : la meme commande ecrit le meme fichier, octet
# pour octet. Le trace est identique d'un traitement a l'autre ; seules les
# couleurs et l'opacite changent.
#
# Dessin genere, (c) Christo Datso. Oeuvre nouvelle, inspiree des dessins de
# Tiziana Alocci et CS Projects (Rendah Mag n.14) -- structure "anneau de
# traits fins" ; rien n'est copie des images du magazine.
#
# Fond retenu (combinaison 15 : variante 5 "tisse", traitement c) :
#   python outils/fond.py --variante 5 --traitement c --sortie fond.svg
# Autres exemples :
#   python outils/fond.py --variante 1 --traitement a --sortie essai.svg
#   python outils/fond.py --variante 1 --traitement b --theme sombre --sortie essai-sombre.svg

import argparse
import math
import random
import sys

# Cadre carre, anneau centre et entier (decision de Christo Datso, 11/10/2026 :
# "entier a l'ecran" ; l'ancien cadre 1400 x 1100 rognait le haut de l'anneau).
REF_LARGEUR = 1300
REF_HAUTEUR = 1300
CX, CY = 650.0, 650.0  # centre de l'anneau, a l'echelle de reference

GRIS = "#8a8578"
OR = "#b8993f"
ENCRE_CLAIR = "#1a1a1a"
ENCRE_SOMBRE = "#f0ede6"

# Opacite du groupe : plafond de tout le dessin (les traits qui se croisent
# ne s'additionnent pas au-dela). Seuils releves par Christo Datso le
# 11/10/2026 (second tour, "environ x3" : 0.18/0.22 -> 0.50/0.55, traits x2) ;
# un fichier commun aux deux themes (a, c) respecte le plus bas.
PLAFOND = {"clair": 0.5, "sombre": 0.55}
OPACITE = {"a": 0.5, "b-clair": 0.5, "b-sombre": 0.55, "c": 0.5}

VARIANTES = {
    1: {"caractere": "regulier", "graine": 1401, "traits": 720, "epaisseur": 1.0},
    2: {"caractere": "brise", "graine": 1402, "traits": 1300, "epaisseur": 0.9},
    3: {"caractere": "double", "graine": 1403, "traits": 1160, "epaisseur": 0.9},
    4: {"caractere": "disperse", "graine": 1404, "traits": 1600, "epaisseur": 0.8},
    5: {"caractere": "tisse", "graine": 1405, "traits": 480, "epaisseur": 0.6},
}

TAU = 2.0 * math.pi


def _polaire(r, th):
    return CX + r * math.cos(th), CY + r * math.sin(th)


def _trait(r, th, direction, longueur):
    """Segment centre au point (r, th), oriente selon direction."""
    x, y = _polaire(r, th)
    dx = 0.5 * longueur * math.cos(direction)
    dy = 0.5 * longueur * math.sin(direction)
    return (x - dx, y - dy, x + dx, y + dy)


def v1_regulier(rng, n):
    # traits radiaux a pas egal ; longueur modulee lentement : l'anneau respire
    segs = []
    for i in range(n):
        th = TAU * i / n + rng.uniform(-0.002, 0.002)
        mod = (0.5 + 0.25 * math.sin(3 * th + 0.7) + 0.15 * math.sin(7 * th + 1.9)
               + 0.1 * math.sin(13 * th))
        longueur = 40 + 110 * mod * (0.85 + 0.3 * rng.random())
        r1 = 470 + rng.gauss(0, 4)
        x1, y1 = _polaire(r1, th)
        x2, y2 = _polaire(r1 + longueur, th)
        segs.append((x1, y1, x2, y2))
    return segs


def v2_brise(rng, n):
    # tirets tangents : orbites interrompues sur cinq rayons, et quelques libres
    orbites = (470, 505, 540, 575, 610)
    segs = []
    for _ in range(n):
        th = rng.uniform(0, TAU)
        if rng.random() < 0.7:
            r = rng.choice(orbites) + rng.gauss(0, 5)
        else:
            r = 540 + rng.gauss(0, 50)
        direction = th + math.pi / 2 + rng.uniform(-0.25, 0.25)
        segs.append(_trait(r, th, direction, rng.uniform(10, 54)))
    return segs


def v3_double(rng, n):
    # deux anneaux : radial fin a l'exterieur, oblique a l'interieur
    segs = []
    n_ext = int(n * 0.55)
    for i in range(n_ext):
        th = TAU * i / n_ext + rng.uniform(-0.003, 0.003)
        r1 = 560 + rng.gauss(0, 3)
        longueur = rng.uniform(20, 60)
        x1, y1 = _polaire(r1, th)
        x2, y2 = _polaire(r1 + longueur, th)
        segs.append((x1, y1, x2, y2))
    for _ in range(n - n_ext):
        th = rng.uniform(0, TAU)
        r = 390 + rng.gauss(0, 18)
        segs.append(_trait(r, th, th + 0.5, rng.uniform(30, 90)))
    return segs


def v4_disperse(rng, n):
    # nuee annulaire : rayon et direction disperses autour de l'anneau
    segs = []
    for _ in range(n):
        th = rng.uniform(0, TAU)
        r = 500 + rng.gauss(0, 55)
        direction = th + rng.gauss(0, 0.6)
        longueur = min(60.0, 12 + rng.expovariate(1 / 16))
        segs.append(_trait(r, th, direction, longueur))
    return segs


def v5_tisse(rng, n):
    # cordes courtes tendues sur le cercle : l'anneau nait de leur enveloppe
    rayon = 560
    segs = []
    for _ in range(n):
        th = rng.uniform(0, TAU)
        delta = 0.6 + 0.6 * rng.random()
        x1, y1 = _polaire(rayon + rng.uniform(-6, 6), th)
        x2, y2 = _polaire(rayon + rng.uniform(-6, 6), th + delta)
        segs.append((x1, y1, x2, y2))
    return segs


DESSINS = {1: v1_regulier, 2: v2_brise, 3: v3_double, 4: v4_disperse, 5: v5_tisse}


def _nombre(v):
    s = "%.1f" % v
    if s.endswith(".0"):
        s = s[:-2]
    if s == "-0":
        s = "0"
    return s


def _chemin(segs, k):
    morceaux = []
    for x1, y1, x2, y2 in segs:
        morceaux.append("M%s %sl%s %s" % (_nombre(x1 * k), _nombre(y1 * k),
                                          _nombre((x2 - x1) * k), _nombre((y2 - y1) * k)))
    return "".join(morceaux).replace(" -", "-")


def dessiner(variante, traitement, theme, largeur):
    p = VARIANTES[variante]
    rng = random.Random(p["graine"])
    segs = DESSINS[variante](rng, p["traits"])
    k = largeur / REF_LARGEUR
    hauteur = round(REF_HAUTEUR * k)
    ep = "%g" % p["epaisseur"]

    if traitement == "b":
        cle = "b-" + theme
        opacite = OPACITE[cle]
        if opacite > PLAFOND[theme]:
            raise ValueError("opacite au-dessus du plafond")
        couleur = ENCRE_CLAIR if theme == "clair" else ENCRE_SOMBRE
        corps = '<path stroke="%s" d="%s"/>' % (couleur, _chemin(segs, k))
    else:
        opacite = OPACITE[traitement]
        if opacite > min(PLAFOND.values()):
            raise ValueError("opacite au-dessus du plafond")
        if traitement == "a":
            corps = '<path stroke="%s" d="%s"/>' % (GRIS, _chemin(segs, k))
        else:
            # c : un trait sur trois environ en or, le reste en gris ; tirage a
            # part pour que le trace reste celui des traitements a et b
            tri = random.Random(p["graine"] + 7)
            ors, gris = [], []
            for s in segs:
                (ors if tri.random() < 0.35 else gris).append(s)
            corps = ('<path stroke="%s" d="%s"/><path stroke="%s" d="%s"/>'
                     % (OR, _chemin(ors, k), GRIS, _chemin(gris, k)))

    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">'
            '<g fill="none" stroke-width="%s" stroke-linecap="round" opacity="%s">'
            '%s</g></svg>\n' % (largeur, hauteur, largeur, hauteur, ep, _nombre2(opacite), corps))


def _nombre2(v):
    return ("%.2f" % v).rstrip("0").rstrip(".")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Fond dessine de l'accueil (anneau de traits fins).")
    ap.add_argument("--variante", type=int, choices=sorted(VARIANTES), required=True)
    ap.add_argument("--traitement", choices=("a", "b", "c"), required=True)
    ap.add_argument("--theme", choices=("clair", "sombre"))
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--largeur", type=int, default=REF_LARGEUR)
    a = ap.parse_args(argv)
    if a.traitement == "b" and not a.theme:
        ap.error("le traitement b demande --theme clair|sombre")
    if a.traitement != "b" and a.theme:
        ap.error("--theme ne vaut que pour le traitement b")
    svg = dessiner(a.variante, a.traitement, a.theme, a.largeur)
    with open(a.sortie, "w", encoding="ascii", newline="\n") as f:
        f.write(svg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
