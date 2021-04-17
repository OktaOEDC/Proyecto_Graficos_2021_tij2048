from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile
loadPrcFile("config/conf.prc")


class test1(ShowBase):

    def __init__(self):
        super().__init__()
        print(self.render)
        text = TextNode('node name')
        text.setText("Every day in every way I'm getting better and better.")
        textNodePath = aspect2d.attachNewNode(text)
        textNodePath.setScale(0.07)


jueguito = test1()
jueguito.run()
