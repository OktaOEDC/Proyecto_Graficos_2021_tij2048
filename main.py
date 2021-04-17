from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectEntry import DirectEntry
from direct.gui.DirectButton import DirectButton
from panda3d.core import loadPrcFile
from panda3d.core import WindowProperties
from panda3d.core import TextNode
from panda3d.core import Vec3
from panda3d.core import TextFont
from panda3d.core import PointLight
from direct.gui.DirectGuiGlobals import WITHIN
loadPrcFile("config/conf.prc")

class Tijuana2033(ShowBase):
    def __init__(self):
        super().__init__()  
        self.playerName= "Player_1"
        self.Main_menu()
        self.IsFullScreen = False
        self.disableMouse()
        ##
        self.light_model = self.loader.loadModel('models/misc/sphere')
        self.light_model.setScale(0.1, 0.1, 0.1)
        self.light_model.reparentTo(self.render)
        ##
        plight = PointLight("plight")
        plight.setColor((1,1,1,1))
        self.plnp = self.render.attachNewNode(plight)
        self.render.setLight(self.plnp)

    def mouseOver(self, argumento): 
        rotation_interval = self.fullScreenShape.hprInterval(10,Vec3(360,0,0))
        rotation_interval.start()

    def getPlayerName(self):
        self.playerName = self.TextInsertNameInput.get()
        print("Hola " + str(self.playerName))

    def setFullScreen(self):
        props = WindowProperties()
        if(self.IsFullScreen == True):
            props.fullscreen = False
            self.IsFullScreen = False
        else:
            props.fullscreen = True
            self.IsFullScreen = True
        self.win.requestProperties(props)

    def Main_menu(self):
        self.fullScreenShape = self.loader.loadModel("models/fullscreen_shape.bam")
        self.fullScreenShape.reparentTo(self.render)
        self.fullScreenShape.setScale(0.25, 0.25, 0.25)
        self.fullScreenShape.setPos(-1.5, 6,-1 )
        self.fondo = self.loader.loadModel("models/fondo_menu.bam")
        self.fondo.reparentTo(self.render)
        self.fondo.setScale(0.27,0.01,0.32)
        self.fondo.setPos(0, 7, 0)
        font = loader.loadFont('./fonts/comic/comic.ttf')
        TextInsertName = OnscreenText(font=font, text='Ingrese su nombre:', pos=(-0.5, 0.02), scale=0.07, fg=(143/255,250/255,2/255,1))
        TextFullScreen = OnscreenText(font=font, text='Fulscreen:', pos=(-0.99, -0.67), scale=0.04, fg=(143/255,250/255,2/255,1))
        self.TextInsertNameInput = DirectEntry(text = "", scale=.05, numLines = 1, focus=1)
        ButtonInsertName = DirectButton(text=("Insertar nombre"), scale=.05, pos=(0.25,0,-0.10),command=self.getPlayerName)
        self.InvisibleButton = DirectButton(text=("*"), scale=.05, pos=(-1, 5,-0.73),command=self.setFullScreen)
        self.InvisibleButton.bind(WITHIN, command = self.mouseOver)

Game = Tijuana2033()
Game.run()