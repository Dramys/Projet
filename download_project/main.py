
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

# Classe représentant la résolution d'équations
class Resoudre:
    def __init__(self, a, b, c=0):
        # POO : Les attributs sont stockés dans une instance de la classe
        self.a = a
        self.b = b
        self.c = c

    # Résolution d'une équation du premier degré : ax + b = 0
    def premier(self):
        if self.a == 0:
            return "Pas de solution" if self.b != 0 else "Infinité de solutions"
        return [-self.b / self.a]  # Liste contenant la solution

    # Résolution d'une équation du second degré : ax² + bx + c = 0
    def second(self):
        delta = self.b**2 - 4*self.a*self.c
        if delta < 0:
            return "Pas de solution réelle"
        elif delta == 0:
            return [-self.b / (2*self.a)]  # Liste contenant une seule solution
        else:
            return self.calcul_racines(delta)  # Appel récursif pour calculer les racines

    # Méthode récursive pour calculer les racines de l'équation
    def calcul_racines(self, delta, racines=[]):
        if len(racines) == 2:
            return racines
        if len(racines) == 0:
            racines.append((-self.b - delta**0.5) / (2*self.a))
        else:
            racines.append((-self.b + delta**0.5) / (2*self.a))
        return self.calcul_racines(delta, racines)

    # Méthode pour afficher la courbe de la fonction
    def afficher_courbe(self, premier_degre=False):
        x = np.linspace(-10, 10, 400)
        if premier_degre:
            y = self.a * x + self.b
            titre = f'{self.a}x + {self.b}'
        else:
            y = self.a * x**2 + self.b * x + self.c
            titre = f'{self.a}x² + {self.b}x + {self.c}'

        plt.plot(x, y, label=titre)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(True, linestyle='--', linewidth=0.5)
        plt.legend()
        plt.title("Courbe de l'équation")
        plt.show()

# Classe gérant l'interface graphique
class Interface:
    def __init__(self, window):
        self.window = window
        self.window.title("Résolveur d'équations")
        self.window.iconbitmap("calculatrice.ico")  # Ajout de l'icône
        self.window.configure(padx=20, pady=20)  # Ajout du padding

        # Création des labels et champs de saisie
        tk.Label(window, text="Coefficient a:").grid(row=0, column=0, pady=5)
        tk.Label(window, text="Coefficient b:").grid(row=1, column=0, pady=5)
        tk.Label(window, text="Coefficient c (si second degré):").grid(row=2, column=0, pady=5)

        self.entree_a = tk.Entry(window)
        self.entree_b = tk.Entry(window)
        self.entree_c = tk.Entry(window)

        self.entree_a.grid(row=0, column=1, pady=5)
        self.entree_b.grid(row=1, column=1, pady=5)
        self.entree_c.grid(row=2, column=1, pady=5)

        # Ajout d'un espace entre les champs et les boutons
        tk.Label(window, text="").grid(row=3, column=0, columnspan=2, pady=10)

        # Boutons pour résoudre les équations
        tk.Button(window, text="Résoudre 1er degré", command=self.resoudre_premier).grid(row=4, column=0, pady=5)
        tk.Button(window, text="Résoudre 2nd degré", command=self.resoudre_second).grid(row=4, column=1, pady=5)
        tk.Button(window, text="Afficher la courbe 1er degré", command=self.afficher_courbe_premier).grid(row=5, column=0, pady=5)
        tk.Button(window, text="Afficher la courbe 2nd degré", command=self.afficher_courbe_second).grid(row=5, column=1, pady=5)

    # Méthode pour récupérer les coefficients saisis
    def recup_coefs(self):
        try:
            a = float(self.entree_a.get())
            b = float(self.entree_b.get())
            c = float(self.entree_c.get()) if self.entree_c.get() else 0
            return a, b, c
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des nombres valides")
            return None

    # Méthode pour résoudre une équation du premier degré
    def resoudre_premier(self):
        coeffs = self.recup_coefs()
        if coeffs:
            a, b, _ = coeffs  # On ignore c car il n'est pas utilisé ici
            solver = Resoudre(a, b)
            solution = solver.premier()
            messagebox.showinfo("Solution", f"Solution: {solution}")

    # Méthode pour résoudre une équation du second degré
    def resoudre_second(self):
        coeffs = self.recup_coefs()
        if coeffs:
            a, b, c = coeffs
            solver = Resoudre(a, b, c)
            solution = solver.second()
            messagebox.showinfo("Solutions", f"Solutions: {solution}")

    # Méthodes pour afficher les courbes des équations
    def afficher_courbe_premier(self):
        coeffs = self.recup_coefs()
        if coeffs:
            a, b, _ = coeffs
            solver = Resoudre(a, b)
            solver.afficher_courbe(premier_degre=True)

    def afficher_courbe_second(self):
        coeffs = self.recup_coefs()
        if coeffs:
            a, b, c = coeffs
            solver = Resoudre(a, b, c)
            solver.afficher_courbe()

# Point d'entrée du programme
if __name__ == "__main__":
    window = tk.Tk()
    app = Interface(window)
    window.mainloop()
