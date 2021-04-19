import os
from direct import task
from direct.showbase.ShowBase import *
from panda3d.core import *
from direct.gui.OnscreenText import OnscreenText
from direct.task import Task, TaskManagerGlobal
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

text_titles_titles = ["INJUSTICIA", "INDIVIDUO",
                      "BUSQUEDA DE JUSTICIA", "FALLA DE SISTEMA"]

class Textcrawl(ShowBase):

    story = [
        ["TIJUANA 2033", "Las Pulgas es fumigada.", "Quien fumiga al fumigador?",
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
        self.do_method_later= taskMgr.doMethodLater(0,self.update,'update')
                
    def update(self, task):
        textposx=0
        textposy=-0.5
        self.textdelay = 1
        for x in self.story:
            for y in x:
            
                if y == 'TIJUANA 2033':
                    logging.debug('esto se ignora')
                else:
                    self.make_text= taskMgr.doMethodLater(self.textdelay,self.print_text,
                                                                'print_text',extraArgs=[task,y,textposx,textposy])
                    self.textdelay+=2
                    textposy += 0.1
            textposy+=0.05
        
        return task.done
    
    

    def print_text(self, task, y, textposx, textposy):
        """Esta funcion es con la que imprimire lentamente el text crawl en vez de todo del putaso
        """
        self.textObject = OnscreenText(text=y, pos=(textposx,textposy),scale=0.05,  fg=[240,240,240,1], wordwrap=45, bg=[0,0,0,0.1])
        return task.done
    
game = Textcrawl()
game.run()

