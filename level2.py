import yaml
from direct.gui.DirectButton import DirectButton
from direct.gui.DirectGui import *
from direct.gui.DirectGuiGlobals import WITHIN
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.OnscreenText import OnscreenText
from direct.particles.ParticleEffect import ParticleEffect
from direct.showbase.Loader import Loader
from direct.showbase.ShowBase import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import *
from pynput.keyboard import Controller, Key

import player


class Level2:
    def __init__(self):
        self.text_pointers = []
        self.keyboard = Controller()
        
        base.cam2dp.node().getDisplayRegion(0).setSort(-20)
        self.runner_font = loader.loadFont('./fonts/runner/BLADRMF_.TTF')
        self.p1 = player.Player()

    def start(self):
        # load
        self.level2 = loader.loadModel("models/CECUT.bam")
        self.level2.reparentTo(render)
        self.level2.setScale(1, 1, 1)
        self.level2.setPos(0, 0, 0)

        # start
        camera.setPos(0, 0, 0)
        camera.lookAt(self.level2)

        # start
        self.background = OnscreenImage(
            parent=render2dp, image="textures/Skunight.png")  # Load an image object

        color = (0.8, 0.8, 0.8)
        #self.linfog = Fog("Scene-wide exponential Fog object")
        #self.linfog.setColor(*color)
        #self.linfog.setLinearRange(0, 35)
        #self.linfog.setLinearFallback(45, 160, 320)
        #render.setFog(self.linfog)
        base.setBackgroundColor(*color)
        self.plight = PointLight("plight")
        self.plight.setColor((1, 1, 1, 1))
        self.plight.setAttenuation((1, 0, 1))

        self.buttons()
        self.text = OnscreenText(font=self.runner_font, text='Que concierto deseas que se presente en el sotano de las ruinas del CECUT?', scale=0.09, pos=[
            0, 0.5], fg=[240, 10, 10, 1], shadow=[0.5, 0.5, 0.5, 0.5], shadowOffset=(0.04, 0.04),wordwrap=20)
        
    def __del__(self):
        print('[*] Destructor called')

    def buttons(self):
        self.option1 = DirectButton(
            text=("Good Bunny"),
            text_font=self.runner_font,
            scale=0.1,
            pos=(-0, -5, -0.75),
            frameTexture=None,
            command=self.onClick1,
            relief=DGG.FLAT)

        self.option2 = DirectButton(
            text=("Los Demonios de Ecatepan"),
            text_font=self.runner_font,
            scale=0.1,
            pos=(0, -5, -0.55),
            frameTexture=None,
            command=self.onClick2,
            relief=DGG.FLAT)

        self.option3 = DirectButton(
            text=("La filarmonica de Ensenada"),
            text_font=self.runner_font,
            scale=0.1,
            pos=(0, -5, -0.35),
            frameTexture=None,
            command=self.onClick3,
            relief=DGG.FLAT)

    def onClick1(self):
        print("[*] Click!")
        self.p1.change_pol(1)
        self.p1.change_edu(1)
        self.p1.change_pop(1)
        self.stop()

    def onClick2(self):
        print("[*] Click!")
        self.p1.change_pol(1)
        self.p1.change_edu(2)
        self.p1.change_pop(3)
        self.stop()

    def onClick3(self):
        print("[*] Click!")
        self.p1.change_pol(0)
        self.p1.change_edu(5)
        self.p1.change_pop(9)
        self.stop()

    def stop(self):
        self.p1.savefile()
        self.text.remove_node()
        self.option1.remove_node()
        self.option2.remove_node()
        self.option3.remove_node()
        self.background.remove_node()
        self.level2.remove_node()
        render.clearLight()
        self.keyboard.press('5' )
        self.keyboard.release('5' )
        self.__del__()
