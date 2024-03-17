import tkinter as tk
import timeit
from tkinter import ttk
from BezierBruteForce import *
from BezierDivideAndConquer import *   

import sys
sys.setrecursionlimit(2**31-1)

class MainWindow(tk.Frame):
    def __init__(self ,parent):
        tk.Frame.__init__(self,parent)
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()
        self.points = Line()
        self._drag_data = {"x": 0, "y": 0, "item": None}
        self.canvas.tag_bind("token","<ButtonPress-1>", self.drag_start)
        self.canvas.tag_bind("token", "<ButtonRelease-1>", self.drag_stop)
        self.canvas.tag_bind("token", "<B1-Motion>", self.drag)
        self.canvas.bind("<Double-1>", self.addControlPoint)
        self.labelObjArray = []
        self.labelObjArrayID = []

        self.frame = tk.LabelFrame(root, text='Options', padx=10, pady=5)
        self.frame.place(in_=self.canvas, relx=1, rely=0, anchor='ne')
        self.label = tk.Label(self.frame, text='Iterations: ')
        self.label.pack()
        self.iterations = tk.StringVar()
        self.spinbox = tk.Spinbox(self.frame, command=self.redrawCurve, from_=1.0, to=12.0, textvariable=self.iterations, width=8, wrap=True)
        self.spinbox.pack()
        self.resetButton = tk.Button(self.frame, text='Reset', command=self.resetCurve)
        self.resetButton.pack()
        self.labelPointHeader = tk.Label(self.frame, text='Points: ')
        self.labelPointHeader.pack()
        self.currentPoints = 0
        self.labelPoint = tk.Label(self.frame, text=str(self.currentPoints))
        self.labelPoint.pack()
        self.labelTimer = tk.Label(self.frame, text='Runtime: ')
        self.labelTimer.pack()
        self.labelTime = tk.Label(self.frame, text=str(0))
        self.labelTime.pack()


    def drag_start(self, event):
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def drag(self, event):
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)

        currTextObj = self.labelObjArray[self.labelObjArrayID.index(self._drag_data["item"])]
        self.canvas.move(currTextObj, delta_x, delta_y)
        
        self.canvas.itemconfig(currTextObj, text=f"({self._drag_data['x']}, {self._drag_data['y']})")

        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def drag_stop(self, event):
        self.setCoordinateByID(self.points.head,int(self._drag_data["item"]))
        currTextObj = self.labelObjArray[self.labelObjArrayID.index(self._drag_data["item"])]
        self.canvas.itemconfig(currTextObj, text=f"({self._drag_data['x']}, {self._drag_data['y']})")
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

        self.redrawCurve()

    def setCoordinateByID(self, point : Point, id : int):
        if point.id==id:
            point.x = self._drag_data["x"]
            point.y = self._drag_data["y"]
            return
        if point!=None:
            self.setCoordinateByID(point.next,id)

    def getValueByID(self,point : Point, ID : int):
        if point.id==id:
            return point
        if point!=None:
            self.getValueByID(point.next,ID)
        
    def recursive_draw(self,start,dashed,color):
        if start.next!=None:
            if(dashed):
                line = self.canvas.create_line(start.x,start.y,start.next.x,start.next.y, fill=color, width=3, tags="line", dash=(20,20))
                
            else:
                line = self.canvas.create_line(start.x,start.y,start.next.x,start.next.y, fill=color, width=3, tags="line")
            self.canvas.tag_lower(line)
            self.recursive_draw(start.next,dashed,color)
        else:
            pass

    def recursive_print(self,start):
        if start!=None:
            print(start.x,start.y)
            self.recursive_print(start.next)
        else:
            pass
        
    def key(self,event):
        print ("pressed", repr(event.char))

    def addControlPoint(self,event):
        self.canvas.create_oval(
            event.x - 10,
            event.y - 10,
            event.x + 10,
            event.y + 10,
            outline='red',
            width=2,
            fill='red',
            tags=("token",),
        )
        newPointLabel = self.canvas.create_text(event.x - 20, event.y - 25, text=f"({event.x}, {event.y})", anchor='center')
        self.labelObjArray.append(newPointLabel)
        self.labelObjArrayID.append(int(self.canvas.find_closest(event.x, event.y)[0]))
        pp = Point(event.x,event.y,None,None,int(self.canvas.find_closest(event.x, event.y)[0]))
        self.points.pushback(pp)
        self.redrawCurve()

    def redrawCurve(self):
        bezier = Line()
        s = timeit.default_timer()
        bezierDivConquer(bezier,self.points,int(self.iterations.get()),0)
        # BezierBruteForce(0.001,bezier,self.points)
        time = timeit.default_timer() - s

        self.canvas.delete("line")
        self.recursive_draw(bezier.head,0,"black")
        self.recursive_draw(self.points.head,1,"black")
        self.currentPoints = (2**int(self.iterations.get()))+1
        self.labelPoint.configure(text=str(self.currentPoints))
        self.labelTime.configure(text=str(round(time,5))+'s')

    def resetCurve(self):
        self.points = Line()
        self.canvas.delete('all')
        self.currentPoints = 0
        self.labelPoint.configure(text=str(self.currentPoints))
        
if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(fill="both", expand=True)
    root.title('Bezier Curve Simulation with Divide and Conquer')
    root.mainloop()
