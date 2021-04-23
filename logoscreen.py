
from direct.particles.ParticleEffect import ParticleEffect
from direct.showbase.ShowBase import *
from panda3d.core import *
from direct.showbase.Loader import Loader
from direct.gui.OnscreenText import OnscreenText
from direct.task import Task


class Logoscreen:
    def __init__(self):
        self.runner_font = loader.loadFont('./fonts/runner/BLADRMF_.TTF')
        self.title = 'TIJUANA 2033'
        self.fondo = loader.loadModel("./models/fondo_menu.bam")
        self.fondo.reparentTo(render)
        self.fondo.setScale(0.5, 0.5, 0.5)
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

    def start(self):
        self.ambientSound = loader.loadSfx('./audio/naive.ogg')
        self.ambientSound.setLoop(True)
        self.ambientSound.play()
        self.fondo.show()
        self.text()
<<<<<<< HEAD

=======
        # if self.ambientSound.status() == AudioSound.PLAYING:
        #     self.stop()
>>>>>>> e726e82741dd7a5ebbd77ccd46d37c1fc4736001

    def stop(self):
        self.fondo.hide()
        render.clearLight()
        self.ambientSound.stop()

    def text(self):
        posx = -1
        posy = 0.0
        delay = 0.3
        for char in self.title:
            taskMgr.doMethodLater(delay, self.temporal_print, 'printtitle', extraArgs=[
                                  0.2, char, posx, posy])
            delay += 0.1
            posx += 0.2
            """self.putchar = OnscreenText(font=runner_font, text=char,scale=0.2, pos=[posx,posy],fg=[240, 240, 240, 1])
            posx+=0.22"""
        taskMgr.do_method_later(delay+2, self.temporal_print, 'pressenter',
                                extraArgs=[0.05, 'Press enter to continue', 0, -0.2])

    def temporal_print(self, _scale, char, _posx, _posy):

        self.putchar = OnscreenText(font=self.runner_font, text=char, scale=_scale, pos=[
                                    _posx, _posy], fg=[240, 0, 0, 1], shadow=[0.5, 0.5, 0.5, 0.5], shadowOffset=(0.04, 0.04))
