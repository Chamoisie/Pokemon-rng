import os
import random
from PIL import Image
import sys
import time


pokedex = []

SPRITE_FOLDER = "sprites"
SHINY_FOLDER = "shiny"
SHINY_CHANCE = 0.05

def rng_sprite():
    if random.random()<SHINY_CHANCE:
        folder = SHINY_FOLDER
    else:
        folder = SPRITE_FOLDER

    file = [f for f in os.listdir(folder)
                if f.lower().endswith((".png", ".jpg", ".jpeg"))]

    if not file:
        raise FileNotFoundError(f"No directory found in  {SPRITE_FOLDER}")

    sprite = random.choice(file)
    return os.path.join(folder, sprite), sprite, folder == SHINY_FOLDER



def afficher_sprite(path):
    image = Image.open(path)
    facteur = 4
    largeur, hauteur = image.size
    image = image.resize((largeur * facteur, hauteur * facteur), Image.NEAREST)
    image.show()
    time.sleep(3)
possible_choices = 4

while True:
    print("\nQue voulez-vous faire ?")
    print("1: RNG !")
    print("2: Open pokedex")
    print("3: Delete one pokemon (by the number)")
    print("4: Leave(will delete your pokedex)")
    choix = int(input("What do you want to do? : "))

    if choix == 1:
        chemin, nom_fichier, is_shiny = rng_sprite()
        pokedex.append(nom_fichier)
        if is_shiny:
            print(f"You pulled a shiny!! It's! {nom_fichier}")
        else:
            print(f"You pulled {nom_fichier}")
        afficher_sprite(chemin)
    
    elif choix == 2:
        if pokedex:
            print("Here are your pokemons:" )
        for j in range(len(pokedex)):
            print("-", j + 1, pokedex[j])

        print(f"you have {len(pokedex)} pokemons !")
    elif choix == 3:
        i=int(input("Which pokemon do you want to delete?"))
        del pokedex [i]
    elif choix == 4:
        print("See you later")
        quit()
    elif choix > possible_choices:
        print("This choice is not avaible")
