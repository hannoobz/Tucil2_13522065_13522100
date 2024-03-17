from PointListClass import *

import sys
sys.setrecursionlimit(2**31-1)

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
        result.uniquepushback(temp.head)
        bezierDivConquer(result,late,iter,curr+1)
    else:
        result.uniquepushfront(line.head)
        result.pushback(line.tailElement())