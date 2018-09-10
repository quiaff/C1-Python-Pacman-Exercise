#
# Developed by 10Pines SRL
# License: 
# This work is licensed under the 
# Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. 
# To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/ 
# or send a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View, 
# California, 94041, USA.
#  
import unittest

class Point:
    
    def __init__(self,x,y):
        self._x = x
        self._y = y 
        
    def __eq__(self,anObject):
        if isinstance(anObject,self.__class__):
            return (self._x == anObject.x()) and (self._y == anObject.y())
        
        return False
    
    def __add__(self,aPoint):
        return Point(self._x+aPoint.x(),self._y+aPoint.y())

    def x(self):
        return self._x
    
    def y(self):
        return self._y

class Actor:
    
    def position(self):
        raise NotImplementedError('Subclass should implement')
    
class Pacman(Actor):
    def position(self):
        raise NotImplementedError('Should implement')
        
class Ghost(Actor):
    def position(self):
        raise NotImplementedError('Should implement')
    
class ConstructionBlockType:
    def nextPositionForGoing(self,anActor,aDirection):
        raise NotImplementedError()
        
class WallType(ConstructionBlockType):
    pass
    
class SpaceType(ConstructionBlockType):
    pass

class LeftTransporterType(ConstructionBlockType):
    pass
    
class GhostHouseDoorType(ConstructionBlockType):
    pass

class TestPacman(unittest.TestCase):
    
    def setUp(self):
        self.pacman = None
        self.blueGhost = None
        self.wallType = None
        self.spaceType = None
        self.leftTransporterType = None
        self.ghostHouseDoorType = None
        
        self.left = None
        self.right = None
        self.up = None
        self.down = None
    
    def testGhostCanNotGoIntoAWall(self):
        self.assertEquals(
                self.blueGhost.position(),
                self.wallType.nextPositionForGoing(self.blueGhost,self.left))

        self.assertEquals(
                self.blueGhost.position(),
                self.wallType.nextPositionForGoing(self.blueGhost,self.right))
        
        self.assertEquals(
                self.blueGhost.position(),
                self.wallType.nextPositionForGoing(self.blueGhost,self.up))
        
        self.assertEquals(
                self.blueGhost.position(),
                self.wallType.nextPositionForGoing(self.blueGhost,self.down))
    
    def testPacmanCanNotGoIntoAWall(self):
        self.assertEquals(
                self.pacman.position(),
                self.wallType.nextPositionForGoing(self.pacman,self.left))

        self.assertEquals(
                self.pacman.position(),
                self.wallType.nextPositionForGoing(self.pacman,self.right))
        
        self.assertEquals(
                self.pacman.position(),
                self.wallType.nextPositionForGoing(self.pacman,self.up))
        
        self.assertEquals(
                self.pacman.position(),
                self.wallType.nextPositionForGoing(self.pacman,self.down))

    def testPacmanMovesFastIntoSpaces(self):
        self.assertEquals(
                self.pacman.position() + Point(-2,0),
                self.spaceType.nextPositionForGoing(self.pacman,self.left))

        self.assertEquals(
                self.pacman.position() + Point(2,0),
                self.spaceType.nextPositionForGoing(self.pacman,self.right))
        
        self.assertEquals(
                self.pacman.position() + Point(0,2),
                self.spaceType.nextPositionForGoing(self.pacman,self.up))
        
        self.assertEquals(
                self.pacman.position() + Point(0,-2),
                self.spaceType.nextPositionForGoing(self.pacman,self.down))

    def testGhostMovesSlowlyIntoSpaces(self):
        self.assertEquals(
                self.blueGhost.position() + Point(-1,0),
                self.spaceType.nextPositionForGoing(self.blueGhost,self.left))

        self.assertEquals(
                self.blueGhost.position() + Point(1,0),
                self.spaceType.nextPositionForGoing(self.blueGhost,self.right))
        
        self.assertEquals(
                self.blueGhost.position() + Point(0,1),
                self.spaceType.nextPositionForGoing(self.blueGhost,self.up))
        
        self.assertEquals(
                self.blueGhost.position() + Point(0,-1),
                self.spaceType.nextPositionForGoing(self.blueGhost,self.down))

    def testGhostCanEnterHisHouse(self):
        self.assertEquals(
                self.blueGhost.position() + Point(-1,0),
                self.ghostHouseDoorType.nextPositionForGoing(self.blueGhost,self.left))

        self.assertEquals(
                self.blueGhost.position() + Point(1,0),
                self.ghostHouseDoorType.nextPositionForGoing(self.blueGhost,self.right))
        
        self.assertEquals(
                self.blueGhost.position() + Point(0,1),
                self.ghostHouseDoorType.nextPositionForGoing(self.blueGhost,self.up))
        
        self.assertEquals(
                self.blueGhost.position() + Point(0,-1),
                self.ghostHouseDoorType.nextPositionForGoing(self.blueGhost,self.down))
 
    def testPacmanCanNotEnterGhostHouse(self):
        self.assertEquals(
                self.pacman.position(),
                self.ghostHouseDoorType.nextPositionForGoing(self.pacman,self.left))

        self.assertEquals(
                self.pacman.position(),
                self.ghostHouseDoorType.nextPositionForGoing(self.pacman,self.right))
        
        self.assertEquals(
                self.pacman.position(),
                self.ghostHouseDoorType.nextPositionForGoing(self.pacman,self.up))
        
        self.assertEquals(
                self.pacman.position(),
                self.ghostHouseDoorType.nextPositionForGoing(self.pacman,self.down))
 
    def testTransporterMovesPacmanToNewPosition(self):
        self.assertEquals(
                Point(10,4),
                self.leftTransporterType.nextPositionForGoing(self.pacman,self.left))

        self.assertEquals(
                Point(10,4),
                self.leftTransporterType.nextPositionForGoing(self.pacman,self.right))

    def testGhostCanNotGoIntoTransporter(self):
        self.assertEquals(
                self.blueGhost.position(),
                self.leftTransporterType.nextPositionForGoing(self.blueGhost,self.left))

        self.assertEquals(
                self.blueGhost.position(),
                self.leftTransporterType.nextPositionForGoing(self.blueGhost,self.right))
