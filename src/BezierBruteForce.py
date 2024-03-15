import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self,x = 0,y = 0, next = None):
        self.x = x if x is not None else 0
        self.y = y if y is not None else 0
        self.next = next if next is not None else None
        
class Line:
    def __init__(self):
        self.head = None

    def pushback(self, p:Point):
        if self.head is None:
            self.head = p
            return
        current_point = self.head
        while(current_point.next):
            current_point = current_point.next
        current_point.next = p

    def pushfront(self, p:Point):
        if self.head is None:
            self.head = p
            return
        else:
            p.next = self.head
            self.head = p
    
    def insertAt(self,index, p:Point):
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

    def lineLength(self):
        temp = self.head
        count = 0
        while (temp):
            count +=1
            temp = temp.next
        return count
    
def recursive_draw(start:Point):
    if start.next is not None:
        plt.plot((start.x,start.next.x),(start.y,start.next.y), marker = 'o')
        recursive_draw(start.next)
    else:
        pass
    
def Bt(P0:Point, P1:Point, t):
    new_point = Point(0,0)
    new_point.x = (1-t)*P0.x + t*P1.x
    new_point.y = (1-t)*P0.y + t*P1.y
    return new_point

def R0(P0:Point, P1:Point, P2:Point, t):
    Q0 = Bt(P0, P1, t)
    Q1 = Bt(P1, P2, t)
    return Bt(Q0, Q1, t)

#Create points incremented by t, until tNew > 1:
def BezierBruteForce(t, line:Line, P0:Point, P1:Point, P2:Point):
    tNew = 0
    while tNew <= 1:
        line.pushback(R0(P0, P1, P2, tNew))
        tNew += t

P0 = Point (20,20)
P1 = Point (80,110)
P2 = Point (140,20)

lines = Line()
lines.pushback(P0)
lines.pushback(P1)
lines.pushback(P2)
BezierBruteForce(0.1, lines, P0, P1, P2)

recursive_draw(lines.head)
plt.show()