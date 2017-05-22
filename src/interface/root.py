# -*-coding:UTF-8-*

from tkinter import Canvas

from .affichage_saisie import *
from .getroot import root, dimy_


def creer_canvas(window):  # Création d'un canvas
    canvas = Canvas(window,
                    width=dimx_,
                    height=dimy_,
                    bg="#002B36"
                )
    return canvas


def effacer(fonction):
    root_clear()
    fonction()


def root_fermer():  # Message de confirmation fermeture de la fenêtre
    if messagebox.askyesno('Confirmation de la fermeture', 'Êtes-vous sûr de vouloir quitter le programme?'):
        root.quit()


def root_clear():  # Détruire la fenêtre
    for w in root.winfo_children():
        w.destroy()


def root_navigation(canvas, back):
    bouton_prec = Button(root,
                        text="Précédent",
                        relief="groove",
                        font="/font/myfont 8",
                        command=back,
                        bg="#00868B",
                        fg="black",
                        activebackground="#ADD8E6"
                    )
    bouton_quitt = Button(root,
                        text="Sortir",
                        command=root_fermer,
                        relief="groove",
                        font="/font/myfont 8",
                        bg="#EE3B3B",
                        fg="white",
                        activebackground="#FF0000"
                    )
    canvas.create_window(dimx_ / 2 - 150, dimy_ - 50, window=bouton_prec)
    canvas.create_window(dimx_ / 2 + 150, dimy_ - 50,
                            window=bouton_quitt
                        )
    canvas.pack()


def root_menu():
    root_clear()
    canvas = creer_canvas(root)
    canvas.create_text(dimx_ / 6 + 25, 50,
                        text="Choisissez une option pour continuer :",
                        font="/font/myfont 20",
                        fill="#00F5FF"
                    )
    bouton_operation = Button(root, command=root_opmatrices_menu,
                                text="Opérations sur les matrices",
                                relief="groove",
                                font="/font/myfont 15",
                                bg="#00868B",
                                fg="black",
                                activebackground="#ADD8E6"
                            )
    bouton_syslin = Button(root,
                            command=root_syslineaires_menu,
                            text="      Systémes linéaires       ",
                            relief="groove",
                            font="/font/myfont 15",
                            bg="#00868B",
                            fg="black",
                            activebackground="#ADD8E6"
                        )
    bouton_quitt = Button(root,
                            text="Quitter",
                            command=root_fermer,
                            relief="groove",
                            font="/font/myfont 8",
                            bg="#EE3B3B",
                            fg="white",
                            activebackground="#FF0000"
                        )
    canvas.create_window(dimx_ / 6 + 25, 150,
                            window=bouton_operation
                        )
    canvas.create_window(dimx_ / 6 + 25, 250,
                            window=bouton_syslin
                        )
    canvas.create_window(dimx_ / 2 + 150, dimy_ - 50,
                            window=bouton_quitt
                        )
    canvas.pack()


def root_syslineaires_menu():
    root_clear()
    canvas = creer_canvas(root)
    saisie_1matrice(root, canvas, affiche_saisiesyslin)
    root_navigation(canvas, root_menu)
    canvas.pack()


def root_opmatrices_menu():  # Choix de l'opération à affectuer
    root_clear()
    canvas = creer_canvas(root)
    canvas.create_text(dimx_ / 6 + 25, 50,
                        text="    Opérations de bases sur les matrices",
                        font="/font/myfont 15 ",
                        fill="#00F5FF"
                    )
    bouton_1matrice = Button(root,
                                text="Opérations sur une matrice",
                                relief="groove",
                                font="/font/myfont 14",
                                command=root_op1matrices_menu,
                                bg="#00868B",
                                fg="black",
                                activebackground="#ADD8E6"
                            )
    bouton_2matrice = Button(root,
                                text="Opérations sur deux matrices",
                                relief="groove",
                                font="/font/myfont 14",
                                command=root_op2matrices_menu,
                                bg="#00868B",
                                fg="black",
                                activebackground="#ADD8E6"
                            )
    canvas.create_window(dimx_ / 6 + 25, 150, window=bouton_1matrice)
    canvas.create_window(dimx_ / 6 + 25, 250, window=bouton_2matrice)
    root_navigation(canvas, root_menu)
    canvas.pack()


def root_op1matrices_menu():
    root_clear()
    canvas = creer_canvas(root)
    saisie_1matrice(root, canvas, affiche_saisie_1matrice)
    root_navigation(canvas, root_opmatrices_menu)
    canvas.pack()


def root_op2matrices_menu():
    root_clear()
    canvas = creer_canvas(root)
    saisie_2matrices(root, canvas)
    root_navigation(canvas, root_opmatrices_menu)
    canvas.pack()


def root_boutons_opmatricemenu1(affiche_saisie, texte):
    root_clear()
    canvas = creer_canvas(root)
    canvas.create_text(dimx_ / 2 + 40, dimy_ / 32,
                        text=texte,
                        font="/font/myfont 9",
                        fill="black"
                    )
    saisie_1matrice(root, canvas, affiche_saisie)


def root_boutons_opmatricemenu2(texte):
    root_clear()
    canvas = creer_canvas(root)
    canvas.create_text(dimx_ / 2 + 60, dimy_ / 32,
                        text=texte,
                        font="/font/myfont 9",
                        fill="black"
                    )
    saisie_2matrices(root, canvas)

