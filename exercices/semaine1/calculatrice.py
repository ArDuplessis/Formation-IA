def addition(a, b):
    """Additionne deux nombres"""
    return a + b

def soustraction(a, b):
    """Soustrait b de a"""
    return a - b

def multiplication(a, b):
    """Multiplie deux nombres"""
    return a * b

def division(a, b):
    """Divise a par b"""
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b

def calculatrice():
    """Fonction principale de la calculatrice"""
    print("Bienvenue dans la calculatrice Python!")
    
    while True:
        print("\nOpérations disponibles :")
        print("1. Addition (+)")
        print("2. Soustraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Quitter")
        
        choix = input("\nChoisissez une opération (1-5): ")
        
        if choix == '5':
            print("Au revoir!")
            break
            
        try:
            a = float(input("Entrez le premier nombre: "))
            b = float(input("Entrez le deuxième nombre: "))
            
            if choix == '1':
                resultat = addition(a, b)
                print(f"{a} + {b} = {resultat}")
            elif choix == '2':
                resultat = soustraction(a, b)
                print(f"{a} - {b} = {resultat}")
            elif choix == '3':
                resultat = multiplication(a, b)
                print(f"{a} * {b} = {resultat}")
            elif choix == '4':
                resultat = division(a, b)
                print(f"{a} / {b} = {resultat}")
            else:
                print("Choix invalide!")
                
        except ValueError as e:
            print(f"Erreur: {e}")
        except Exception as e:
            print(f"Une erreur est survenue: {e}")

if __name__ == "__main__":
    calculatrice()