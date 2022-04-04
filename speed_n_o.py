from turtle import *
import time

class Char(Turtle):
    def __init__(self, x, y, step):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(0, 1)
        self.color("orange")
        self.shape("triangle")
        self.step = step
        self.x = x
        self.y = y
    def move_up(self):
        self.goto(self.xcor(),self.ycor()+self.step)
    def move_down(self):
        self.goto(self.xcor(),self.ycor()-self.step)
    def move_left(self):
        self.goto(self.xcor()-self.step,self.ycor())
    def move_right(self):
        self.goto(self.xcor()+self.step,self.ycor())

class Enemy1(Turtle):
    def __init__(self, x, y, step):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(0, 100)
        self.color("red")
        self.shape("square")
        self.step = step
        self.x = x
        self.y = y
        self.i1 = 0
    def run1(self):
        if self.i1 == 23:
            while self.i1 != 1:
                self.goto(self.xcor()+self.step,self.ycor())
                self.i1 -= 1
                if main.distance(complet.xcor(), complet.ycor()) <= 20:
                    main.goto(21, 900)
                    main.color("white")
                    clon.goto(0, 900)
                    clon.color("white")
                    print("Победа!")
                    enem1.goto(0, 400)
                    enem2.goto(0, 400)
                    complet.goto(0, 900)
                enem1.atack1()
        self.goto(self.xcor()-self.step,self.ycor())
        self.i1 += 1
        if main.distance(complet.xcor(), complet.ycor()) <= 20:
            main.goto(21, 900)
            main.color("white")
            clon.goto(0, 900)
            clon.color("white")
            print("Победа!")
            enem1.goto(0, 400)
            enem2.goto(0, 400)
            complet.goto(0, 900)
        enem1.atack1()
        enem2.run2()
    def atack1(self):
        if main.distance(enem1.xcor(), enem1.ycor()) <= 20 or clon.distance(enem1.xcor(), enem1.ycor()) <= 20:
            if main.distance(enem1.xcor(), enem1.ycor()) <= 20:
                main.goto(21, 900)
                main.color("white")
                clon.goto(0, 900)
                clon.color("white")
                print("Проигрыш!")
                enem1.goto(0, 400)
                enem2.goto(0, 400)
                complet.goto(0, 900)
            elif clon.distance(enem1.xcor(), enem1.ycor()) <= 20:
                clon.color("white")
                clon.goto(0, 800)
                print("Клон был утерян!")

class Enemy2(Turtle):
    def __init__(self, x, y, step):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(0, 150)
        self.color("red")
        self.shape("square")
        self.step = step
        self.x = x
        self.y = y
        self.i2 = 0
    def run2(self):
        if self.i2 == 23:
            while self.i2 != 1:
                self.goto(self.xcor()-self.step,self.ycor())
                self.i2 -= 1
                if main.distance(complet.xcor(), complet.ycor()) <= 20:
                    main.goto(21, 900)
                    main.color("white")
                    clon.goto(0, 900)
                    clon.color("white")
                    print("Победа!")
                    enem1.goto(0, 400)
                    enem2.goto(0, 400)
                    complet.goto(0, 900)
                enem2.atack2()
                    
        self.goto(self.xcor()+self.step,self.ycor())
        self.i2 += 1
        if main.distance(complet.xcor(), complet.ycor()) <= 20 or clon.distance(complet.xcor(), complet.ycor()) <= 20:
            if main.distance(complet.xcor(), complet.ycor()) <= 20:
                main.goto(21, 900)
                main.color("white")
                clon.goto(0, 900)
                clon.color("white")
                print("Победа!")
                enem1.goto(0, 400)
                enem2.goto(0, 400)
                complet.goto(0, 900)
        enem2.atack2()
        enem1.run1()

    def atack2(self):
        if main.distance(enem2.xcor(), enem2.ycor()) <= 20 or clon.distance(enem2.xcor(), enem2.ycor()) <= 20:
            if main.distance(enem2.xcor(), enem2.ycor()) <= 20:
                main.goto(21, 900)
                main.color("white")
                clon.goto(0, 900)
                clon.color("white")
                print("Проигрыш!")
                enem1.goto(0, 400)
                enem2.goto(0, 400)
                complet.goto(0, 900)
            if clon.distance(enem2.xcor(), enem2.ycor()) <= 20:
                clon.color("white")
                clon.goto(0, 800)
                print("Клон был утерян!")
        
class Clone(Turtle):
    def __init__(self, x, y, step):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(21, 400)
        self.color("orange")
        self.shape("triangle")
        self.step = step
        self.x = x
        self.y = y
    def hide(self):
        self.goto(21, 400)
        self.penup()
        self.color("white")
    def visible(self):
        self.goto(main.xcor()+50,main.ycor())
        self.color("orange")
    def move_up(self):
        self.goto(self.xcor(),self.ycor()+self.step)
    def move_down(self):
        self.goto(self.xcor(),self.ycor()-self.step)
    def move_left(self):
        self.goto(self.xcor()-self.step,self.ycor())
    def move_right(self):
        self.goto(self.xcor()+self.step,self.ycor())

class Complete(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(50, 200)
        self.color("green")
        self.shape("triangle")
        self.x = x
        self.y = y

main = Char(0, 1, 10)
clon = Clone(20, 20, 10)
clon.hide()
complet = Complete(50, 200)

scr = main.getscreen()
scr.listen()

scr.onkey(main.move_up,"Up")
scr.onkey(main.move_down,"Down")
scr.onkey(main.move_left,"Left")
scr.onkey(main.move_right,"Right")

scr.onkey(clon.visible,"2")
scr.onkey(clon.hide,"1")

scr.onkey(clon.move_up,"W")
scr.onkey(clon.move_down,"S")
scr.onkey(clon.move_left,"A")
scr.onkey(clon.move_right,"D")

enem1 = Enemy1(0, 100, 10)
enem2 = Enemy2(0, 200, 10)

enem1.run1()