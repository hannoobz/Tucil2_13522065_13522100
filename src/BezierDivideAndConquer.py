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
    length = temp.length
    for i in range(length-1):
        splitter(temp)
        temp = temp.child

def bezierDivConquer(result:Line,line:Line,iter : int, curr : int, rec : int):
    if iter>curr:
        temp = line
        lineMidPoint(temp)
        early = Line()
        late = Line()
        while(temp.child):
            early.pushback(temp.head)
            late.pushfront(temp.tail)
            temp = temp.child
        early.pushback(temp.head)
        late.pushfront(temp.head)
        rec +=bezierDivConquer(result,early,iter,curr+1,rec+1)
        result.pushback(temp.head)
        rec +=bezierDivConquer(result,late,iter,curr+1,rec+1)
        return rec
    else:
        result.pushfront(line.head)
        result.pushback(line.tail)
        return rec