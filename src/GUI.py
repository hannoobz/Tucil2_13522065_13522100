import tkinter as tk
import timeit
from tkinter import ttk
from BezierBruteForce import *
from BezierDivideAndConquer import *   
from random import randint

import sys
sys.setrecursionlimit(2**31-1)

class MainWindow(tk.Frame):
    def __init__(self ,parent):
        tk.Frame.__init__(self,parent)
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()
        self.createGrid()
        self.points = Line()
        self._drag_data = {"x": 0, "y": 0, "item": None}
        self.canvas.tag_bind("token","<ButtonPress-1>", self.drag_start)
        self.canvas.tag_bind("token", "<ButtonRelease-1>", self.drag_stop)
        self.canvas.tag_bind("token", "<B1-Motion>", self.drag)
        self.canvas.bind("<Double-1>", self.addControlPoint)
        self.labelObjArray = []
        self.labelObjArrayID = []
        self.availablePoint = ()
        self.pointDictionary = {}
        self.inversePointDictionary = {}
        self.selectedPoint = tk.StringVar()
        self.useBruteForce = tk.IntVar()
        self.iterations = tk.StringVar()
        self.increment = tk.StringVar()
        self.pointX = tk.StringVar()
        self.pointY = tk.StringVar()
        self.iterations.set(str(6))
        self.increment.set(str(0.02))
        self.dontClearLinesGetter = tk.IntVar()
        self.color = ["red","orange","yellow","green","blue","purple","cyan","brown","gold"]
        self.dontClearLinesVal = False


        self.frame = tk.LabelFrame(root, text='Options', padx=10, pady=5)
        self.frame.place(in_=self.canvas, relx=1, rely=0, anchor='ne')
        self.label = tk.Label(self.frame, text='Iterations: ')
        self.label.pack()
        self.spinbox = tk.Spinbox(self.frame, command=self.redrawCurve, from_=0, to=12, textvariable=self.iterations, width=8, wrap=True)
        self.spinbox.bind("<Return>", self.updatespinbox)
        self.spinbox.pack()
        self.pointChosenLabel = ttk.Label(self.frame,text="Control Point :")
        self.pointChosenLabel.pack()
        self.pointChosen = ttk.Combobox(self.frame,width=5,textvariable=self.selectedPoint)
        self.pointChosen.pack()
        self.pointChosen.bind("<<ComboboxSelected>>",self.updateSelectedPoint)
        self.coordinateLabel = tk.Label(self.frame,text="XY Coordinate: ")
        self.coordinateLabel.pack()
        self.pointXBox = tk.Spinbox(self.frame,width=5,textvariable=self.pointX,from_=0,to=800)
        self.pointYBox = tk.Spinbox(self.frame,width=5,textvariable=self.pointY,from_=0,to=600)
        self.pointXBox.pack()
        self.pointYBox.pack()
        self.pointXBox.bind("<Return>", self.updateCoordinateBySpinbox)
        self.pointXBox.bind("<Button-1>", self.updateCoordinateBySpinbox)
        self.pointYBox.bind("<Return>", self.updateCoordinateBySpinbox)
        self.pointYBox.bind("<Button-1>", self.updateCoordinateBySpinbox)
        self.bruteForceCheckBox = tk.Checkbutton(self.frame,text='Use Brute Force?',variable=self.useBruteForce,onvalue=1, offvalue=0, command=self.bruteForceToggle)
        self.bruteForceCheckBox.pack()
        self.dontClearLinesCheckBox = tk.Checkbutton(self.frame,text='Keep Previous Iteration?',variable=self.dontClearLinesGetter,onvalue=1, offvalue=0, command=self.dontClearLinesToggle)
        self.dontClearLinesCheckBox.pack()
        self.labelPointHeader = tk.Label(self.frame, text='Points: ')
        self.labelPointHeader.pack()
        self.currentPoints = 0
        self.labelPoint = tk.Label(self.frame, text=str(self.currentPoints))
        self.labelPoint.pack()
        self.labelTimer = tk.Label(self.frame, text='Runtime: ')
        self.labelTimer.pack()
        self.labelTime = tk.Label(self.frame, text=str(0))
        self.labelTime.pack()
        self.resetButton = tk.Button(self.frame, text='Reset', command=self.resetCurve)
        self.resetButton.pack()

    
    def createGrid(self):
        for i in range(0, 800, 25):
            self.canvas.create_line([(i, 0), (i, 600)], tag='grid_line',width=1,fill="#bfbfbf")
        for i in range(0, 600, 25):
            self.canvas.create_line([(0, i), (800, i)], tag='grid_line',width=1,fill="#bfbfbf")

    def updatespinbox(self,placeholder):
        #Nothing
        self.redrawCurve()

    def updateSelectedPoint(self,placeholder):
        selectedPoint = self.pointDictionary[int(self.selectedPoint.get())]
        point = self.getPointByID(self.points.head,selectedPoint)
        self.pointX.set(point.x)
        self.pointY.set(point.y)

    def updateCoordinateBySpinbox(self,placeholder):
        selectedPoint = self.pointDictionary[int(self.selectedPoint.get())]
        self.setCoordinateByID(self.points.head,selectedPoint,float(self.pointX.get()),float(self.pointY.get()))
        currTextObj = self.labelObjArray[self.labelObjArrayID.index(selectedPoint)]
        self.canvas.itemconfig(currTextObj, text=f"({self.pointX.get()}, {self.pointY.get()})")
        self.canvas.moveto(currTextObj, float(self.pointX.get())-50, float(self.pointY.get())-33)
        self.canvas.moveto(selectedPoint,float(self.pointX.get())-11.5,float(self.pointY.get())-11.5)
        self.redrawCurve()

    def bruteForceToggle(self):
        if self.useBruteForce.get():
            self.label.configure(text="Increment: ")
            self.spinbox.configure(command=self.redrawCurve, from_=0.0001, to=1,increment=0.0001, textvariable=self.increment, width=8, wrap=True)
        else:
            self.label.configure(text='Iterations: ')
            self.spinbox.configure(command=self.redrawCurve, from_=int(0), to=int(12),increment=1,textvariable=self.iterations, width=8, wrap=True)
        try:
            self.redrawCurve()
        except:
            pass

    def dontClearLinesToggle(self):
        if self.dontClearLinesGetter.get():
            self.dontClearLinesVal = True
        else:
            self.dontClearLinesVal = False
        self.redrawCurve()


    def getPointMapID(self,point,mapped):
        if point is None:
            return None
        if self.pointDictionary[mapped] == point.id:
            return point
        else:
            return self.getPointMapID(point.next,mapped)
        
    def setXandYfromSpinbox(self):
        mapped = int(self.selectedPoint.get())
        point = self.getPointMapID(self.points.head,mapped)
        self.pointX.set(point.x)
        self.pointY.set(point.y)


    def drag_start(self, event):
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y
        self.selectedPoint.set(self.inversePointDictionary[int(self._drag_data["item"])])
        self.pointX.set(event.x)
        self.pointY.set(event.y)

    def drag(self, event):
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)

        currTextObj = self.labelObjArray[self.labelObjArrayID.index(self._drag_data["item"])]
        self.canvas.move(currTextObj, delta_x, delta_y)
        
        self.canvas.itemconfig(currTextObj, text=f"({self._drag_data['x']}, {self._drag_data['y']})")

        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

        self.pointX.set(event.x)
        self.pointY.set(event.y)

    def drag_stop(self, event):
        self.setCoordinateByID(self.points.head,int(self._drag_data["item"]),self._drag_data["x"],self._drag_data["y"])
        currTextObj = self.labelObjArray[self.labelObjArrayID.index(self._drag_data["item"])]
        self.canvas.itemconfig(currTextObj, text=f"({self._drag_data['x']}, {self._drag_data['y']})")
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0
        self.pointX.set(event.x)
        self.pointY.set(event.y)
        self.canvas.delete("line")
        self.canvas.delete("dashline")
        self.redrawCurve()

    def setCoordinateByID(self, point : Point, id : int,x,y):
        if point.id==id:
            point.x = x
            point.y = y
            return
        if point!=None:
            self.setCoordinateByID(point.next,id,x,y)

    def getPointByID(self,point : Point, ID : int):
        if point.id==ID:
            return point
        if point!=None:
            return self.getPointByID(point.next,ID)
        
    def recursive_draw(self,start,dashed,color):
        if start.next!=None:
            if(dashed):
                line = self.canvas.create_line(start.x,start.y,start.next.x,start.next.y, fill=color, width=3, tags="dashline", dash=(5,1))
            else:
                line = self.canvas.create_line(start.x,start.y,start.next.x,start.next.y, fill=color, width=3, tags="line")
            self.canvas.tag_lower(line)
            self.canvas.tag_lower("grid_line")
            self.recursive_draw(start.next,dashed,color)
        else:
            pass

    def recursive_print(self,start):
        if start!=None:
            print(start.x,start.y)
            self.recursive_print(start.next)
        else:
            pass
        
    def comboboxPoint(self,point,start,val):
        if point is not None:
            val += (str(start),)
            return self.comboboxPoint(point.next,start+1,val)
        else:
            return val
        
    def addPointDictionary(self,point,start,val):
        if point is not None:
            val[start] = point.id
            return self.addPointDictionary(point.next,start+1,val)
        else:
            return val


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
        self.availablePoint = ()
        self.availablePoint = self.comboboxPoint(self.points.head,0,self.availablePoint)
        self.pointDictionary = {}
        self.pointDictionary = self.addPointDictionary(self.points.head,0,self.pointDictionary)
        self.inversePointDictionary = {val: key for key, val in self.pointDictionary.items()}
        self.pointChosen["values"] = self.availablePoint
        self.selectedPoint.set(self.inversePointDictionary[int(self.canvas.find_closest(event.x, event.y)[0])])
        self.pointX.set(event.x)
        self.pointY.set(event.y)
        self.canvas.delete("line")
        self.redrawCurve()

    def redrawCurve(self):
        bezier = Line()
        if self.useBruteForce.get():
            s = timeit.default_timer()
            t = float(self.increment.get())
            if t>0:
                BezierBruteForce(t,bezier,self.points)
                time = timeit.default_timer() - s
                self.currentPoints = bezier.length
        else:
            t = int(self.iterations.get())
            if type(t) is int and t>=0:
                s = timeit.default_timer()
                bezierDivConquer(bezier,self.points,t,0)
                time = timeit.default_timer() - s

        self.currentPoints = bezier.length
        if self.dontClearLinesVal==True:
            self.canvas.delete("dashline")
            color= self.color[randint(0,len(self.color)-1)]
            self.recursive_draw(bezier.head,0,color)
            pass
        else:
            self.canvas.delete("line")
            self.canvas.delete("dashline")
            self.recursive_draw(bezier.head,0,"black")

        self.recursive_draw(self.points.head,1,"gray")
        self.labelPoint.configure(text=str(self.currentPoints))
        self.labelTime.configure(text=str(round(time,5))+'s')

    def resetCurve(self):
        self.points = Line()
        self.canvas.delete("all")
        self.createGrid()
        self.currentPoints = 0
        self.labelObjArray = []
        self.labelObjArrayID = []
        self.availablePoint = ()
        self.pointDictionary = {}
        self.pointChosen["values"] = self.availablePoint
        self.labelPoint.configure(text=str(self.currentPoints))
        
if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(fill="both", expand=True)
    root.title('Bezier Curve Simulation with Divide and Conquer')
    root.maxsize(800,600)
    root.minsize(800,600)
    root.mainloop()
