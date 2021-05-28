from direct.fsm.FSM import FSM
from direct.gui.DirectButton import DirectButton
from direct.gui.DirectEntry import DirectEntry
from direct.gui.DirectGui import DGG
from direct.gui.DirectGuiGlobals import WITHIN
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.OnscreenText import OnscreenText
from direct.showbase import DirectObject
from direct.showbase.Loader import Loader
from direct.showbase.ShowBase import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task, TaskManagerGlobal
from direct.task.TaskManagerGlobal import taskMgr
from panda3d.core import *
from pynput.keyboard import Controller, Key

import crawl
import level1
import logoscreen
import player
import textcrawl


class Menu:
    def __init__(self, otherProperties, baseClass):
        self.text_pointers = []
        self.keyboard = Controller()
        self.IsFullScreen = False
        self.others = otherProperties
        self.baseClass = baseClass

    def __del__(self):
        print('Destructor called')

    def start(self):

        self.fullScreenShape = loader.loadModel(
            "models/fullscreen_shape.bam")
        self.fullScreenShape.reparentTo(render)
        self.fullScreenShape.setScale(0.25, 0.25, 0.25)
        self.fullScreenShape.setPos(-1.5, 6, -1)
        self.fondo = loader.loadModel("models/fondo_menu.bam")
        self.fondo.reparentTo(render)
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
            0.25, 0, -0.10), command=self.make_player)
        self.InvisibleButton = DirectButton(
            text=("*"), scale=.05, pos=(-1, 5, -0.73), command=self.setFullScreen)
        self.InvisibleButton.bind(WITHIN, command=self.mouseOver)
        self.fullScreenShape.reparentTo(render)
        self.fondo.reparentTo(render)
        self.TextInsertNameInput.show()
        self.fullScreenShape.show()
        self.fondo.show()
        self.TextInsertName.show()
        self.TextFullScreen.show()
        self.ButtonInsertName.show()
        self.InvisibleButton.show()

    def stop(self):
        self.fullScreenShape.hide()
        self.fondo.remove_node()
        self.TextInsertName.hide()
        self.TextFullScreen.hide()
        self.ButtonInsertName.hide()
        self.InvisibleButton.hide()
        self.TextInsertNameInput.hide()
        self.keyboard.press('3')
        self.keyboard.release('3')
        self.__del__()

    def mouseOver(self, argumento):
        rotation_interval = self.fullScreenShape.hprInterval(
            10, Vec3(360, 0, 0))
        rotation_interval.start()

    def setFullScreen(self):
        props = self.others
        if(self.IsFullScreen == True):
            props.fullscreen = False
            self.IsFullScreen = False
        else:
            props.fullscreen = True
            self.IsFullScreen = True
        self.baseClass.win.requestProperties(props)

    def make_player(self):
        self.player = player.Player(self.TextInsertNameInput.get())
        self.player.savefile()
        self.stop()
