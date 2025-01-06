# Jeu du Pendu

## Description
Implémentation du jeu classique du pendu en Python.

## Fonctionnalités
- Interface console
- Dictionnaire de mots français
- Affichage graphique ASCII du pendu
- Gestion du score
- Sauvegarde des meilleurs scores

## Structure
```python
class Pendu:
    def __init__(self):
        self.mot = ""
        self.lettres_trouvees = []
        self.erreurs = 0
        self.max_erreurs = 6
    
    def choisir_mot(self):
        # Choisir un mot aléatoire
        pass
    
    def jouer(self):
        # Logique principale du jeu
        pass
    
    def afficher_pendu(self):
        # Affichage ASCII du pendu
        pass
```

## Installation
```bash
git clone [url]
cd jeu_pendu
python main.py
```

## Tests
```bash
python -m unittest tests/
```