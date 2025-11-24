import turtle
turtle.setup(650,350,300,300)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor('purple')
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)#40°方向回正
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.down()
