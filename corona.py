import turtle

t= turtle.Turtle()
s=turtle.Screen()

s.bgcolor("black")
t.pencolor("purple")
a=0
b=0
t.speed(200)
t.penup()
t.goto(0,-150)
t.pendown()
while True:
    t.forward(a)
    t.left(b)
    a+=1
    b+=1
    if b==200:
        break
    t.hideturtle()
a=0
b=0
t.speed(200)
t.penup()
t.goto(0,120)
t.pendown()
while True:
    t.forward(a)
    t.left(b)
    a+=1
    b+=1
    if b==200:
        break
    t.hideturtle()
a=0
b=0
t.speed(200)
t.penup()
t.goto(100,100)
t.pendown()
while True:
    t.forward(a)
    t.left(b)
    a+=1
    b+=1
    if b==200:
        break
    t.hideturtle()
turtle.done()
