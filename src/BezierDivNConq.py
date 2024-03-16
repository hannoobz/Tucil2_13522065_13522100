from math import floor,ceil

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

import numpy as np
class Point:
    def __init__(self,x = 0,y = 0, next = None,chr = None ,chl = None):
        self.x = x if x is not None else 0
        self.y = y if y is not None else 0
        self.next = next if next is not None else None
    
    def copy(self):
        return Point(self.x,self.y)

    
class Line:
    def __init__(self):
        self.head = None
        self.child = None

    def pushback(self, a:Point):
        p = a.copy()
        if self.head is None:
            self.head = p
            return
        current_point = self.head
        while(current_point.next):
            current_point = current_point.next
        current_point.next = p

    def pushfront(self, a:Point):
        p = a.copy()
        if self.head is None:
            self.head = p
            return
        else:
            p.next = self.head
            self.head = p
    
    def insertAt(self,index, a:Point):
        p = a.copy()
        current_point = self.head
        id = 0
        if id==index:
            self.pushfront(p)
        else:
            while(current_point != None and id+1 != index):
                id += 1
                current_point = current_point.next
            if current_point != None :
                p.next = current_point.next
                current_point.next = p
            else:
                pass

    def indexElement(self,i):
        temp = self.head
        for j in range(i):
            temp = temp.next
        return Point(temp.x,temp.y)
    
    def tailElement(self):
        temp = self.head
        while(temp.next):
            temp = temp.next
        return Point(temp.x,temp.y)

    def lineLength(self):
        temp = self.head
        count = 0
        while (temp):
            count +=1
            temp = temp.next
        return count
    


def midpoint(p1:Point, p2:Point):
    return Point(((p1.x+p2.x)/2),((p1.y+p2.y)/2));

def splitter(line:Line):
    temp = line.head
    child = Line()
    while(temp.next):
        child.pushback(midpoint(temp,temp.next))
        temp = temp.next
    line.child = child

def lineMidPoint(line:Line):
    temp = line
    length = temp.lineLength()
    for i in range(length-1):
        splitter(temp)
        temp = temp.child

def bezierDivConquer(result:Line,line:Line,iter,curr):
    if iter>curr:
        temp = line
        lineMidPoint(temp)
        early = Line()
        late = Line()
        while(temp.child):
            early.pushback(temp.head)
            late.pushfront(temp.tailElement())
            temp = temp.child
        early.pushback(temp.head)
        late.pushfront(temp.head)
        bezierDivConquer(result,early,iter,curr+1)
        result.pushback(temp.head)
        bezierDivConquer(result,late,iter,curr+1)
    else:
        result.pushfront(line.head)
        result.pushback(line.tailElement())

def recursive_print(start:Point):
    if start is not None:
        print((start.x,start.y))
        recursive_print(start.next)
    else:
        pass


import tkinter
root = tkinter.Tk()
canvas = tkinter.Canvas(root)
canvas.pack()

def recursive_draw(start,color):
    if start.next!=None:
        canvas.create_line(start.x,start.y,start.next.x,start.next.y, fill=color, width=3)
        recursive_draw(start.next,color)
    else:
        pass

P0 = Point (10,200)
P1 = Point (10,20)
P2 = Point (200,20)
P3 = Point (200,200)
P4 = Point (300,200)
P5 = Point (300,10)
        
            
lines = Line()
lines.pushback(P0)
lines.pushback(P1)
lines.pushback(P2) 
lines.pushback(P3) 
lines.pushback(P4)
lines.pushback(P5) 


# recursive_print(lines.child.child.child.head)

rez = Line()
bezierDivConquer(rez,lines,8,0)
# bezier3(P0,P1,P2,3,0)

# recursive_draw(anu.head)
recursive_draw(rez.head,"red")
# recursive_draw(lines.head,"green")


root.mainloop()