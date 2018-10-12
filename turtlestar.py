import turtle
def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in[0,80,-160,80]:
            turtle.left(angle)
            koch(size/3,n-1)
def main():
    turtle.speed(0)
    turtle.setup(1000,800)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor("red")
    leval=3
    koch(300,leval)
    turtle.right(60)
    turtle.pencolor("green")
    koch(300,leval)
    turtle.right(60)
    turtle.pencolor("blue")
    koch(300,leval)
    turtle.right(60)
    turtle.pencolor("red")
    koch(300,leval)
    turtle.right(60)
    turtle.pencolor("green")
    koch(300,leval)
    turtle.right(60)
    turtle.pencolor("blue")
    koch(300,leval)
    turtle.hideturtle()
    turtle.done()
main()
