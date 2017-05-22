#!/usr/bin/python
# -*- coding:UTF-8 -*

from  interface.root import *


def presentation():  # Ma Présentation
    root_clear()
    canvas_fen = creer_canvas(root)
    canvas_fen.create_text(dimx_ / 6 + 25, 50,
                            text="Projet : Algègre Linéaire",
                            font="/font/myfont 35 ",
                            fill="#00F5FF"
                        )
    canvas_fen.create_text(dimx_ / 6 + 25, 150,
                            text="Prénoms : El Hadj Babacar",
                            font="/font/myfont 30 ",
                            fill="#00F5FF"
                        )
    canvas_fen.create_text(dimx_ / 6 + 25, 250,
                            text="Noms : Cissé",
                            font="/font/myfont 30 ",
                            fill="#00F5FF"
                        )
    canvas_fen.create_text(dimx_ / 6 + 25, 350,
                            text="Classe : DIC1 Informatiquer",
                            font="/font/myfont 30 ",
                            fill="#00F5FF"
                        )
    bouton_suiv = Button(root,
                            text="Suivant",
                            command=root_menu,
                            relief="groove",
                            font="/font/myfont 8 ",
                            bg="#00868B",
                            fg="black", activebackground="#ADD8E6"
                        )
    bouton_quitt = Button(root,
                        text="Quitter",
                        command=root_fermer,
                        relief="groove",
                        font="/font/myfont 8 ",
                        bg="#EE3B3B",
                        fg="white",
                        activebackground="#FF0000"
                    )
    canvas_fen.create_window(dimx_ / 2 + 18, dimy_ - 50,
                                window=bouton_suiv
                            )
    canvas_fen.create_window(dimx_ / 2 + 150, dimy_ - 50,
                                window=bouton_quitt
                            )
    canvas_fen.pack()


def __main__():
    presentation()
    root.mainloop()


if __name__ == "__main__":
    __main__()

