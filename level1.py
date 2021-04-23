
from direct.particles.ParticleEffect import ParticleEffect
from direct.showbase.ShowBase import *
from panda3d.core import *
from direct.showbase.Loader import Loader
from direct.gui.OnscreenText import OnscreenText
from direct.task import Task
from direct.gui.OnscreenImage import OnscreenImage



class Level1:
    def __init__(self,baseClass):
        baseClass.Nivel1 = loader.loadModel("models/Campestre_light.bam")
        baseClass.Nivel1.reparentTo(render)
        baseClass.Nivel1.setScale(1, 1, 1)
        baseClass.Nivel1.setPos(0.33, 6, -1)
        #camera = camera.setPos(-0.66, 2.5, 0.55)
        #camera.lookAt(self.Nivel1)
        baseClass.background = OnscreenImage(
            parent=render2dp, image="textures/Skunight.png")  # Load an image object

    def start(self,baseClass):
        base.cam2dp.node().getDisplayRegion(0).setSort(-20)
        color = (0.8, 0.8, 0.8)
        linfog = Fog("Scene-wide exponential Fog object")
        linfog.setColor(*color)
        linfog.setLinearRange(0, 25)
        linfog.setLinearFallback(45, 160, 320)
        render.setFog(linfog)
        base.setBackgroundColor(*color)
        baseClass.plight_lv1 = PointLight("plight")
        baseClass.plight_lv1.setColor((1, 1, 1, 1))
        baseClass.plnp_lv1 = baseClass.render.attachNewNode(baseClass.plight_lv1)
        baseClass.plight_lv1.setAttenuation((1, 0, 1))
        baseClass.plnp_lv1.setPos(0.33, 6, 4)
        baseClass.render.setLight(baseClass.plnp_lv1)



    def stop(self):
        self.Nivel1.hide()
        #self.camera.hide()
        self.background.hide()
        


