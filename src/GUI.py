import tkinter as tk
from BezierDivideAndConquer import *

root = tk.Tk()
root.title('Bezier Curve Simulation with Divide and Conquer')

points = Line() # List of points

def recursive_draw(start,color):
    if start.next!=None:
        canvas.create_line(start.x,start.y,start.next.x,start.next.y, fill=color, width=3)
        recursive_draw(start.next,color)
    else:
        pass

def key(event):
    print ("pressed", repr(event.char))

def click(event):
    print ("clicked at", event.x, event.y)
    points.pushback(Point(event.x,event.y))
    redrawCurve()

def redrawCurve():
    bezier = Line()
    bezierDivConquer(bezier,points,int(iterations.get()),0)
    canvas.delete("all")
    recursive_draw(points.head,"red")
    recursive_draw(bezier.head,"blue")

canvas= tk.Canvas(root, width=800, height=600)

canvas.pack()

frame = tk.LabelFrame(root, text='Options', padx=10, pady=5)
frame.place(in_=canvas, relx=1, rely=0, anchor='ne')

label = tk.Label(frame, text='Iterations: ')
label.pack()
iterations = tk.StringVar()
spinbox = tk.Spinbox(frame, command=redrawCurve, from_=1.0, to=12.0, textvariable=iterations, width=8, wrap=True)
spinbox.pack()

canvas.bind("<Key>", key)
canvas.bind("<Button-1>", click)

root.mainloop()