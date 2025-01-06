# Jeu du Pendu - Main File

class Pendu:
    def __init__(self):
        self.mot = ""
        self.lettres_trouvees = []
        self.erreurs = 0
        self.max_erreurs = 6
        self.mots = ["python", "programmation", "algorithme", "variable", "fonction"]
    
    def choisir_mot(self):
        from random import choice
        self.mot = choice(self.mots)
        return self.mot
    
    def afficher_mot_cache(self):
        return ' '.join([lettre if lettre in self.lettres_trouvees else '_' for lettre in self.mot])
    
    def verifier_lettre(self, lettre):
        if lettre in self.mot:
            self.lettres_trouvees.append(lettre)
            return True
        self.erreurs += 1
        return False
    
    def partie_gagnee(self):
        return all(lettre in self.lettres_trouvees for lettre in self.mot)
    
    def partie_perdue(self):
        return self.erreurs >= self.max_erreurs

def main():
    jeu = Pendu()
    print("Bienvenue dans le Jeu du Pendu!")
    jeu.choisir_mot()
    
    while not (jeu.partie_gagnee() or jeu.partie_perdue()):
        print(f"\nMot : {jeu.afficher_mot_cache()}")
        print(f"Erreurs : {jeu.erreurs}/{jeu.max_erreurs}")
        
        lettre = input("\nProposez une lettre : ").lower()
        if len(lettre) != 1:
            print("Veuillez entrer une seule lettre!")
            continue
            
        if lettre in jeu.lettres_trouvees:
            print("Vous avez déjà proposé cette lettre!")
            continue
            
        if jeu.verifier_lettre(lettre):
            print("Bravo! Lettre trouvée!")
        else:
            print("Dommage, cette lettre n'est pas dans le mot!")
    
    if jeu.partie_gagnee():
        print(f"\nFélicitations! Vous avez gagné! Le mot était : {jeu.mot}")
    else:
        print(f"\nPerdu! Le mot était : {jeu.mot}")

if __name__ == "__main__":
    main()