from direct.showbase.ShowBase import *
from panda3d.core import *



import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class textcrawl(ShowBase):

    story = [
        ["TIJUANA 2033.", "Las Pulgas es fumigada.", "Quien fumiga al fumigador?",
            "WE LIVE IN A SOCIETY", "Where honor is a distant memory"],
        ["Xolos International compro la presa de Tijuana en 2023"],
        ["Tijuana cedio a ser una democracia directa en 2025"],
        ["Dubai y China compraron McDonalds en 2026 debido al colapso espcultativo del mercado de gallos en Asia."],
        ["En 2024 los Estados Unidos prohibio en su enteridad la produccion de carnes a base de animales.",
            "El SOYBOI PARTY ha remplazado al partido libertariano como la astilla de circulo politico en Washington "],
        ["Mandato numero 1984 permite el uso continuo en espacios publicos de mascaras de cobertura completa tras la pandemia de 2022 de covid-21"]]
    # Load the environment model.
    def __init__(self):
        ShowBase.__init__(self)
        self.scene = self.loader.loadModel("models/fondo_menu.bam")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)


    def make_text(self):
        """AUN NO LO HE HECHO
        """
        pass


text_titles_titles = ["INJUSTICIA", "INDIVIDUO",
                          "BUSQUEDA DE JUSTICIA", "FALLA DE SISTEMA"]

 
game_test = textcrawl()
game_test()