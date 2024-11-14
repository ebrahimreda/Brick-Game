from turtle import Screen, Turtle
from ball import Ball
from paddles import Paddel
from breakout_rewards import RewardManager, Reward
import time

FIRST_SCREEN= Screen()
FIRST_SCREEN.bgcolor("black")
FIRST_SCREEN.setup(width=800, height=600)
FIRST_SCREEN.tracer(0)

Instructions = Turtle()
Instructions.hideturtle()
Instructions.penup()
Instructions.color("white")
Instructions.goto(-380, 100)
Instructions.write("Turtle Loses LIVES 2\nThe circle increases the life by 2"
                   "\nThe square increases the life by 1"
                   "\nThe triangle increases the life by 1" 
                   "\n انتظر 5 ثواني , Wait 5 seconds"
                   , align="left", font=("Arial", 24, "normal"))


FIRST_SCREEN.update()

time.sleep(4.9)
FIRST_SCREEN.clear()




# إعداد الشاشة
SecondScreen = Screen()
SecondScreen.bgcolor("#ADD8E6")
SecondScreen.setup(width=2000, height=1000)
SecondScreen.tracer(0)

# إنشاء كائنات
paddels_ = Paddel()
ball = Ball()
blocks_manager = RewardManager()
blocks = blocks_manager.paddles

LIVES=3
LIVES_display =Turtle()
LIVES_display.hideturtle()
LIVES_display.color("black")
LIVES_display.penup()
LIVES_display.goto(-900, 400)
LIVES_display.write(f"LIVES: {LIVES}", align="left", font=("Arial", 24, "normal"))


# حركة الأسهم
SecondScreen.listen()
SecondScreen.onkeypress(paddels_.run_Left, "Left")
SecondScreen.onkeypress(paddels_.run_Right, "Right")

# تشغيل اللعبة
time.sleep(0.2)
GameOn = True
while GameOn:
    ball.move()
    SecondScreen.update()
    time.sleep(0.01)

    # ارتداد الكرة عند التصادم
    if ball.xcor() >= 980 or ball.xcor() <= -980:
        ball.bounce_x()

    # حدود السقف
    if ball.ycor() >= 480:
        ball.bounce_y()

    # حدود الأرض
    if ball.ycor() <= -500:
        ball.goto(0, 0)
        ball.bounce_y()
        LIVES -= 1
        LIVES_display.clear()
        LIVES_display.write(f"LIVES: {LIVES}", align="left", font=("Arial", 24, "normal"))

        # انهاء اللعبة
        if LIVES <= 0:
            LIVES_display.clear()
            LIVES_display.goto(0, 0)
            LIVES_display.write("Game Over", align="center", font=("Arial", 36, "normal"))
            GameOn= False
            break

    # الاصطدام مع المضرب
    if ball.distance(paddels_) <= 60 and ball.ycor() <= -460:
        ball.bounce_y()

    # تكرار على الطوب لإخفائه عند الاصطدام
    for block in blocks[:]:
        if len(blocks[:])<=0:
            break
        if ball.distance(block) < 50:
            ball.bounce_y()
            if isinstance(block, Reward):#  لو الطوبة مكافأة ==True
                block.is_active = True

            else:
                block.hideturtle()
                blocks.remove(block)

    # تحريك الجوائز
    for block in blocks:
        if isinstance(block, Reward):
            block.move()
            block.showturtle()

        if block.distance(paddels_) < 50 and block.shape()=="turtle":
            block.hideturtle()
            blocks.remove(block)
            LIVES -= 2
            LIVES_display.clear()
            LIVES_display.write(f"LIVES: {LIVES}", align="left", font=("Arial", 24, "normal"))


        elif block.distance(paddels_) < 50 and block.shape() == "circle":
            block.hideturtle()
            blocks.remove(block)
            LIVES += 2
            LIVES_display.clear()
            LIVES_display.write(f"LIVES: {LIVES}", align="left", font=("Arial", 24, "normal"))

        elif block.distance(paddels_) < 50 and block.shape() == "square":
            block.hideturtle()
            blocks.remove(block)
            LIVES += 1
            LIVES_display.clear()
            LIVES_display.write(f"LIVES: {LIVES}", align="left", font=("Arial", 24, "normal"))

        elif block.distance(paddels_) < 50 and block.shape() == "triangle":
            block.hideturtle()
            blocks.remove(block)
            LIVES += 1
            LIVES_display.clear()
            LIVES_display.write(f"LIVES: {LIVES}", align="left", font=("Arial", 24, "normal"))

        elif block.ycor() <= -500:
            block.hideturtle()
            blocks.remove(block)

SecondScreen.exitonclick()