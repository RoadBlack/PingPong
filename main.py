import turtle
import os
wn = turtle.Screen()
wn.title("Pong Przez Patryka bo mam za dużo czasu")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


#player_a= turtle.textinput("Wpisz swój nick", "Gracz Nr 1(lewo)")
#color_a= turtle.textinput("Wybierz swój kolor", "Wybierz swój kolor w języku angielskim:{}".format(player_a))
#while color_a =="":
#    color_a = turtle.textinput("Wybierz swój kolor", "Wybierz swój kolor w języku angielskim:{}".format(player_a))
#player_b= turtle.textinput("Wpisz swój nick", "Gracz Nr 2(prawo)")
#color_b= turtle.textinput("Wybierz swój kolor", "Wybierz swój kolor w języku angielskim: {}".format(player_b))
#while color_b =="":
 #   color_b = turtle.textinput("Wybierz swój kolor", "Wybierz swój kolor w języku angielskim: {}".format(player_b))

player_a = "Adam"
color_a = "blue"
player_b = "Jolo"
color_b = "pink"
# Score
score_a = 0
score_b = 0




#leftBorder
border_a= turtle.Turtle()
border_a.speed(0)
border_a.shape("square")
border_a.color("red")
border_a.shapesize(stretch_wid=0.1 , stretch_len=30)
border_a.penup()
border_a.left(90)
border_a.goto(-396 , 0)
border_a.hideturtle()
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("{}".format(color_a))
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("{}".format(color_b))
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
#RightBorder
border_b = turtle.Turtle()
border_b.speed(0)
border_b.shape("square")
border_b.color("red")
border_b.shapesize(stretch_wid=0.1 , stretch_len=30)
border_b.penup()
border_b.right(90)
border_b.goto(386 , 0)
border_b.hideturtle()


#ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2
#scoreBoard
score_a = 0
score_b = 0
board = turtle.Turtle()
board.speed(0)
board.color("white")
board.penup()
board.hideturtle()
board.goto(0,260)
board.write("{} :0  {}:0".format(player_a , player_b) , align="center" , font=("Courier" , 24 , "bold"))
#moving Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
while True:
    wn.update()
    border_a.hideturtle()
    border_b.hideturtle()
    #move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1
        os.system("afplay ping.wav&")
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *=-1
        os.system("afplay ping.wav&")
    if ball.xcor() >390:
        ball.goto(0 , 0)
        ball.dx *=-1
        score_a+=1
        board.clear()
        board.write("{}:{}  {}:{}".format(player_a , score_a , player_b, score_b), align="center", font=("Courier", 24, "bold"))
        border_b.showturtle()
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b+=1
        board.clear()
        board.write("{}:{}  {}:{}".format(player_a , score_a , player_b, score_b), align="center", font=("Courier", 24, "bold"))
        border_a.showturtle()
    #COLLISON
    if ball.xcor() >340  and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx*=-1
        os.system("afplay ping.wav&")
    if ball.xcor() < -340  and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx*=-1
        os.system("afplay ping.wav&")

    while paddle_a.ycor() > 270:
        paddle_a.goto(-350, 260)
    while paddle_a.ycor() < -260:
        paddle_a.goto(-350, -250)
    while paddle_b.ycor() > 270:
        paddle_b.goto(350, 260)
    while paddle_b.ycor() < -260:
        paddle_b.goto(350, -250)





