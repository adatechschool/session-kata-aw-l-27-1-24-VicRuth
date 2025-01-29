# Jeu d'Awelé 

# Etape 1:Classe pour le plateau de jeu

class Plateau_jeu:
    def __init__(self):
        # Plateau : 2 rangées de 6 cases, chaque case contenant 0 graines au départ
        self.cases = [[0 for _ in range(6)] for _ in range(2)]
        self.labels = ['A', '  B', '  C', '  D', '  E', '  F', 'G', '  H', '  I', '  J', '  K', '  L']

    def display(self):
        # Affichage des cases en mode console
        print("    " + "  ".join(self.labels[:6]))
        print("   " + "  ".join(f"({self.cases[0][i]})" for i in range(6)))
        print("   " + "  ".join(f"({self.cases[1][i]})" for i in range(6)))
        print("    " + "  ".join(self.labels[6:]))

    def isEmpty(self):
        # Vérifie si toutes les cases contiennent 0 graines
        return all(graines == 0 for row in self.cases for graines in row)

# Exemple d'initialisation et d'affichage
plateau = Plateau_jeu()
plateau.display()
print("Plateau vide ?", plateau.isEmpty())

#Etape 2:Classe pour le joueur
class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.score = 0

    def incrementer_score(self, graines):
        self.score += graines
        print(f"{self.nom} a récolté {graines} graines. Score actuel : {self.score}")


#Etape 3 et 4:

# Classe pour le plateau de jeu
class Plateau:
    def __init__(self):
        # Plateau : 2 rangées de 6 cases, chaque case contenant 4 graines au départ
        self.cases = [[4 for _ in range(6)] for _ in range(2)]
        self.labels = ['A', '  B', '  C', '  D', '  E', '  F', 'G', '  H', '  I', '  J', '  K', '  L']

    def display(self):
        # Affichage des cases en mode console
        print("    " + "  ".join(self.labels[:6]))
        print("   " + "  ".join(f"({self.cases[0][i]})" for i in range(6)))
        print("   " + "  ".join(f"({self.cases[1][i]})" for i in range(6)))
        print("    " + "  ".join(self.labels[6:]))

    def isEmpty(self):
        # Vérifie si toutes les cases contiennent 0 graines
        return all(graines == 0 for row in self.cases for graines in row)

    def case_suivante(self, ligne, colonne):
        # Calculer la case suivante
        if ligne == 0 and colonne == 5:  # Dernière case de la rangée du haut
            return 1, 5  # Passer à la rangée du bas
        elif ligne == 1 and colonne == 0:  # Première case de la rangée du bas
            return 0, 0  # Revenir à la rangée du haut
        else:
            return ligne, (colonne + 1) if ligne == 0 else (colonne - 1)

    def semer(self, ligne, colonne):
        graines = self.cases[ligne][colonne]
        self.cases[ligne][colonne] = 0  # Vider la case
        while graines > 0:
            ligne, colonne = self.case_suivante(ligne, colonne)
            self.cases[ligne][colonne] += 1
            graines -= 1



# Gestion du jeu
class Jeu:
    def __init__(self):
        self.plateau = Plateau()
        self.joueur1 = Joueur("Joueur 1")
        self.joueur2 = Joueur("Joueur 2")
        self.tour = self.joueur1  # Le joueur 1 commence

    def jouer_tour(self):
        self.plateau.display()
        print(f"C'est au tour de {self.tour.nom}")
        case = input("Choisissez une case (A à L) : ").strip().upper()
        if case not in self.plateau.labels:
            print("Case invalide, veuillez réessayer.")
            return True  # Rejouer le tour

        index = self.plateau.labels.index(case)
        ligne = 0 if index < 6 else 1
        colonne = index % 6

        if self.plateau.cases[ligne][colonne] == 0:
            print("Cette case est vide, choisissez une autre case.")
            return True  # Rejouer le tour

        self.plateau.semer(ligne, colonne)

        # Vérifier si le plateau est vide
        if self.plateau.isEmpty():
            print("Fin du jeu !")
            self.afficher_scores()
            return False  # Fin du jeu

        # Changer de joueur
        self.tour = self.joueur1 if self.tour == self.joueur2 else self.joueur2
        return True

    def afficher_scores(self):
        print(f"{self.joueur1.nom} : {self.joueur1.score}")
        print(f"{self.joueur2.nom} : {self.joueur2.score}")

# Exemple d'utilisation
jeu = Jeu()
while jeu.jouer_tour():
    pass
