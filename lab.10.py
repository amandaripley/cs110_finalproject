import random

class Key:
    def __init__(self, name, shape = 0, x, y, x = 0, y = 0, inventory_x, inventory_y):
        self.name = name
        self.shape = shape
        self.x = x
        self.y = y
        self.inventory_x = [1,2,3,4,5,6,7,8,9,10]
        self.inventory_y = [1,2]
        #different shapes of different keys for different level

    def __int__(self):
        return int(self.shape)

    def open(shape, hole):
        #open the box and the door
        if self.shape == hole.shape
        return self

    def save_in_inventory(self):
        if self:
            move_x = random.choice(self.inventory_x)
            move_y = random.choice(self.inventory_y)
            self.x += move_x
            self.y += move_y
            inventory_x.remove(move_x)
            inventory_y.remove(move_y)
        #the found keys saved in the inventory
