import tkinter as tk
from BezierDivideAndConquer import *        

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
        self.frame = tk.LabelFrame(root, text='Options', padx=10, pady=5)
        self.frame.place(in_=self.canvas, relx=1, rely=0, anchor='ne')
        self.label = tk.Label(self.frame, text='Iterations: ')
        self.label.pack()
        self.iterations = tk.StringVar()
        self.spinbox = tk.Spinbox(self.frame, command=self.redrawCurve, from_=1.0, to=12.0, textvariable=self.iterations, width=8, wrap=True)
        self.spinbox.pack()
        self.resetButton = tk.Button(self.frame, text='Reset', command=self.resetCurve)
        self.resetButton.pack()

    def drag_start(self, event):
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def drag(self, event):
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def drag_stop(self, event):
        self.id_finder(self.points.head,int(self._drag_data["item"]))
        self.recursive_print(self.points.head)
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0
        self.redrawCurve()

    def id_finder(self, point : Point, id : int):
        if point.id==id:
            point.x = self._drag_data["x"]
            point.y = self._drag_data["y"]
            return
        if point!=None:
            print(point.id)
            self.id_finder(point.next,id)
        
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
        ctrlOval = self.canvas.create_oval(
            event.x - 10,
            event.y - 10,
            event.x + 10,
            event.y + 10,
            outline='red',
            width=2,
            fill='red',
            tags=("token",),
        )
        pp = Point(event.x,event.y,None,int(self.canvas.find_closest(event.x, event.y)[0]))
        print ("added at", pp.x, pp.y,pp.id)
        self.points.pushback(pp)
        self.redrawCurve()
        
    def redrawCurve(self):
        bezier = Line()
        bezierDivConquer(bezier,self.points,int(self.iterations.get()),0)
        self.canvas.delete("line")
        self.recursive_draw(bezier.head,0,"black")
        self.recursive_draw(self.points.head,1,"black")

    def resetCurve(self):
        self.points = Line()
        self.canvas.delete('all')
        
if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(fill="both", expand=True)
    root.title('Bezier Curve Simulation with Divide and Conquer')
    root.mainloop()
