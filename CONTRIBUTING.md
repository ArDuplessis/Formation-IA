# Guide de Contribution

## Prérequis
1. Python 3.8 ou supérieur
2. pip pour l'installation des dépendances

## Installation
1. Cloner le repository :
```bash
git clone [url]
cd Formation-IA
```

2. Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

## Structure du Code
- Suivre la PEP 8
- Documenter les fonctions (docstrings)
- Ajouter des tests unitaires

## Tests
```bash
python -m pytest
```

## Pull Requests
1. Fork le repository
2. Créer une branche
3. Commiter les changements
4. Créer une Pull Request