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

    def choisir_objet(self):
        return random.choice(self.objets)
        
words = RandomWord(word_file)

@app.get("/")
async def root():
    return words.choisir_objet()    