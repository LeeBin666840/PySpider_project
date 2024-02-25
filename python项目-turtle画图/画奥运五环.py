"""
-*- coding: utf-8 -*-
@Time    : 2022/9/27 13:31
@Author  : 无言
@FileName: 画奥运五环.py
@Software: PyCharm
"""
import turtle

turtle.hideturtle()
turtle.pensize(8)

def draw_a_circle(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pensize(5)
    turtle.pencolor(color)
    turtle.pendown()
    turtle.circle(70)
    turtle.penup()

draw_a_circle(-130, 75, "cyan")
draw_a_circle(-10, 75, "black")
draw_a_circle(110, 75, "red")
draw_a_circle(-60, -20, "yellow")
draw_a_circle(60, -20, "lightgreen")

turtle.mainloop()
