
from direct.particles.ParticleEffect import ParticleEffect
from direct.showbase.ShowBase import *
from panda3d.core import *
from direct.gui.DirectGui import *
from direct.showbase.Loader import Loader
from direct.gui.OnscreenText import OnscreenText
from direct.task import Task
from direct.gui.OnscreenImage import OnscreenImage
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.gui.DirectButton import DirectButton
from direct.gui.DirectGuiGlobals import WITHIN
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *

class Level2:
    def __init__(self):
        base.cam2dp.node().getDisplayRegion(0).setSort(-20)
        self.runner_font = loader.loadFont('./fonts/runner/BLADRMF_.TTF')

    def start(self):
        # load
        self.level2 = loader.loadModel("./models/CECUT.bam")
        self.level2.reparentTo(render)
        self.level2.setScale(1, 1, 1)
        self.level2.setPos(0, 0, 0)

        # start
        camera.setPos(-2,2, 4)
        camera.lookAt(self.level2)

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
        

    def __del__(self):
        print('[*] Destructor called')

    def buttons(self):
        self.button1 = DirectButton(
            text=("OPTION 1"), 
            text_font=self.runner_font, 
            scale=0.1, 
            pos=(-1, -5, -0.75), 
            frameTexture=None,
            command=self.stop, 
            relief=DGG.FLAT)

        self.option2 = DirectButton(
            text=("Option 2"), 
            text_font=self.runner_font, 
            scale=0.1, 
            pos=(0, -5, -0.75), 
            frameTexture=None, 
            command=self.stop, 
            relief=DGG.FLAT)

        self.option3 = DirectButton(
            text=("Option 3"), 
            text_font=self.runner_font, 
            scale=0.1, 
            pos=(1, -5, -0.75), 
            frameTexture=None, 
            command=self.stop, 
            relief=DGG.FLAT)
        
        
    def onClick(self):
        print("[*] Click!")

    def stop(self):
        self.__del__()
