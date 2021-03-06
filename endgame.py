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
import player

class Endgame:
    def __init__(self):
        self.text_pointers = []
        self.keyboard = Controller()
        self.runner_font = loader.loadFont('./fonts/runner/BLADRMF_.TTF')
        self.title = 'TIJUANA 2033'
        self.p1 = player.Player()

    def start(self):
        self.ambientSound = loader.loadSfx('./audio/naive.ogg')
        self.ambientSound.setLoop(True)
        self.ambientSound.play()
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
        self.report()

    def stop(self):
        self.fondo.remove_node()
        self.alnp.remove_node()
        render.clearLight()
        self.end.remove_node()
        for text in self.text_pointers():
            text.remove_node()
        self.__del__()

    def __del__(self):
        print('[*] Destructor called')

    def report(self):
        self.p1.loadfile()
        reports = self.p1.get_phil()
        self.end = OnscreenText(font=self.runner_font, text='FIN DEL JUEGO', scale=0.2, pos=[
            0, 0], fg=[240, 0, 0, 1], shadow=[0.5, 0.5, 0.5, 0.5], shadowOffset=(0.04, 0.04))

        dropy = -0.5
        for text in reports:
            self.text = OnscreenText(font=self.runner_font, text=str(text), scale=0.1, pos=[
            0, dropy], fg=[240, 0, 0, 1], shadow=[0.5, 0.5, 0.5, 0.5], shadowOffset=(0.04, 0.04),wordwrap=20)
            self.text_pointers.append(self.text)
            dropy-=0.3
            