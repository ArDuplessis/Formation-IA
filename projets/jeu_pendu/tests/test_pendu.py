import unittest
from src.main import Pendu

class TestPendu(unittest.TestCase):
    def setUp(self):
        self.jeu = Pendu()
        self.jeu.mot = "python"  # Mot fixe pour les tests
    
    def test_initialisation(self):
        self.assertEqual(self.jeu.erreurs, 0)
        self.assertEqual(self.jeu.max_erreurs, 6)
        self.assertEqual(len(self.jeu.lettres_trouvees), 0)
    
    def test_affichage_mot_cache(self):
        self.assertEqual(self.jeu.afficher_mot_cache(), "_ _ _ _ _ _")
        
        self.jeu.lettres_trouvees.append('p')
        self.assertEqual(self.jeu.afficher_mot_cache(), "p _ _ _ _ _")
    
    def test_verifier_lettre_correcte(self):
        self.assertTrue(self.jeu.verifier_lettre('p'))
        self.assertEqual(self.jeu.erreurs, 0)
        self.assertIn('p', self.jeu.lettres_trouvees)
    
    def test_verifier_lettre_incorrecte(self):
        self.assertFalse(self.jeu.verifier_lettre('z'))
        self.assertEqual(self.jeu.erreurs, 1)
        self.assertNotIn('z', self.jeu.lettres_trouvees)
    
    def test_partie_gagnee(self):
        for lettre in 'python':
            self.jeu.lettres_trouvees.append(lettre)
        self.assertTrue(self.jeu.partie_gagnee())
    
    def test_partie_perdue(self):
        self.jeu.erreurs = 6
        self.assertTrue(self.jeu.partie_perdue())

if __name__ == '__main__':
    unittest.main()