import logging
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
from panda3d.core import *
from direct.showbase.Loader import Loader
import player
import textcrawl
import testlevel
import logoscreen
import level1
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


def cleanUp(task):
    global taskAccumulator
    print("Task func has accumulated %d" % taskAccumulator)
    # Reset the accumulator
    taskAccumulator = 0

    # A task that runs forever


def taskFunc(task):
    global taskAccumulator
    taskAccumulator += 1
    return task.cont


def taskStop(task):
    taskMgr.remove('Accumulator')


class Tijuana2033(ShowBase, FSM):
    def __init__(self):
        ShowBase.__init__(self)
        FSM.__init__(self, "FSM-Game")
        # self.win
        render.setShaderAuto()
        self.render.setAntialias(AntialiasAttrib.MAuto)
        self.playerName = ""
        self.IsFullScreen = False
        self.blade_runner = player.Player(self.playerName)
        self.disableMouse()
        ##
        self.plight = PointLight("plight")
        self.plight.setColor((1, 1, 1, 1))
        self.plnp = self.render.attachNewNode(self.plight)
        self.render.setLight(self.plnp)
        # get the displays width and height for later usage
        # self.dispWidth = self.pipe.getDisplayWidth()
        # props = WindowProperties()
        # self.dispHeight = self.pipe.getDisplayHeight()
        # props.setSize(self.dispWidth, self.dispHeight)
        # base.win.requestProperties(props)
        # ESTA ES LA SECUENCIA DE LO QUE QUIERO HACER, PERO NO SE COMO HACER QUE OCURRAN UNA DE OTRA DE FORMA TEMPORAZIDA O CONDICIONAL SIN BOTONES

        self.intro = logoscreen.Logoscreen()
        self.intro.start()
        self.accept('enter', self.intro.stop)

        self.crawl = testlevel.testCrawl()
        self.accept('enter', self.crawl.start)

        self.accept('enter', self.Main_menu)

        self.l1 = level1.Level1()
        #self.accept('enter',self.l1.start)
        
        # self.l1.stop()
        # self.accept('enter',self.l1.start)

        # self.accept('enter',self.crawl.stop)

        # taskMgr.add(self.crawl,uponDeath=cleanUp)
        #taskMgr.add(self.Main_menu, 'first', sort=1, uponDeath=cleanUp)
        #taskMgr.add(self.transition, 'trans', sort=2, uponDeath=cleanUp)
        #taskMgr.add(self.level1, 'level1', sort=2, uponDeath=cleanUp)

    def mouseOver(self, argumento):
        rotation_interval = self.fullScreenShape.hprInterval(
            10, Vec3(360, 0, 0))
        rotation_interval.start()

    def getPlayerName(self):
        self.playerName = self.TextInsertNameInput.get()
        self.blade_runner = player.Player(self.playerName)
        print('Hola', self.blade_runner.get_name(), 'bienvenido a TIJUANA 2033')
        # Remover el menu principal
        self.blade_runner = player.Player(self.playerName)
        print('Hola', self.blade_runner.get_name(), 'bienvenido a TIJUANA 2033')
 
    def setFullScreen(self):
        # props = WindowProperties()
        # if(self.IsFullScreen == True):
        #      props.fullscreen = False
        #      self.IsFullScreen = False
        #  else:
        #      props.fullscreen = True
        #      self.IsFullScreen = True
        #  self.win.requestProperties(props)
        pass

    def Main_menu(self):
        self.fullScreenShape = self.loader.loadModel(
            "models/fullscreen_shape.bam")
        self.fullScreenShape.reparentTo(self.render)
        self.fullScreenShape.setScale(0.25, 0.25, 0.25)
        self.fullScreenShape.setPos(-1.5, 6, -1)
        self.fondo = self.loader.loadModel("models/fondo_menu.bam")
        self.fondo.reparentTo(self.render)
        self.fondo.setScale(0.27, 0.01, 0.32)
        self.fondo.setPos(0, 7, 0)
        font = loader.loadFont('./fonts/comic/comic.ttf')
        self.TextInsertName = OnscreenText(font=font, text='Ingrese su nombre:', pos=(
            -0.5, 0.02), scale=0.07, fg=(143/255, 250/255, 2/255, 1))
        self.TextFullScreen = OnscreenText(
            font=font, text='Fulscreen:', pos=(-0.99, -0.67), scale=0.04, fg=(143/255, 250/255, 2/255, 1))
        self.TextInsertNameInput = DirectEntry(
            text="", scale=.05, numLines=1, focus=1)
        self.ButtonInsertName = DirectButton(text=("Insertar nombre"), scale=.05, pos=(
            0.25, 0, -0.10), command=self.getPlayerName)
        self.InvisibleButton = DirectButton(
            text=("*"), scale=.05, pos=(-1, 5, -0.73), command=self.setFullScreen)
        self.InvisibleButton.bind(WITHIN, command=self.mouseOver)




Game = Tijuana2033()
Game.run()
