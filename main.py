from direct import showbase
import menu
import os
import time
from direct.fsm.FSM import FSM
from direct.gui.DirectButton import DirectButton
from direct.gui.DirectEntry import DirectEntry
from direct.gui.DirectGui import DGG
from direct.gui.DirectGuiGlobals import WITHIN
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.OnscreenText import OnscreenText
from direct.showbase import DirectObject
from direct.showbase.ShowBase import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task, TaskManagerGlobal
from direct.task.TaskManagerGlobal import taskMgr
from direct.particles.ParticleEffect import ParticleEffect
from panda3d.core import *
from direct.showbase.Loader import Loader
import player
import textcrawl
import crawl
import logoscreen
import level1
import level2
import level3
import level4
import endgame
loadPrcFile("config/conf.prc")


text_titles_titles = ["INJUSTICIA", "INDIVIDUO",
                      "BUSQUEDA DE JUSTICIA", "FALLA DE SISTEMA"]

taskAccumulator = 0
story = [
        ["TIJUANA 2033", "Las Pulgas es fumigada.", "Quien fumiga al fumigador?",
            "WE LIVE IN A SOCIETY", "Where honor is a distant memory"],
        ["Xolos International compro la presa de Tijuana en 2023"],
        ["Tijuana cedio a ser una democracia directa en 2025"],
        ["Dubai y China compraron McDonalds en 2026 debido al colapso espcultativo del mercado de gallos en Asia."],
        ["En 2024 los Estados Unidos prohibio en su enteridad la produccion de carnes a base de animales.",
            "El SOYBOI PARTY ha remplazado al partido libertariano como la astilla de circulo politico en Washington "],
        ["Mandato numero 1984 permite el uso continuo en espacios publicos de mascaras de cobertura completa tras la pandemia de 2022 de covid-21"]]


class Tijuana2033(ShowBase, FSM):
    def __init__(self):
        ShowBase.__init__(self)
        FSM.__init__(self, "FSM-Game")
        # self.win
        base.enableParticles()
        self.playerName = ""
        self.IsFullScreen = False
        self.blade_runner = player.Player(self.playerName)
        self.disableMouse()
        self.plight = PointLight("plight")
        self.plight.setColor((1, 1, 1, 1))
        self.plnp = self.render.attachNewNode(self.plight)
        self.render.setLight(self.plnp)
        self.windowProps = WindowProperties()

        self.intro = logoscreen.Logoscreen()
        self.intro.start()

        self.crawl = crawl.testCrawl()
        self.accept('1', self.crawl.start)

        self.menu = menu.Menu(self.windowProps, self)
        self.accept('2', self.menu.start)

        self.l1 = level1.Level1()
        self.accept('3', self.l1.start)

        self.l2 = level2.Level2()
        self.accept('4', self.l2.start)

        self.l3 = level3.Level3()
        self.accept('5', self.l3.start)

        self.l4 = level4.Level4()
        self.accept('6', self.l4.start)

        #ENDGAME SCREEN WITH REPORT
        self.end = endgame.Endgame()
        self.accept('7', self.end.start)


Game = Tijuana2033()
Game.run()
