from turtle import *
pu()
ht()
right(30)
speed(100)
shape("triangle")


def sier(size, order):
    if order == 0:
        stamp()
    else:
        for i in range(0,3):         
            fillcolor("red") 
            forward(size) 
            
            sier(size/2,order-1)
            
            backward(size)
            left(120)
            
sier(100,4)  
window = Screen()      
window.exitonclick()


# Alternative Solutions


# from turtle import *

# def Sierpensky(l,d):
#     if d> 1 : dot()
#     if d==0 :
#         stamp()
#     else:
#         forward(l)
#         Sierpensky(l/2,d-1)
#         backward(l)
#         left(120)
#         forward(l)
#         Sierpensky (l/2,d-1)
#         backward(l)
#         left(120)
#         forward(l)
#         Sierpensky (l/2,d-1)
#         backward(l)
#         left(120)
# Sierpensky(200,6)

# import turtle
# def draw_sierpinski(length,depth):
#     if depth==0:
#         for i in range(0,3):
#             t.fd(length)
#             t.left(120)
#     else:
#         draw_sierpinski(length/2,depth-1)
#         t.fd(length/2)
#         draw_sierpinski(length/2,depth-1)
#         t.bk(length/2)
#         t.left(60)
#         t.fd(length/2)
#         t.right(60)
#         draw_sierpinski(length/2,depth-1)
#         t.left(60)
#         t.bk(length/2)
#         t.right(60)

# window = turtle.Screen()
# t = turtle.Turtle()
# draw_sierpinski(200,6)
# window.exitonclick()
