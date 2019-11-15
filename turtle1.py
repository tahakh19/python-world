# Python program to draw square 
# using Turtle Programming
import random
import turtle


skk = turtle.Turtle() 

'''
for i in range(4): 
	skk.backward(100) 
	skk.left(90) 
'''

#turtle.done() 


# Python program to draw star 
# using Turtle Programming 
#star = turtle.Turtle() 
'''
for i in range(10): 
	skk.backward(50) 
	skk.right(120) 
'''

#polygon = turtle.Turtle() 

'''
num_sides = 200
side_length = 2
angle = 360.0 / num_sides 

for i in range(num_sides): 
	skk.forward(side_length) 
	skk.right(angle) 
'''

#colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
colors = ['red', 'blue'] 
t = turtle.Pen() 
turtle.bgcolor('black')
#turtle.bgcolor('green')
for x in range(360):
    #t.pencolor(colors[x%2])
    #turtle.color(random.random(), random.random(), random.random())
    t.pencolor(random.random(), random.random(), random.random())
    #t.pensize(100)
    t.width(x/100 + 1) 
    t.forward(x) 
    t.left(59) 

turtle.done() 
