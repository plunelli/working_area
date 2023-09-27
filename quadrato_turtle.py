import turtle
win=turtle.Screen()
win.bgcolor("black")
win.title("Quadrato")
t=turtle.Turtle()
t.color("green")
t.pensize(3)
for contatore in range (4):
    t.forward(100)
    t.right(90 )
p=input ("premi invio per concludere")