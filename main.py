from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectEntry import DirectEntry
from direct.gui.DirectButton import DirectButton
from panda3d.core import loadPrcFile
from panda3d.core import MouseWatcher
from panda3d.core import DisplayRegion
from panda3d.core import WindowProperties
from panda3d.core import TextNode
from panda3d.core import Vec3
from panda3d.core import TextFont
from direct.gui.DirectGuiGlobals import WITHIN
loadPrcFile("config/conf.prc")

class test1(ShowBase):
    def __init__(self):
        super().__init__()  
        self.playerName= "Player_1"
        self.Main_menu()
        self.IsFullScreen = False
        self.disableMouse()
        ##

    def mouseOver(self, argumento):
        ##self.scene.setHpr(120,230,30)  
        rotation_interval = self.scene.hprInterval(10,Vec3(360,0,0))
        rotation_interval.start()
        pass

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
        pass

    def Main_menu(self):
        self.scene = self.loader.loadModel("models/Espejo_fullscreen.bam")
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-1.5, 6,-1)
        ##Todo hacer prisma para modelo
        ##imageObject = OnscreenImage(image='backgrounds/90sbg.jpg', pos=(0, 0, 0), scale=(1.78,1,1))
        font = loader.loadFont('./fonts/comic/comic.ttf')
        TextInsertName = OnscreenText(font=font, text='Ingrese su nombre:', pos=(-0.5, 0.02), scale=0.07, fg=(143/255,250/255,2/255,1))
        TextFullScreen = OnscreenText(font=font, text='Fulscreen:', pos=(-0.99, -0.67), scale=0.04, fg=(143/255,250/255,2/255,1))
        self.TextInsertNameInput = DirectEntry(text = "", scale=.05, numLines = 1, focus=1)
        ButtonInsertName = DirectButton(text=("Insertar nombre"), scale=.05, pos=(0.25,0,-0.10),command=self.getPlayerName)
        self.InvisibleButton = DirectButton(text=("*"), scale=.05, pos=(-1, 5,-0.73),command=self.setFullScreen)
        self.InvisibleButton.bind(WITHIN, command = self.mouseOver)

jueguito = test1()
jueguito.run()
