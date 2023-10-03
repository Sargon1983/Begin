import turtle
turtle.speed(25)
for i in range(1, 100, 2):
    turtle.circle(-i)
    turtle.circle(i)
    turtle.forward(i)
    turtle.right(i)
    turtle.pensize(1+i/(i+1))
    