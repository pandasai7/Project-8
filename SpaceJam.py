from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectGui import *
from panda3d.core import *
import math, sys, random
import SpaceJamClasses  
import DefensePaths
from pandac.PandaModules import *
from direct.gui.DirectGui import *


class MyApp(ShowBase):

    class ControlMenu(object):
        isMenuOpen = False

        txtscale = 0.05
        txtentrywidth = 5
        txtlabelcolor = (255, 255, 255, 255)
        menufilepath = './Assets/menu/menubg.png'
        menubgscale = (1, 0.75, 0.75)
        
        left_ctrl = 'a'
        right_ctrl = 'd'
        up_ctrl = 'w'
        down_ctrl = 's'

        left_ctrl_old = []
        right_ctrl_old = []
        up_ctrl_old = []
        down_ctrl_old = []


    class MainMenu(object):
        isMenuOpen = False

        txtscale = 0.05
        txtentrywidth = 5
        txtlabelcolor = (255, 255, 255, 255)
        menufilepath = './Assets/menu/menubg.png'
        menubgscale = (1, 0.75, 0.75)
        
        left_ctrl = 'a'
        right_ctrl = 'd'
        up_ctrl = 'w'
        down_ctrl = 's'

        left_ctrl_old = ''
        right_ctrl_old = ''
        up_ctrl_old = ''
        down_ctrl_old = ''

        left_entry = ''
        right_entry = ''
        up_entry = ''
        down_entry = ''


    def __init__(self):
        ShowBase.__init__(self)

        def SetControls(self):
            #Mouse Control
            base.disableMouse()
            base.camera.setPos(-10.0, -15.0, 0.0)
            base.camera.setHpr(0.0, 0.0, 0.0)

            
            #controls---------
            #menu
            #self.openSettingsMenu(MyApp.ControlMenu.isMenuOpen)
            self.openMainMenu(MyApp.MainMenu.isMenuOpen)
            
            #left
            self.accept(MyApp.ControlMenu.left_ctrl, self.negativeX, [1]) #LeftPressed
            self.accept(MyApp.ControlMenu.left_ctrl + '-up', self.negativeX, [0]) #LeftReleased

            #right
            self.accept(MyApp.ControlMenu.right_ctrl, self.positiveX, [1]) #RightPressed
            self.accept(MyApp.ControlMenu.right_ctrl + '-up', self.positiveX, [0]) #RightReleased

            #up
            self.accept(MyApp.ControlMenu.up_ctrl, self.positiveY, [1]) #RightPressed
            self.accept(MyApp.ControlMenu.up_ctrl + '-up', self.positiveY, [0]) #RightReleased

            #down
            self.accept(MyApp.ControlMenu.down_ctrl, self.negativeY, [1]) #RightPressed
            self.accept(MyApp.ControlMenu.down_ctrl + '-up', self.negativeY, [0]) #RightReleased

            #rollleft
            self.accept('q', self.barrelRollLeft, [1])
            self.accept('q' + '-up', self.barrelRollLeft, [0])
        

        

        SetupScene(self)
        SetCamera(self)
        #SetMovement(self)
        SetControls(self)
        
        self.openSettingsMenu(MyApp.ControlMenu.isMenuOpen)
        self.closeSettingsMenu()
        self.openMainMenu(MyApp.MainMenu.isMenuOpen)
        self.closeMainMenu()
        self.accept('escape', self.toggleMenu, [False])

    def negativeX(self, keyDown):
            if(keyDown):
                self.taskMgr.add(self.moveNegativeX, 'moveNegativeX')
            else:
                 self.taskMgr.remove('moveNegativeX')
    def positiveX(self, keyDown):
            if(keyDown):
                self.taskMgr.add(self.movePositiveX, 'movePositiveX')
            else:
                 self.taskMgr.remove('movePositiveX')
    def negativeY(self, keyDown):
            if(keyDown):
                self.taskMgr.add(self.moveNegativeY, 'moveNegativeY')
            else:
                 self.taskMgr.remove('moveNegativeY')
    def positiveY(self, keyDown):
            if(keyDown):
                self.taskMgr.add(self.movePositiveY, 'movePositiveY')
            else:
                 self.taskMgr.remove('movePositiveY')
    def barrelRollLeft(self, keyDown):
            if(keyDown):
                self.taskMgr.add(self.rollLeft, 'rollLeft')
            else:
                 self.taskMgr.remove('rollLeft')

    def quit(self):
        sys.exit()

    def moveNegativeX(self, task):
         self.Hero.setX((-100, 0, 0))
         return task.cont

    def movePositiveX(self, task):
        self.Hero.setX((100, 0, 0))
        return task.cont

    def moveNegativeY(self, task):
        self.Hero.setY((0, -100, 0))
        return task.cont

    def movePositiveY(self, task):
        self.Hero.setY((0, 100, 0))
        return task.cont
    
    def rollLeft(self, task):
        self.Hero.rotateLeft()
        return task.cont

    def toggleMenu(self, openOr):
        if(not openOr):
            self.openMainMenu(MyApp.MainMenu.isMenuOpen)
        else:
            self.closeMainMenu()
            self.closeSettingsMenu()

    def openSettingsMenu(self, openOr):
            if(not openOr):
                
                MyApp.ControlMenu.menubgimg = OnscreenImage(image = MyApp.ControlMenu.menufilepath, pos = (0, 0, 0.2), scale = MyApp.ControlMenu.menubgscale)
                MyApp.ControlMenu.up_label = OnscreenText(text = 'FORWARD CONTROL', pos = (-0.3, 0.1), scale = MyApp.ControlMenu.txtscale, fg = MyApp.ControlMenu.txtlabelcolor)            
                MyApp.ControlMenu.up_entry = DirectEntry(width=10, numLines = 1, scale = MyApp.ControlMenu.txtscale, relief = DGG.SUNKEN, cursorKeys = 1, frameSize = (0, 15, 0, 1), pos = (0.0, 0.0, 0.1))
                MyApp.ControlMenu.down_label = OnscreenText(text = 'DOWN CONTROL', pos = (-0.3, 0.2), scale = MyApp.ControlMenu.txtscale, fg = MyApp.ControlMenu.txtlabelcolor)            
                MyApp.ControlMenu.down_entry = DirectEntry(width=10, numLines = 1, scale = MyApp.ControlMenu.txtscale, relief = DGG.SUNKEN, cursorKeys = 1, frameSize = (0, 15, 0, 1), pos = (0.0, 0.0, 0.2))
                MyApp.ControlMenu.left_label = OnscreenText(text = 'LEFT CONTROL', pos = (-0.3, 0.3), scale = MyApp.ControlMenu.txtscale, fg = MyApp.ControlMenu.txtlabelcolor)            
                MyApp.ControlMenu.left_entry = DirectEntry(width=10, numLines = 1, scale = MyApp.ControlMenu.txtscale, relief = DGG.SUNKEN, cursorKeys = 1, frameSize = (0, 15, 0, 1), pos = (0.0, 0.0, 0.3))
                MyApp.ControlMenu.right_label = OnscreenText(text = 'RIGHT CONTROL', pos = (-0.3, 0.4), scale = MyApp.ControlMenu.txtscale, fg = MyApp.ControlMenu.txtlabelcolor)            
                MyApp.ControlMenu.right_entry = DirectEntry(width=10, numLines = 1, scale = MyApp.ControlMenu.txtscale, relief = DGG.SUNKEN, cursorKeys = 1, frameSize = (0, 15, 0, 1), pos = (0.0, 0.0, 0.4))

                def setText():
                    bk_text = "Button Clicked"
                    MyApp.ControlMenu.up_ctrl = MyApp.ControlMenu.up_entry.get()
                    MyApp.ControlMenu.down_ctrl = MyApp.ControlMenu.down_entry.get()
                    MyApp.ControlMenu.left_ctrl = MyApp.ControlMenu.left_entry.get()
                    MyApp.ControlMenu.right_ctrl = MyApp.ControlMenu.right_entry.get()

                    # Add button
                MyApp.ControlMenu.save_btn = DirectButton(text=("SAVE SETTINGS", "SAVED", "SAVE SETTINGS", "disabled"), scale=.05, command=setText)


                self.ControlMenu.isMenuOpen = True
            else:
             
                self.closeSettingsMenu()

                for i in MyApp.ControlMenu.left_ctrl_old:
                    self.ignore(i)

    def closeSettingsMenu(self):
        MyApp.ControlMenu.isMenuOpen = False
        if(MyApp.ControlMenu.left_entry.get() != ''): 
            MyApp.ControlMenu.left_ctrl_old.append(MyApp.ControlMenu.left_entry.get())
        if(MyApp.ControlMenu.right_entry.get() != ''):
            MyApp.ControlMenu.right_ctrl_old.append(MyApp.ControlMenu.right_entry.get())
        if(MyApp.ControlMenu.up_entry.get() != ''):
            MyApp.ControlMenu.up_ctrl_old.append(MyApp.ControlMenu.up_entry.get())
        if(MyApp.ControlMenu.down_entry.get() != ''):
            MyApp.ControlMenu.down_ctrl_old.append(MyApp.ControlMenu.down_entry.get())

        MyApp.ControlMenu.menubgimg.destroy()
        MyApp.ControlMenu.up_label.destroy()           
        MyApp.ControlMenu.up_entry.destroy()

        MyApp.ControlMenu.down_label.destroy()            
        MyApp.ControlMenu.down_entry.destroy()

        MyApp.ControlMenu.left_label.destroy()            
        MyApp.ControlMenu.left_entry.destroy()

        MyApp.ControlMenu.right_label.destroy()            
        MyApp.ControlMenu.right_entry.destroy()
        MyApp.ControlMenu.save_btn.destroy()

    def openMainMenu(self, openOr):
            if(not openOr):
                
                MyApp.MainMenu.menubgimg = OnscreenImage(image = MyApp.MainMenu.menufilepath, pos = (0, 0, 0.2), scale = MyApp.MainMenu.menubgscale)
                MyApp.MainMenu.up_label = OnscreenText(text = '', pos = (-0.3, 0.1), scale = MyApp.MainMenu.txtscale, fg = MyApp.MainMenu.txtlabelcolor)            
                MyApp.MainMenu.up_entry = DirectEntry(width=10, numLines = 1, scale = MyApp.MainMenu.txtscale, relief = DGG.SUNKEN, cursorKeys = 1, frameSize = (0, 15, 0, 1), pos = (0.0, 0.0, 0.1))
                MyApp.MainMenu.down_label = OnscreenText(text = '', pos = (-0.3, 0.2), scale = MyApp.MainMenu.txtscale, fg = MyApp.MainMenu.txtlabelcolor)            
                MyApp.MainMenu.down_entry = DirectEntry(width=10, numLines = 1, scale = MyApp.MainMenu.txtscale, relief = DGG.SUNKEN, cursorKeys = 1, frameSize = (0, 15, 0, 1), pos = (0.0, 0.0, 0.2))
                MyApp.MainMenu.left_label = OnscreenText(text = '', pos = (-0.3, 0.3), scale = MyApp.MainMenu.txtscale, fg = MyApp.MainMenu.txtlabelcolor)            
                MyApp.MainMenu.left_entry = DirectEntry(width=10, numLines = 1, scale = MyApp.MainMenu.txtscale, relief = DGG.SUNKEN, cursorKeys = 1, frameSize = (0, 15, 0, 1), pos = (0.0, 0.0, 0.3))
                MyApp.MainMenu.right_label = OnscreenText(text = '', pos = (-0.3, 0.4), scale = MyApp.MainMenu.txtscale, fg = MyApp.MainMenu.txtlabelcolor)            
                MyApp.MainMenu.right_entry = DirectEntry(width=10, numLines = 1, scale = MyApp.MainMenu.txtscale, relief = DGG.SUNKEN, cursorKeys = 1, frameSize = (0, 15, 0, 1), pos = (0.0, 0.0, 0.4))

                def closeMenu():
                    bk_text = "Button Clicked"
                    self.MainMenu.isMenuOpen = False
                        
                    MyApp.MainMenu.menubgimg.destroy()
                    MyApp.MainMenu.up_label.destroy()            
                    MyApp.MainMenu.up_entry.destroy()

                    MyApp.MainMenu.down_label.destroy()            
                    MyApp.MainMenu.down_entry.destroy()

                    MyApp.MainMenu.left_label.destroy()            
                    MyApp.MainMenu.left_entry.destroy()

                    MyApp.MainMenu.right_label.destroy()            
                    MyApp.MainMenu.right_entry.destroy()
                    MyApp.MainMenu.close_btn.destroy()
                    MyApp.MainMenu.settings_btn.destroy()


                    # Add button
                MyApp.MainMenu.close_btn = DirectButton(text=("CLOSE", "CLOSE", "CLOSE", "disabled"), scale=.05, command=closeMenu)
                MyApp.MainMenu.settings_btn = DirectButton(text=("CONTROLS", "CONTROLS", "CONTROLS", "disabled"), scale=.05, command=self.openSettingsMenu, extraArgs = [False])
                #MyApp.MainMenu.settings_btn.command = self.openSettingsMenu

                self.MainMenu.isMenuOpen = True

            else:
                self.MainMenu.isMenuOpen = False
                if(MyApp.MainMenu.left_entry.get() != ''): 
                    MyApp.MainMenu.left_ctrl_old.append(MyApp.MainMenu.left_entry.get())
                if(MyApp.MainMenu.right_entry.get() != ''):
                    MyApp.MainMenu.right_ctrl_old.append(MyApp.MainMenu.right_entry.get())
                if(MyApp.MainMenu.up_entry.get() != ''):
                    MyApp.MainMenu.up_ctrl_old.append(MyApp.MainMenu.up_entry.get())
                if(MyApp.MainMenu.down_entry.get() != ''):
                    MyApp.MainMenu.down_ctrl_old.append(MyApp.MainMenu.down_entry.get())

                self.closeMainMenu()

    def closeMainMenu(self):
        
        MyApp.MainMenu.menubgimg.destroy()
        MyApp.MainMenu.up_label.destroy()           
        MyApp.MainMenu.up_entry.destroy()

        MyApp.MainMenu.down_label.destroy()            
        MyApp.MainMenu.down_entry.destroy()

        MyApp.MainMenu.left_label.destroy()            
        MyApp.MainMenu.left_entry.destroy()

        MyApp.MainMenu.right_label.destroy()            
        MyApp.MainMenu.right_entry.destroy()
        #MyApp.MainMenu.save_btn.destroy()





def SetupScene(self):

    #UNIVERSE
    self.Universe = SpaceJamClasses.Universe(self.loader, "./Assets/Universe/Universe.x", self.render, "Universe", "./Assets/Universe/universe.jpg", (0, 0, 0), 25000)

    #PLANETS
    self.Planet1 = SpaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet1", "./Assets/Planets/earth.jpg",      (1000,      10,     -1000),     1000)
    self.Planet2 = SpaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet2", "./Assets/Planets/loaf.jpg",       (3000,     100,    -3000),    1000)
    self.Planet3 = SpaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet3", "./Assets/Planets/mars.jpg",       (21000,     1000,   -7000),     1100)
    self.Planet4 = SpaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet4", "./Assets/Planets/purple.jpg",     (-7000,     10,     21000),     1000)
    self.Planet5 = SpaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet5", "./Assets/Planets/saturn.jpg",     (-14000,    100,    14000),     1000)
    self.Planet6 = SpaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet6", "./Assets/Planets/shamrock.jpg",   (-21000,    1000,   7000),      1000)

    self.SpaceStation1 = SpaceJamClasses.SpaceStation(self.loader, "./Assets/Space Station/SpaceStation1B/spaceStation.egg", self.render, "Space Station", "./Assets/Space Station/SpaceStation1B/SpaceStation1_Dif2.png", (-2000, 10, -2000), 100)

    self.Hero = SpaceJamClasses.Player(self.loader, "./Assets/Dumbledore/Dumbledore.egg", self.render, "Player", "./Assets/Dumbledore/spacejet_C.png", (0, 0, 0), 100)

    #Baseball Seams
    for i in range(100):
        step = i
        droneName = 'drone' + str(i)
        droneCoords = DrawBaseballSeams(self, self.Planet1, droneName, step, 50)
        self.DroneObj = SpaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", droneCoords, 5)
        i = i + 1
    #X
    for i in range(150):
        step = i
        droneName = 'drone' + str(i)
        droneCoords = DrawXSeams(self, self.Planet2, droneName, step, 150)
        self.DroneObj = SpaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", droneCoords, 5)
        i = i + 1
    #Y
    for i in range(150):
        step = i
        droneName = 'drone' + str(i)
        droneCoords = DrawYSeams(self, self.Planet3, droneName, step, 150)
        self.DroneObj = SpaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", droneCoords, 5)
        i = i + 1
    #Z
    for i in range(150):
        step = i
        droneName = 'drone' + str(i)
        droneCoords = DrawZSeams(self, self.Planet4, droneName, step, 150)
        self.DroneObj = SpaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", droneCoords, 5)
        i = i + 1
    #Cloud
    for i in range(150):
        step = i
        droneName = 'drone' + str(i)
        droneCoords = DrawCloudDefense(self, self.Planet5, droneName)
        self.DroneObj = SpaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", droneCoords, 5)
        i = i + 1

def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 4.1):
    unitVec = DefensePaths.BaseballSeams(step, numSeams, B = 0.4)
    unitVec.normalize()
    position = unitVec * radius * 250 + centralObject.modelNode.getPos()
    return position

def DrawXSeams(self, centralObject, droneName, step, numSeams, radius = 4.1):
    unitVec = DefensePaths.XSeams(step, numSeams, B = 0.4)
    unitVec.normalize()
    position = unitVec * radius * 250 + centralObject.modelNode.getPos()
    return position

def DrawYSeams(self, centralObject, droneName, step, numSeams, radius = 4.1):
    unitVec = DefensePaths.YSeams(step, numSeams, B = 0.4)
    unitVec.normalize()
    position = unitVec * radius * 250 + centralObject.modelNode.getPos()
    return position

def DrawZSeams(self, centralObject, droneName, step, numSeams, radius = 4.1):
    unitVec = DefensePaths.ZSeams(step, numSeams, B = 0.4)
    unitVec.normalize()
    position = unitVec * radius * 250 + centralObject.modelNode.getPos()
    return position
    
def DrawCloudDefense(self, centralObject, droneName):
    unitVec = DefensePaths.DrawCloud()
    unitVec.normalize()
    position = unitVec * 1250 + centralObject.modelNode.getPos()
    SpaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10)
    SpaceJamClasses.Drone.droneCount += 1
    nickName = "Drone" + str(SpaceJamClasses.Drone.droneCount)
    return position

def SetCamera(self):
    self.disableMouse() # disables the default panda mouse movement controls
    self.camera.reparentTo(self.Hero.modelNode)
    self.camera.setFluidPos(0, 1, 0)

def SetMovement(self):
    SpaceJamClasses.Player.Thrust(self, 'space')





app = MyApp()
app.run()