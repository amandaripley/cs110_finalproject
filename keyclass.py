import random

class Key:
    def __init__(self, name,shape = 0,  x = 0, y = 0):
        self.name = name
        self.shape = shape
        self.x = x
        self.y = y

        #different shapes of different keys for different level

    def open(self, hole):
        #open the box and the door
	self.hole = hole
        if self.shape == self.hole:
		print True
            	return self
