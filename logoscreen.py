from pynput.keyboard import Key, Controller
from direct.particles.ParticleEffect import ParticleEffect
from direct.showbase.ShowBase import *
from panda3d.core import *
from direct.showbase.Loader import Loader
from direct.gui.OnscreenText import OnscreenText
from direct.task import Task
from direct.gui.DirectButton import DirectButton
from direct.gui.DirectGuiGlobals import WITHIN
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
import yaml


class Logoscreen:
    def __init__(self):
        self.text_pointers = []
        self.keyboard = Controller()
        self.runner_font = loader.loadFont('./fonts/runner/BLADRMF_.TTF')
        self.title = 'TIJUANA 2033'
        self.fondo = loader.loadModel("./models/fondo_menu.bam")
        self.fondo.reparentTo(render)
        self.fondo.setScale(0.6, 0.6, 0.6)
        self.fondo.setPos(0, 10, 0)
        ambientLight = AmbientLight("ambient_light")
        ambientLight.setColor((0.2, 0.2, 0.2, 1))
        self.alnp = render.attachNewNode(ambientLight)
        sunLens = PerspectiveLens()
        sunLens.setFilmSize(50)
        sun = DirectionalLight("sun")
        sun.setColor((1, 1, 1, 1))
        sun.setShadowCaster(True, 2048, 2048)
        sun.setScene(render)
        self.InvisibleButton = DirectButton(
            text=("Click to continue"), text_font=self.runner_font, scale=0.2, pos=(-0, -20, -0.3), frameTexture=None, command=self.stop, relief=DGG.FLAT)
        self.InvisibleButton.setTransparency(True)

    def __del__(self):
        print('Destructor called')

    def start(self):
        self.ambientSound = loader.loadSfx('./audio/naive.ogg')
        self.ambientSound.setLoop(True)
        self.ambientSound.play()
        self.fondo.show()
        self.text()
        self.InvisibleButton.show()

    def stop(self):
        NodePath.remove_node(self.putchar)
        NodePath.remove_node(self.fondo)
        render.clearLight()
        self.ambientSound.stop()
        self.InvisibleButton.removeNode()
        for letter in self.text_pointers:
            letter.removeNode()
        self.keyboard.press('1' )
        self.keyboard.release('1' )
        self.__del__()

    def text(self):
        posx = -1
        posy = 0.0
        delay = 0.1
        for char in self.title:
            taskMgr.doMethodLater(delay, self.temporal_print, 'printtitle', extraArgs=[
                                  0.2, char, posx, posy])
            delay += 0.1
            posx += 0.2
            

    def temporal_print(self, _scale, char, _posx, _posy):
        self.putchar = OnscreenText(font=self.runner_font, text=char, scale=_scale, pos=[
                                    _posx, _posy], fg=[240, 0, 0, 1], shadow=[0.5, 0.5, 0.5, 0.5], shadowOffset=(0.04, 0.04))

        self.text_pointers.append(self.putchar)
        # print(self.putchar.getPos())


    def yamlplayer():
        pass