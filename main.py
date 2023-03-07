from fastapi import FastAPI
import json
import random

app = FastAPI()
word_file = 'mots-rose.json'

class RandomWord:

    def __init__(self, chemin_fichier):
        # Ouverture du fichier JSON contenant les objets
        with open(chemin_fichier, 'r') as f:
            self.objets = json.load(f)
        # Initialisation d'une liste vide pour stocker les objets déjà choisis
        self.objets_deja_choisis = []

    def choisir_objet(self):
        # Vérification que tous les objets n'ont pas encore été proposés
        if len(self.objets_deja_choisis) < len(self.objets):
            objet_choisi = random.choice(self.objets)
            # Vérification que l'objet n'a pas déjà été choisi
            while objet_choisi in self.objets_deja_choisis:
                objet_choisi = random.choice(self.objets)
            # Ajout de l'objet choisi à la liste des objets déjà choisis
            self.objets_deja_choisis.append(objet_choisi)
            return objet_choisi
        else:
            self.objets_deja_choisis.clear()
            objet_choisi = random.choice(self.objets)
            return objet_choisi

words = RandomWord(word_file)
@app.get("/")
async def root():
    return words.choisir_objet()    