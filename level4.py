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


class Level4:
    def __init__(self):
        self.text_pointers = []
        self.keyboard = Controller()
        
        base.cam2dp.node().getDisplayRegion(0).setSort(-20)
        self.runner_font = loader.loadFont('./fonts/runner/BLADRMF_.TTF')
        self.p1 = player.Player()

    def start(self):
        # load
        self.level4 = loader.loadModel("models/Picacho_diablo_11_068m.bam")
        self.level4.reparentTo(render)
        self.level4.setScale(1, 1, 1)
        self.level4.setPos(0, 0, 0)

        # start
        camera.setPos(-2, 2, 4)
        camera.lookAt(self.level4)

        # start
        self.background = OnscreenImage(
            parent=render2dp, image="textures/Skunight.png")  # Load an image object

        color = (0.8, 0.8, 0.8)
        self.linfog = Fog("Scene-wide exponential Fog object")
        self.linfog.setColor(*color)
        self.linfog.setLinearRange(0, 35)
        self.linfog.setLinearFallback(45, 160, 320)
        render.setFog(self.linfog)
        base.setBackgroundColor(*color)
        self.plight = PointLight("plight")
        self.plight.setColor((1, 1, 1, 1))
        self.plight.setAttenuation((1, 0, 1))

        self.buttons()
        self.text = OnscreenText(font=self.runner_font, text='La comunidad sin hogares de Baja California se ha reubicado al PICACHO DEL DIABLO!', scale=0.09, pos=[
            0, 0.5], fg=[240, 10, 10, 1], shadow=[0.5, 0.5, 0.5, 0.5], shadowOffset=(0.04, 0.04),wordwrap=20)
    def __del__(self):
        print('[*] Destructor called')

    def buttons(self):
        self.option1 = DirectButton(
            text=("NUKE 'EM BOYS"),
            text_font=self.runner_font,
            scale=0.1,
            pos=(0, -5, -0.75),
            frameTexture=None,
            command=self.onClick1,
            relief=DGG.FLAT)

        self.option2 = DirectButton(
            text=("construir barda"),
            text_font=self.runner_font,
            scale=0.1,
            pos=(0, -5, -0.55),
            frameTexture=None,
            command=self.onClick2,
            relief=DGG.FLAT)

        self.option3 = DirectButton(
            text=("cortarles recursos e ignorar"),
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
        self.level4.remove_node()
        render.clearLight()
        self.keyboard.press('7' )
        self.keyboard.release('7' )
        self.__del__()
