
from math import floor,ceil

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

import numpy as np
class Point:
    def __init__(self,x = 0,y = 0, next = None):
        self.x = x if x is not None else 0
        self.y = y if y is not None else 0
        self.next = next if next is not None else None
    
    def copy(self):
        return Point(self.x,self.y)
    
class Line:
    def __init__(self):
        self.head = None

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

    def lineLength(self):
        temp = self.head
        count = 0
        while (temp):
            count +=1
            temp = temp.next
        return count
    



def midpoint(p1:Point, p2:Point):
    return Point(((p1.x+p2.x)/2),((p1.y+p2.y)/2));

def lineMidPointHelper(line:Line):
    if line.lineLength()==1:
        retval = Line();
        retval.pushback(line.head);
        retval.head.next = None;
        return retval;
    elif line.lineLength()==2:
        retval = Line()
        mid = midpoint(line.head,line.head.next);
        retval.pushback(line.head);
        retval.pushback(mid);
        retval.pushback(line.head.next);
        return retval;
    else:
        split1 = Line()
        split2 = Line()
        temp = line.head
        for i in range(ceil(line.lineLength()/2)):
            split1.pushback(temp);
            temp = temp.next;
        for i in range (floor(line.lineLength()/2)):
            split2.pushback(temp);
            temp = temp.next;
        
        split1 = lineMidPointHelper(split1);
        split2 = lineMidPointHelper(split2);
        temp = split1.head
        retval = Line()
        while(temp.next):
            retval.pushback(temp)
            temp = temp.next
        retval.pushback(temp)
        retval.pushback(midpoint(temp,split2.head))
        temp = split2.head
        while(temp):
            retval.pushback(temp)
            temp = temp.next
        return retval
    
def cornerCutting(line:Line):
    temp = lineMidPointHelper(line).head
    retval = Line()
    retval.pushback(temp)
    i = 1
    while(temp.next):
        if i%2==0:
            retval.pushback(temp);
        temp = temp.next
        i +=1
    retval.pushback(temp)
    mid_index = int((retval.lineLength()/2))
    retval.insertAt(mid_index,midpoint(retval.indexElement(mid_index-1),retval.indexElement(mid_index)))
    return retval

def lineMidPoint(line:Line):
    length = line.lineLength()
    temp = line;
    for i in range(length-1):
        temp = cornerCutting(temp);
    return temp

def singleLineMidPoint(line:Line):
    temp = line.head
    length = line.lineLength()
    for i in range(floor(length/2)):
        temp = temp.next
    return temp.copy()


global anu 
anu = Line()
def bezier3(ctrl1,ctrl2,ctrl3,iter,curr):
    if(curr<iter):
        p1 = midpoint(ctrl1,ctrl2)
        p2 = midpoint(ctrl2,ctrl3)
        p3 = midpoint(p1,p2)
        curr +=1;
        print("CTRL POINT 3")
        print(ctrl1.x,ctrl1.y)
        print(p1.x,p1.y)
        print(p3.x,p3.y)
        print(p2.x,p2.y)
        print(ctrl3.x,ctrl3.y)
        print("=========")
        bezier3(ctrl1,p1,p3,iter,curr)
        anu.pushback(p3);
        bezier3(p3,p2,ctrl3,iter,curr)

def bezierDivConquer(result:Line,line:Line,iter,curr):
    if iter>curr:
        temp_line = cornerCutting(line)
        temp_el = temp_line.head
        early = Line()
        late = Line()
        for i in range(floor(temp_line.lineLength()/2)):
            early.pushback(temp_el)
            temp_el = temp_el.next
        mid = temp_el
        early.pushback(mid)
        while(temp_el):
            late.pushback(temp_el)
            temp_el = temp_el.next
        bezierDivConquer(result,early,iter,curr+1)
        result.pushback(mid)
        bezierDivConquer(result,late,iter,curr+1)



def recursive_print(start:Point):
    if start is not None:
        print((start.x,start.y))
        recursive_print(start.next)
    else:
        pass

def recursive_draw(start:Point):
    if start.next is not None:
        plt.plot((start.x,start.next.x),(start.y,start.next.y), marker = 'o')
        recursive_draw(start.next)
    else:
        pass


# anu = Line()
# def bezier3(inserted:Line,line:Line,iter,curr):
    




P0 = Point (20,20)
P1 = Point (80,110)
P2 = Point (140,20)
P3 = Point (190,25)
        
            
lines = Line()
lines.pushback(P0)
lines.pushback(P1)
lines.pushback(P2) 
lines.pushback(P3) 
# lines.pushback(P4)


# anu = lineMidPoint(lines)

bezier = Line()
bezierDivConquer(bezier,lines,7,0)
bezier3(P0,P1,P2,2,0)
ax = cornerCutting(lines)
recursive_print(ax.head)

# recursive_draw(anu.head)
recursive_draw(bezier.head)
# recursive_draw(lines.head)
# recursive_draw(anu.head)
# recursive_draw(bezier.head)



plt.show()