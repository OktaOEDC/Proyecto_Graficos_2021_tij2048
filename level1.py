
from direct.particles.ParticleEffect import ParticleEffect
from direct.showbase.ShowBase import *
from panda3d.core import *
from direct.showbase.Loader import Loader
from direct.gui.OnscreenText import OnscreenText
from direct.task import Task
from direct.gui.OnscreenImage import OnscreenImage



class Level1:
    def __init__(self):
        self.Nivel1 = loader.loadModel("models/Campestre_light.bam")
        self.Nivel1.reparentTo(render)
        self.Nivel1.setScale(1, 1, 1)
        self.Nivel1.setPos(0.33, 6, -1)
        #camera = camera.setPos(-0.66, 2.5, 0.55)
        #camera.lookAt(self.Nivel1)
        self.background = OnscreenImage(
            parent=render2dp, image="textures/Skunight.png")  # Load an image object

    def start(self):
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



    def stop(self):
        self.Nivel1.hide()
        #self.camera.hide()
        self.background.hide()
        


