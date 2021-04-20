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
import player

text_titles_titles = ["INJUSTICIA", "INDIVIDUO",
                      "BUSQUEDA DE JUSTICIA", "FALLA DE SISTEMA"]


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
        self.blade_runner = player.Player(self.playerName) 
        print('Hola',self.blade_runner.get_name(),'bienvenido a TIJUANA 2033')
        ##Remover el menu principal
        self.fondo.removeNode()
        self.fullScreenShape.removeNode() 
        self.TextInsertName.removeNode()
        self.TextInsertNameInput.removeNode()
        self.ButtonInsertName.removeNode()
        self.InvisibleButton.removeNode()
        self.TextFullScreen.removeNode()
        ##Transicionar al primer nivel
        
        ###
        self.Nivel1 = self.loader.loadModel("models/Campestre_light.bam")
        self.Nivel1.reparentTo(self.render)
        self.Nivel1.setScale(1, 1, 1)
        self.Nivel1.setPos(-1.5, 6,-1 )

    def transition(self, title):
        self.scene = self.loader.loadModel("models/fondo_menu.bam")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(1, 1, 1)
        self.scene.setPos(0, 25, 0)
    
        #TITLE TEXT PART...
        self.textObject = OnscreenText(text=y, pos=(textposx,textposy),scale=0.05,  fg=[240,240,240,1], wordwrap=45, bg=[0,0,0,0.1])
        return task.done
    
    def loading():
        self.light_model = self.loader.loadModel('models/misc/sphere')
        self.light_model.setScale(0.1, 0.1, 0.1)
        self.light_model.reparentTo(self.render)
        
            
    
                  
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
        self.TextInsertName = OnscreenText(font=font, text='Ingrese su nombre:', pos=(-0.5, 0.02), scale=0.07, fg=(143/255,250/255,2/255,1))
        self.TextFullScreen = OnscreenText(font=font, text='Fulscreen:', pos=(-0.99, -0.67), scale=0.04, fg=(143/255,250/255,2/255,1))
        self.TextInsertNameInput = DirectEntry(text = "", scale=.05, numLines = 1, focus=1)
        self.ButtonInsertName = DirectButton(text=("Insertar nombre"), scale=.05, pos=(0.25,0,-0.10),command=self.getPlayerName)
        self.InvisibleButton = DirectButton(text=("*"), scale=.05, pos=(-1, 5,-0.73),command=self.setFullScreen)
        self.InvisibleButton.bind(WITHIN, command = self.mouseOver)

Game = Tijuana2033()
Game.run()