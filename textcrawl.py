import os
from direct.showbase.ShowBase import *
from panda3d.core import *
from direct.gui.OnscreenText import OnscreenText
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

text_titles_titles = ["INJUSTICIA", "INDIVIDUO",
                      "BUSQUEDA DE JUSTICIA", "FALLA DE SISTEMA"]

class Textcrawl(ShowBase):

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
        self.scene.setScale(1, 1, 1)
        self.scene.setPos(0, 25, 0)
        self.make_text()
     

    def make_text(self):
        """AUN NO LO HE HECHO
        """
        font = loader.loadFont('/fonts/comic/comicbd.ttf')
        font.setPageSize(512,512)
        
        textposx=-0.5
        textposy=0.02
        for x in self.story:
            for y in self.story[x]:
                time.sleep(1)
                textObject = OnscreenText(text=y, pos=(textposx,textposy),scale=0.07)
                textposy += 0.5


game = Textcrawl()
game.run()