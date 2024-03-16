import tkinter
from BezierDivideAndConquer import *

root = tkinter.Tk()

points = Line() # List of points

def recursive_draw(start,color):
    if start.next!=None:
        canvas.create_line(start.x,start.y,start.next.x,start.next.y, fill=color, width=3)
        recursive_draw(start.next,color)
    else:
        pass

def key(event):
    print ("pressed", repr(event.char))

def callback(event):
    print ("clicked at", event.x, event.y)
    points.pushback(Point(event.x,event.y))
    bezier = Line()
    bezierDivConquer(bezier,points,12,0)
    canvas.delete("all")
    recursive_draw(points.head,"red")
    recursive_draw(bezier.head,"blue")
    

canvas= tkinter.Canvas(root, width=800, height=600)
canvas.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
canvas.pack()

root.mainloop()