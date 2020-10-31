from graphics import *
import random 

def GraphicInterface(win):  

    #Main Board
    big_rect1 = Rectangle(Point(15,10),Point(560,550))
    big_rect1.setFill(color_rgb(255,253,208))
    big_rect1.setWidth(3)
    big_rect1.draw(win)



    #Starting Positions for the respective Players
    green_circ = Circle(Point(108,455),89)
    green_circ.setFill('green')
    green_circ.setWidth(1)
    green_circ.draw(win)

    red_circ = Circle(Point(108,107),89)
    red_circ.setFill('red')
    red_circ.draw(win)

    blue_circ = Circle(Point(465,107),89)
    blue_circ.setFill('cyan')
    blue_circ.draw(win)

    yellow_circ = Circle(Point(465,455),89)
    yellow_circ.setFill('yellow')
    yellow_circ.draw(win)



    #Creating rectangle inside Circles
    green_rect14 = Rectangle(Point(50,520),Point(165,390))
    green_rect14.setFill('green')
    green_rect14.setWidth(1)
    green_rect14.draw(win)

    red_rect14 = Rectangle(Point(50,175),Point(165,40))
    red_rect14.setFill('red')
    red_rect14.setWidth(1)
    red_rect14.draw(win)

    blue_rect14 = Rectangle(Point(400,170),Point(527,45))
    blue_rect14.setFill(color_rgb(115,125,255))
    blue_rect14.setWidth(1)
    blue_rect14.draw(win)

    yellow_rect14 = Rectangle(Point(400,520),Point(527,390))
    yellow_rect14.setFill(color_rgb(255,255,120))
    yellow_rect14.setWidth(1)
    yellow_rect14.draw(win)


    #Creating Main Rows For Each side
    yellow_rect2 = Rectangle(Point(230,200),Point(340,540))
    yellow_rect2.setWidth(1)
    yellow_rect2.draw(win)

    green_rect2 = Rectangle(Point(15,230),Point(340,330))
    green_rect2.draw(win)

    red_rect2 = Rectangle(Point(230,15),Point(340,540))
    red_rect2.draw(win)

    blue_rect2 = Rectangle(Point(230,230),Point(550,330))
    blue_rect2.draw(win)



    #Creating Columns and rows for bottom hand side
    yellow_rect3 = Rectangle(Point(230,200),Point(260,540))
    yellow_rect3.setWidth(1)
    yellow_rect3.draw(win)

    yellow_rect4 = Rectangle(Point(260,300),Point(305,540))
    yellow_rect4.setFill('yellow')
    yellow_rect4.setWidth(1)
    yellow_rect4.draw(win)

    yellow_rect5 = Rectangle(Point(230,446),Point(340,475))
    yellow_rect5.setWidth(1)
    yellow_rect5.draw(win)

    yellow_rect6 = Rectangle(Point(230,417),Point(340,446))
    yellow_rect6.setWidth(1)
    yellow_rect6.draw(win)

    yellow_rect7 = Rectangle(Point(230,388),Point(340,417))
    yellow_rect7.setWidth(1)
    yellow_rect7.draw(win)

    yellow_rect8 = Rectangle(Point(230,359),Point(340,388))
    yellow_rect8.setWidth(1)
    yellow_rect8.draw(win)

    yellow_rect9 = Rectangle(Point(230,330),Point(340,359))
    yellow_rect9.setWidth(1)
    yellow_rect9.draw(win)

    yellow_rect10 = Rectangle(Point(230,300),Point(340,330))
    yellow_rect10.setWidth(1)
    yellow_rect10.draw(win)

    yellow_rect11 = Rectangle(Point(230,446),Point(340,510))
    yellow_rect11.setWidth(1)
    yellow_rect11.draw(win)


    #Safe Space Color Fill
    yellow_rect20 = Rectangle(Point(305,388),Point(340,417))
    yellow_rect20.setFill('yellow')
    yellow_rect20.setWidth(1)
    yellow_rect20.draw(win)

    yellow_rect20 = Rectangle(Point(230,388),Point(260,417))
    yellow_rect20.setFill('green')
    yellow_rect20.setWidth(1)
    yellow_rect20.draw(win)

   

    #Color of Middle Rectangle
    rectmain = Rectangle(Point(260,255),Point(308,300))
    rectmain.setFill('red')
    rectmain.draw(win)



    #Color of middle Polygons
    poly_r3 = Polygon(Point(260,255),Point(260,300),Point(284,277.5))
    poly_r3.setWidth(1)
    poly_r3.setFill('green')
    poly_r3.draw(win)

    poly_r4 = Polygon(Point(308,255),Point(308,300),Point(284,277.5))
    poly_r4.setWidth(1)
    poly_r4.setFill('blue')
    poly_r4.draw(win)

    poly_r5 = Polygon(Point(308,300),Point(260,300),Point(284,277.5))
    poly_r5.setWidth(1)
    poly_r5.setFill('yellow')
    poly_r5.draw(win)
    
    green_rect3 = Rectangle(Point(15,230),Point(230,255))
    green_rect3.setWidth(1)
    green_rect3.draw(win)

    green_rect4 = Rectangle(Point(15,255),Point(260,300))
    green_rect4.setFill('green')
    green_rect4.setWidth(1)
    green_rect4.draw(win)



    #Redid the lower rectangle so the green space would not overlap it in space 60/8
    yellow_rect25 = Rectangle(Point(230,200),Point(340,540))
    yellow_rect25.setWidth(1)
    yellow_rect25.draw(win)

    
    #Continuation of Column and rows
    green_rect5 = Rectangle(Point(15,230),Point(45,330))
    green_rect5.setWidth(1)
    green_rect5.draw(win)

    green_rect6 = Rectangle(Point(45,230),Point(80,330))
    green_rect6.setWidth(1)
    green_rect6.draw(win)

    green_rect7 = Rectangle(Point(80,230),Point(112,330))
    green_rect7.setWidth(1)
    green_rect7.draw(win)

    green_rect8 = Rectangle(Point(112,230),Point(141,330))
    green_rect8.setWidth(1)
    green_rect8.draw(win)

    green_rect9 = Rectangle(Point(141,230),Point(170,330))
    green_rect9.setWidth(1)
    green_rect9.draw(win)

    green_rect10 = Rectangle(Point(170,230),Point(200,330))
    green_rect10.setWidth(1)
    green_rect10.draw(win)



    #Safe spaces for left hand side
    green_rect11 = Rectangle(Point(141,230),Point(170,255))
    green_rect11.setFill('red')
    green_rect11.draw(win)

    green_rect12 = Rectangle(Point(141,300),Point(170,330))
    green_rect12.setFill('green')
    green_rect12.draw(win)




    #Creating columns and rows for top side
    red_rect3 = Rectangle(Point(230,15),Point(260,200))
    red_rect3.setWidth(1)
    red_rect3.draw(win)

    red_rect4 = Rectangle(Point(260,15),Point(305,255))
    red_rect4.setFill('red')
    red_rect4.draw(win)

    red_rect24 = Rectangle(Point(230,15),Point(340,540))
    red_rect24.draw(win)

    red_rect5 = Rectangle(Point(260,171),Point(340,200))
    red_rect5.setWidth(1)
    red_rect5.draw(win)

    red_rect6 = Rectangle(Point(230,142),Point(340,171))
    red_rect6.setWidth(1)
    red_rect6.draw(win)

    red_rect7 = Rectangle(Point(230,113),Point(340,142))
    red_rect7.setWidth(1)
    red_rect7.draw(win)

    red_rect8 = Rectangle(Point(230,84),Point(340,113))
    red_rect8.setWidth(1)
    red_rect8.draw(win)

    red_rect9 = Rectangle(Point(230,55),Point(340,84))
    red_rect9.setWidth(1)
    red_rect9.draw(win)



    #Safe spaces filled for top side
    red_rect11 = Rectangle(Point(305,142),Point(340,171))
    red_rect11.setFill('blue')
    red_rect11.draw(win)

    red_rect12 = Rectangle(Point(230,142),Point(260,171))
    red_rect12.setFill('red')
    red_rect12.draw(win)


    red_rect3 = Rectangle(Point(340,230),Point(550,260))
    red_rect3.setWidth(1)
    red_rect3.draw(win)

    red_rect4 = Rectangle(Point(308,260),Point(550,300))
    red_rect4.setWidth(1)
    red_rect4.setFill('blue')
    red_rect4.draw(win)



    #Redid the rectangle due to overlap in space  42/26 
    #Creating Cloumns and rows for right hand side
    blue_rect20 = Rectangle(Point(230,230),Point(550,330))
    blue_rect20.draw(win)

    blue_rect5 = Rectangle(Point(340,230),Point(370,260))
    blue_rect5.setWidth(1)
    blue_rect5.draw(win)

    blue_rect6 = Rectangle(Point(370,230),Point(400,330))
    blue_rect6.setWidth(1)
    blue_rect6.draw(win)

    blue_rect7 = Rectangle(Point(400,230),Point(430,330))
    blue_rect7.setWidth(1)
    blue_rect7.draw(win)

    blue_rect8 = Rectangle(Point(430,230),Point(460,260))
    blue_rect8.setWidth(1)
    blue_rect8.draw(win)

    blue_rect9 = Rectangle(Point(460,230),Point(490,330))
    blue_rect9.setWidth(1)
    blue_rect9.draw(win)

    blue_rect10 = Rectangle(Point(490,230),Point(520,330))
    blue_rect10.setWidth(1)
    blue_rect10.draw(win)

    blue_rect11 = Rectangle(Point(400,230),Point(430,260))
    blue_rect11.setFill('blue')
    blue_rect11.draw(win)

    blue_rect12 = Rectangle(Point(400,300),Point(430,330))
    blue_rect12.setFill('yellow')
    blue_rect12.draw(win)



    #Lines for Polygons
    x = Line(Point(230,230), Point(340,330))
    x.setFill('black')
    x.draw(win)

    x2 = Line(Point(340,230), Point(230,330))
    x2.setFill('black')
    x2.draw(win)

 



