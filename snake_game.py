import turtle
import time
import random

delay =0.1

## Score
score=0
high_score=0

## Set up screen
wn= turtle.Screen()
wn.title("Snake Game by San")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  # BY putting zero it turns off the screen animation

## Snake head

head= turtle.Turtle()
head.speed(0) # This is speed of animation not of paddle in game
head.shape("square")
head.color("black")
#head.shapesize(stretch_wid=1, stretch_len=1) # keeping length constanr and increasing the width by factor 5
head.penup()
head.goto(0,0)
#head.dx=0.5
#head.dy=head
head.direction= "stop"

## Snake food

food= turtle.Turtle()
food.speed(0) # This is speed of animation not of paddle in game
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,0)

segment=[]

## Pen
pen= turtle.Turtle()
pen.speed(0) # This is speed of animation not of paddle in game
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score=0  High Score=0", align="center", font=("courier",24,"normal"))


## Functions

def go_up():
    if head.direction!="down":
        head.direction="up"

def go_down():
    if head.direction!="up":
        head.direction="down"

def go_right():
    if head.direction!="left":
        head.direction="right"

def go_left():
    if head.direction!="right":
        head.direction="left"


def move():
    if head.direction=="up":
        y= head.ycor()
        head.sety(y+20)
    
    if head.direction=="down":
        y= head.ycor()
        head.sety(y-20)

    if head.direction=="right":
        x= head.xcor()
        head.setx(x+20)

    if head.direction=="left":
        x= head.xcor()
        head.setx(x-20)

## keyboard bindings

wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_left,"a")

## Main game loop
while True:
    wn.update()

    ## Check for collison with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction= "stop"
        

        ## Hide the segments

        for seg in segment:
            seg.goto(1000,1000) # Thare no tools in turtle to disappear or delete the segment hence it is better to move outside the window
        score=0
        pen.clear()
        pen.write("Score: {} High Score: {}". format(score, high_score), align="center",font=("courier",24,"normal"))
        ## Clear the segment list

        segment.clear()
    ## Check for collison with food
    if head.distance(food)<20:  # This is center distance between food and head which is nothing but collision
        #move the food to the random position
        x= random.randint(-290,290)
        y= random.randint(-290,290)
        food.goto(x,y)
         # Add a segment
        new_segment= turtle.Turtle()
        new_segment.speed(0) # This is speed of animation not of paddle in game
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segment.append(new_segment)

        ## Increase the score
        score +=10

        if score>high_score:
            high_score= score
        pen.clear()
        pen.write("Score: {} High Score: {}". format(score, high_score), align="center",font=("courier",24,"normal"))

    ## Move the end segment first in reverse order

    for index in range(len(segment)-1,0,-1):
        x=segment[index-1].xcor()
        y=segment[index-1].ycor()
        segment[index].goto(x,y)
    
    ## Move segement 0 to where the head is
    if len(segment)>0:
        x=head.xcor()
        y=head.ycor()
        segment[0].goto(x,y)    
    move()

    ## Check for collision with body segment
    for seg in segment:
        if seg.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction= "stop"
            for seg in segment:
                seg.goto(1000,1000)
            segment.clear()
            score=0
            pen.clear()
            pen.write("Score: {} High Score: {}". format(score, high_score), align="center",font=("courier",24,"normal"))
    time.sleep(delay)

wn.mainloop()





