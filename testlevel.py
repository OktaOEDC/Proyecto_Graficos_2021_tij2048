
from direct.particles.ParticleEffect import ParticleEffect
from direct.showbase.ShowBase import *
from panda3d.core import *
from direct.showbase.Loader import Loader
from direct.gui.OnscreenText import OnscreenText
from direct.task import Task


class testCrawl:
    def __init__(self):

        self.fullScreenShape = loader.loadModel(
            "models/fullscreen_shape.bam")
        self.fullScreenShape.reparentTo(render)
        self.fullScreenShape.setScale(0.25, 0.25, 0.25)
        self.fullScreenShape.setPos(-1.5, 6, -1)
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
        self.ambientSound.play()
        self.fullScreenShape.show()
        self.crawl()
        if self.ambientSound.status()== AudioSound.PLAYING :
          self.stop()
          
    def stop(self):
        self.fullScreenShape.hide()
        render.clearLight()
        self.ambientSound.stop()


    def crawl(self):
        textposx = 0.0
        textposy = 0.5
        self.textdelay = 1
        for x in story:
            for y in x:
                self.print_task = taskMgr.do_method_later(self.textdelay,self.slow_crawl, name='slow_crawl', extraArgs=[y, textposx, textposy])
                self.textdelay += 2
                textposy -= 0.1
            textposy -= 0.05

    def slow_crawl(self,argtext, _posx, _posy):
        self.textObject = OnscreenText(text=argtext, pos=(_posx, _posy), scale=0.05,  fg=[
            240, 240, 240, 1], wordwrap=45, bg=[0, 0, 0, 0.1])
        print('SLOW CRAWL')


story = [
        ["TIJUANA 2033", "Las Pulgas es fumigada.", "Quien fumiga al fumigador?",
            "WE LIVE IN A SOCIETY", "Where honor is a distant memory"],
        ["Xolos International compro la presa de Tijuana en 2023"],
        ["Tijuana cedio a ser una democracia directa en 2025"],
        ["Dubai y China compraron McDonalds en 2026 debido al colapso espcultativo del mercado de gallos en Asia."],
        ["En 2024 los Estados Unidos prohibio en su enteridad la produccion de carnes a base de animales.",
            "El SOYBOI PARTY ha remplazado al partido libertariano como la astilla de circulo politico en Washington "],
        ["Mandato numero 1984 permite el uso continuo en espacios publicos de mascaras de cobertura completa tras la pandemia de 2022 de covid-21"]]
