import pygame
import time

class Arrow(object):
    def __init__(self,shape,color):
        self.shape = shape
        self.color = color

    def turn(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == 1 and action != None:
            action()

def triangle(screen):
    red = (165,42,42)
    pygame.draw.polygon(screen,red,((100,250),(50,280),(100,310)))

def triangleTwo(screen):
    red = (165,42,42)
    pygame.draw.polygon(screen,red,((400,250),(450,280),(400,310)))

#These two triangles should probably be a class but they took me forever and I can't look at them anymore

def main():
    pygame.init()
    on = True
    while on:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                on = False
        screen = pygame.display.set_mode((500,500))
        pygame.display.set_caption("Escape")
        screen.fill((248,248,255))
        turnLeft = Arrow(triangle(screen),(165,42,42))
        turnRight = Arrow(triangleTwo(screen),(165,42,42))
        turnLeft.turn()
        turnRight.turn()
        pygame.display.update()
    pygame.quit()
    quit()
main()
