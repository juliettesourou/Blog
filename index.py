from tkinter import *
from tkinter import messagebox
#from tkcalendar import *
#import mysql.connector

class Demandeur:
    def __init__(self, nom, prenom, sexe, date_naissance, lieu_naissance, situation_matrimoniale, profession, type_logement):
        self.__nom = nom
        self.__prenom = prenom
        self.__sexe = sexe
        self.__date_naissance = date_naissance
        self.__lieu_naissance = lieu_naissance
        self.__situation_matrimoniale = situation_matrimoniale
        self.__profession = profession
        self.__type_logement = type_logement

    # Getters
    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_sexe(self):
        return self.__sexe

    def get_date_naissance(self):
        return self.__date_naissance

    def get_lieu_naissance(self):
        return self.__lieu_naissance

    def get_situation_matrimoniale(self):
        return self.__situation_matrimoniale

    def get_profession(self):
        return self.__profession

    def get_type_logement(self):
        return self.__type_logement

    # Setters
    def set_nom(self, nom):
        self.__nom = nom

    def set_prenom(self, prenom):
        self.__prenom = prenom

    def set_sexe(self, sexe):
        self.__sexe = sexe

    def set_date_naissance(self, date_naissance):
        self.__date_naissance = date_naissance

    def set_lieu_naissance(self, lieu_naissance):
        self.__lieu_naissance = lieu_naissance

    def set_situation_matrimoniale(self, situation_matrimoniale):
        self.__situation_matrimoniale = situation_matrimoniale

    def set_profession(self, profession):
        self.__profession = profession

    def set_type_logement(self, type_logement):
        self.__type_logement = type_logement

# Interface graphique avec Tkinter
def soumettre():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    sexe = entry_sexe.get()
    date_naissance = entry_date_naissance.get()
    lieu_naissance = entry_lieu_naissance.get()
    situation_matrimoniale = entry_situation_matrimoniale.get()
    profession = entry_profession.get()
    type_logement = entry_type_logement.get()

    # Créer une instance de Demandeur
    Infos_demandeur = Demandeur(nom, prenom, sexe, date_naissance, lieu_naissance, situation_matrimoniale, profession, type_logement)

    # Afficher les informations du demandeur dans la console
    print("Nom:", Infos_demandeur.get_nom())
    print("Prénom:", Infos_demandeur.get_prenom())
    print("Sexe:", Infos_demandeur.get_sexe())
    print("Date de naissance:", Infos_demandeur.get_date_naissance())
    print("Lieu de naissance:", Infos_demandeur.get_lieu_naissance())
    print("Situation matrimoniale:", Infos_demandeur.get_situation_matrimoniale())
    print("Profession:", Infos_demandeur.get_profession())
    print("Type de logement:", Infos_demandeur.get_type_logement())

# Création de l'interface graphique
fenetre = Tk()
fenetre.geometry('400x500')  
fenetre.title('Inscription')

# Labels

Label(fenetre, text="Nom :").grid(row=0, column=0, padx=10, pady=5)
Label(fenetre, text="Prénom :").grid(row=1, column=0, padx=10, pady=5)
Label(fenetre, text="Sexe :").grid(row=2, column=0, padx=10, pady=5)
Label(fenetre, text="Date de naissance :").grid(row=3, column=0, padx=10, pady=5)
Label(fenetre, text="Lieu de naissance :").grid(row=4, column=0, padx=10, pady=5)
Label(fenetre, text="Situation matrimoniale :").grid(row=5, column=0, padx=10, pady=5)
Label(fenetre, text="Profession :").grid(row=6, column=0, padx=10, pady=5)
Label(fenetre, text="Type de logement :").grid(row=7, column=0, padx=10, pady=5)

# Entrées
entry_nom = Entry(fenetre)
entry_nom.grid(row=0, column=1, padx=10, pady=5)
entry_prenom = Entry(fenetre)
entry_prenom.grid(row=1, column=1, padx=10, pady=5)
entry_sexe = Entry(fenetre)
entry_sexe.grid(row=2, column=1, padx=10, pady=5)
entry_date_naissance = Entry(fenetre)
entry_date_naissance.grid(row=3, column=1, padx=10, pady=5)
entry_lieu_naissance = Entry(fenetre)
entry_lieu_naissance.grid(row=4, column=1, padx=10, pady=5)
entry_situation_matrimoniale = Entry(fenetre)
entry_situation_matrimoniale.grid(row=5, column=1, padx=10, pady=5)
entry_profession = Entry(fenetre)
entry_profession.grid(row=6, column=1, padx=10, pady=5)
entry_type_logement = Entry(fenetre)
entry_type_logement.grid(row=7, column=1, padx=10, pady=5)

# Bouton Soumettre
Button(fenetre, text="Soumettre", command=soumettre).grid(row=8, column=0, columnspan=2, pady=10)

#pour la verification sur une autre page

def verifier_informations():
    # Récupérer les informations des entrées
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    sexe = entry_sexe.get()
    date_naissance = entry_date_naissance.get()
    lieu_naissance = entry_lieu_naissance.get()
    situation_matrimoniale = entry_situation_matrimoniale.get()
    profession = entry_profession.get()
    type_logement = entry_type_logement.get()

    # Créer une nouvelle fenêtre pour la vérification
    fenetre_verification = Tk()
    fenetre_verification.title('Vérification des informations')
    fenetre_verification.geometry('400x300')  # Changer la taille de la fenêtre

    # Afficher les informations dans la nouvelle fenêtre
    Label(fenetre_verification, text="Nom: " + nom).pack()
    Label(fenetre_verification, text="Prénom: " + prenom).pack()
    Label(fenetre_verification, text="Sexe: " + sexe).pack()
    Label(fenetre_verification, text="Date de naissance: " + date_naissance).pack()
    Label(fenetre_verification, text="Lieu de naissance: " + lieu_naissance).pack()
    Label(fenetre_verification, text="Situation matrimoniale: " + situation_matrimoniale).pack()
    Label(fenetre_verification, text="Profession: " + profession).pack()
    Label(fenetre_verification, text="Type de logement: " + type_logement).pack()

    # Fonction pour soumettre ou modifier les informations
    def soumettre_ou_modifier():
        # Vous pouvez ajouter ici la logique pour envoyer ou modifier les informations en fonction de l'action de l'utilisateur
        # Par exemple, vous pouvez fermer la fenêtre de vérification ici après l'envoi ou la modification

        fenetre_verification.destroy()  # Fermer la fenêtre de vérification

    # Bouton pour soumettre ou modifier les informations
    Button(fenetre_verification, text="Confirmer", command=soumettre_ou_modifier).pack()

    # Fonction pour revenir à la page d'inscription
    def retour_inscription():
        fenetre_verification.destroy()  # Fermer la fenêtre de vérification
        fenetre.deiconify()  # Afficher la fenêtre d'inscription

    # Bouton de retour à la page d'inscription
    Button(fenetre_verification, text="Retour à l'inscription", command=retour_inscription).pack()

    # Bouton pour accéder à la page d'inscription en cas de changement d'informations
    def retour_modification():
        fenetre_verification.destroy()  # Fermer la fenêtre de vérification
        fenetre.deiconify()  # Afficher la fenêtre d'inscription

    # Bouton de retour à la page d'inscription en cas de changement d'informations
    Button(fenetre_verification, text="Modifier les informations", command=retour_modification).pack()

# Bouton pour vérifier les informations
Button(fenetre, text="Vérifier Informations", command=verifier_informations).grid(row=8, column=0, columnspan=2, pady=10)




# Ajoutez cette importation pour gérer les noms de fichiers
import os

# Fonction pour écrire les informations dans un fichier texte
def creer_fiche_inscription(nom, prenom, date_naissance, lieu_naissance, profession, situation_matrimoniale, type_logement):
    nom_fichier = f"{nom}_{prenom}.txt"
    with open(nom_fichier, 'w') as fichier:
        fichier.write(f"Nom: {nom}\n")
        fichier.write(f"Prénom: {prenom}\n")
        fichier.write(f"Date de naissance: {date_naissance}\n")
        fichier.write(f"Lieu de naissance: {lieu_naissance}\n")
        fichier.write(f"Profession: {profession}\n")
        fichier.write(f"Situation matrimoniale: {situation_matrimoniale}\n")
        fichier.write(f"Type de logement: {type_logement}\n")
    print(f"Fiche d'inscription créée: {nom_fichier}")

# Fonction pour vérifier les informations et créer la fiche d'inscription
def verifier_informations():
    # Récupérer les informations des entrées
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    date_naissance = entry_date_naissance.get()
    lieu_naissance = entry_lieu_naissance.get()
    profession = entry_profession.get()
    situation_matrimoniale = entry_situation_matrimoniale.get()
    type_logement = entry_type_logement.get()

    # Créer une nouvelle fenêtre pour la vérification
    fenetre_verification = Tk()
    fenetre_verification.title('Vérification des informations')
    fenetre_verification.geometry('400x300')  # Changer la taille de la fenêtre

    # Afficher les informations dans la nouvelle fenêtre
    Label(fenetre_verification, text="Nom: " + nom).pack()
    Label(fenetre_verification, text="Prénom: " + prenom).pack()
    Label(fenetre_verification, text="Date de naissance: " + date_naissance).pack()
    Label(fenetre_verification, text="Lieu de naissance: " + lieu_naissance).pack()
    Label(fenetre_verification, text="Profession: " + profession).pack()
    Label(fenetre_verification, text="Situation matrimoniale: " + situation_matrimoniale).pack()
    Label(fenetre_verification, text="Type de logement: " + type_logement).pack()

    # Fonction pour soumettre les informations
    def soumettre_informations():
        # Créer la fiche d'inscription avec les informations fournies
        creer_fiche_inscription(nom, prenom, date_naissance, lieu_naissance, profession, situation_matrimoniale, type_logement)
        fenetre_verification.destroy()  # Fermer la fenêtre de vérification

    # Bouton pour confirmer et créer la fiche d'inscription
    Button(fenetre_verification, text="Confirmer", command=soumettre_informations).pack()


# Options pour le type de logement
options_type_logement = ["LT1", "LT2", "LT3", "LT4"]
var_type_logement = StringVar(fenetre)
var_type_logement.set(options_type_logement[0])  # Sélectionnez le premier élément par défaut

# Liste déroulante pour le type de logement
opt_menu_type_logement = OptionMenu(fenetre, var_type_logement, *options_type_logement)
opt_menu_type_logement.grid(row=7, column=1, padx=10, pady=5)
# Modifier le bouton pour vérifier les informations
Button(fenetre, text="Vérifier Informations", command=verifier_informations).grid(row=8, column=0, columnspan=2, pady=10)

fenetre.mainloop()




