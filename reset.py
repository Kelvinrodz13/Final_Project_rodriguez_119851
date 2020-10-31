from graphics import *

def reset(self,win):
        rect2 = Rectangle(Point(235,235),Point(265,265))
        rect2.setFill('cyan')
        rect2.draw(win)
        rect = Rectangle(Point(230,25),Point(270,55))
        rect.setFill(color_rgb(30,50,30))
        rect.draw(win)