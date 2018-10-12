import turtle
import time
def drawGap():
    turtle.penup()
    turtle.fd(5)
def drawline(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDight(dight):
    drawline(True)if dight in[2,3,4,5,6,8,9]else drawline(False)
    drawline(True)if dight in[0,3,1,4,5,6,7,8,9]else drawline(False)
    drawline(True)if dight in[2,3,0,5,6,8,9]else drawline(False)
    drawline(True)if dight in[2,0,6,8]else drawline(False)
    turtle.left(90)
    drawline(True)if dight in[0,4,5,6,8,9]else drawline(False)
    drawline(True)if dight in[2,3,0,5,7,8,9]else drawline(False)
    drawline(True)if dight in[2,3,0,1,4,7,8,9]else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
    turtle.penup()
    turtle.fd(20)
    turtle.pendown()
    turtle.fd(1)
    turtle.left(90)
    turtle.fd(1)
    turtle.left(90)
    turtle.fd(1)
    turtle.left(90)
    turtle.fd(1)
    turtle.left(90)
    turtle.penup()
    turtle.fd(20)
def drawdate(date):
        turtle.pencolor("red")
        for i in date:
            
            if i=='-':
                turtle.write('年',font=("Arial",32,"normal"))
                turtle.pencolor("green")
                turtle.fd(40)
            elif i=='=':
                turtle.write('月',font=("Arial",32,"normal"))
                turtle.pencolor("blue")
                turtle.fd(40)
            elif i=='+':
                turtle.pencolor("pink")
                turtle.write('日',font=("Arial",32,"normal"))   
            else:
                drawDight(eval(i))
def main():
    turtle.setup(1200,350,200,200)
    turtle.penup()
    turtle.fd(-500)
    turtle.pensize(5)
    drawdate(time.strftime("%H-%M=%S+",time.localtime()))
    turtle.hideturtle()
    
    turtle.done()
turtle.speed(0)
#turtle.Turtle().screen.delay(0)    


main()
