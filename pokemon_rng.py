import os
import random
from PIL import Image

SPRITE_FOLDER = "sprites"
SHINY_FOLDER = "shiny"

def rng_sprite():
    fichiers = [f for f in os.listdir(SPRITE_FOLDER)
                if f.lower().endswith((".png", ".jpg", ".jpeg"))]

    if not fichiers:
        raise FileNotFoundError(f"rien dans {SPRITE_FOLDER}")

    sprite = random.choice(fichiers)
    return os.path.join(SPRITE_FOLDER, sprite), sprite

def rng_sprite_shiny():
    shiny_pkm = [f for f in os.listdir(SHINY_FOLDER)
             if f.lower().endwith((".png"))]
    if not shiny_pkm:
        raise FileNotFoundError(f"rien dans {SHINY_FOLDER}")
    shiny_sprite = random.choice(shiny_pkm)
    return os.path.join(SHINY_FOLDER,shiny_pkm),shiny_pkm


def afficher_sprite(path):
    image = Image.open(path)
    facteur = 4
    largeur, hauteur = image.size
    image = image.resize((largeur * facteur, hauteur * facteur), Image.NEAREST)
    image.show()

if __name__ == "__main__":
    chemin, nom_fichier = rng_sprite() 
    print(f"Pokémon tiré : {nom_fichier}")
    afficher_sprite(chemin)
