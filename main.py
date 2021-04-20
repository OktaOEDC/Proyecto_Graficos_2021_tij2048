import time
import logging

from direct.gui.DirectButton import DirectButton
from direct.gui.DirectEntry import DirectEntry
from direct.gui.DirectGuiGlobals import WITHIN
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.ShowBase import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task, TaskManagerGlobal
from direct.task.TaskManagerGlobal import taskMgr
#from direct import *
from panda3d.core import (Fog, NodePath, PointLight, TextFont, TextNode, Vec3,
                          WindowProperties, loadPrcFile)

import player

loadPrcFile("config/conf.prc")


text_titles_titles = ["INJUSTICIA", "INDIVIDUO",
                      "BUSQUEDA DE JUSTICIA", "FALLA DE SISTEMA"]

taskAccumulator = 0


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


class Tijuana2033(ShowBase):
    def __init__(self):
        super().__init__()
        self.playerName = ""
        self.IsFullScreen = False
        self.blade_runner = player.Player(self.playerName)
        self.disableMouse()
        ##
        self.plight = PointLight("plight")
        self.plight.setColor((1, 1, 1, 1))
        self.plnp = self.render.attachNewNode(self.plight)
        # self.plight.setAttenuation((1,0,1))
        ##self.plnp.setPos(0.33, 6,4)
        self.render.setLight(self.plnp)
        # self.Main_menu()

        taskMgr.add(self.Main_menu, 'first', sort=1, uponDeath=cleanUp)
        taskMgr.add(self.transition, 'trans', sort=2, uponDeath=cleanUp)

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
        # Remover el menu principal
        self.render.clearLight()
        self.plnp.removeNode()
        self.fondo.removeNode()
        self.fullScreenShape.removeNode()
        self.TextInsertName.removeNode()
        self.TextInsertNameInput.removeNode()
        self.ButtonInsertName.removeNode()
        self.InvisibleButton.removeNode()
        self.TextFullScreen.removeNode()
        ###

    def level1(self, task):
        self.Nivel1 = self.loader.loadModel("models/Campestre_light.bam")
        self.Nivel1.reparentTo(self.render)
        self.Nivel1.setScale(1, 1, 1)
        self.Nivel1.setPos(0.33, 6, -1)
        self.camera.setPos(-0.66, 2.5, 0.55)
        # self.camera.setPos(0.33,6,5)
        self.camera.lookAt(self.Nivel1)
        self.background = OnscreenImage(
            parent=render2dp, image="textures/Skunight.png")  # Load an image object
        base.cam2dp.node().getDisplayRegion(0).setSort(-20)
        color = (0.8, 0.8, 0.8)
        linfog = Fog("Scene-wide exponential Fog object")
        linfog.setColor(*color)
        linfog.setLinearRange(0, 25)
        linfog.setLinearFallback(45, 160, 320)
        render.setFog(linfog)
        base.setBackgroundColor(*color)
        self.plight_lv1 = PointLight("plight")
        self.plight_lv1.setColor((1, 1, 1, 1))
        self.plnp_lv1 = self.render.attachNewNode(self.plight_lv1)
        self.plight_lv1.setAttenuation((1, 0, 1))
        self.plnp_lv1.setPos(0.33, 6, 4)
        self.render.setLight(self.plnp_lv1)

    def transition(self, task):
        textposx = 0
        textposy = -0.5
        self.scene = self.loader.loadModel("models/fondo_menu.bam")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(1, 1, 1)
        self.scene.setPos(0, 25, 0)
        # TITLE TEXT PART...
        if len(self.blade_runner.name) < 1:
            task.time = 0
            return Task.again
        if task.time !=0:
            self.textObject = OnscreenText(text="NIVEL 1", pos=(textposx, textposy), scale=0.1,  fg=[
                240, 240, 240, 1], wordwrap=45, bg=[0, 0, 0, 0.1])
        return Task.done
        

        self.textObject.removeNode()
        return Task.done

    def remover(self, task):
        self.textObject.removeNode()
        return task.done

    def level1(self, task):
        self.Nivel1 = self.loader.loadModel("models/Campestre_light.bam")
        self.Nivel1.reparentTo(self.render)
        self.Nivel1.setScale(1, 1, 1)
        self.Nivel1.setPos(0.33, 6, -1)
        # We use a special trick of Panda3D: by default we have two 2D renderers: render2d and render2dp, the two being equivalent. We can then use render2d for front rendering (like modelName), and render2dp for background rendering.
        self.background = OnscreenImage(
            parent=render2dp, image="textures/Skunight.png")  # Load an image object
        # Force the rendering to render the background image first (so that it will be put to the bottom of the scene since other models will be necessarily drawn on top)
        base.cam2dp.node().getDisplayRegion(0).setSort(-20)
        return task.done

    def setFullScreen(self):
        props = WindowProperties()
        if(self.IsFullScreen == True):
            props.fullscreen = False
            self.IsFullScreen = False
        else:
            props.fullscreen = True
            self.IsFullScreen = True
        self.win.requestProperties(props)
        

    
    def Main_menu(self, task):
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
        return task.done


Game = Tijuana2033()
Game.run()
