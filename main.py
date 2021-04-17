from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectEntry import DirectEntry
from direct.gui.DirectButton import DirectButton
from panda3d.core import loadPrcFile
from panda3d.core import WindowProperties
from panda3d.core import TextNode
from panda3d.core import TextFont
loadPrcFile("config/conf.prc")

class test1(ShowBase):
    def __init__(self):
        super().__init__()  
        self.playerName= "Player_1"
        self.Main_menu()

    def getPlayerName(self):
        self.playerName = self.TextInsertNameInput.get()
        print(" hola " + str(self.playerName))
        # props = WindowProperties()
        # props.fullscreen = True
        # self.win.requestProperties(props)

    def Main_menu(self):
        self.disableMouse
        imageObject = OnscreenImage(image='backgrounds/90sbg.jpg', pos=(0, 0, 0), scale=(1.78,1,1))
        font = loader.loadFont('./fonts/comic/comic.ttf')
        TextInsertName = OnscreenText(font=font, text='Ingrese su nombre:', pos=(-0.5, 0.02), scale=0.07, fg=(143/255,250/255,2/255,1))
        self.TextInsertNameInput = DirectEntry(text = "", scale=.05, numLines = 1, focus=1)
        ButtonInsertName = DirectButton(text=("Insertar nombre"), scale=.05, pos=(0.25,0,-0.10),command=self.getPlayerName)


jueguito = test1()
jueguito.run()
