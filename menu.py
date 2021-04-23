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


class Menu:
    def __init__(self):
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
    
    def start(self):
        pass
    
    def stop(self):
        self.fullScreenShape.hide()
        self.fondo.hide()
        self.TextInsertName.hide()
        self.TextFullScreen.hide()
        self.ButtonInsertName.hide()
        self.InvisibleButton.hide()
        self.TextInsertNameInput.hide()
    
        # self.render.clearLight()
        # self.plnp.removeNode()
        # self.fondo.removeNode()
        # self.fullScreenShape.removeNode()
        # self.TextInsertName.removeNode()
        # self.TextInsertNameInput.removeNode()
        # self.ButtonInsertName.removeNode()
        # self.InvisibleButton.removeNode()
        # self.TextFullScreen.removeNode()