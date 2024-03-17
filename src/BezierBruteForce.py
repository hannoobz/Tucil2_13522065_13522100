from PointListClass import *


def binomialCoeff(n,k):
    if k==0:
        return 1
    if n==k:
        return 1
    else:
        return binomialCoeff(n-1,k-1)+binomialCoeff(n-1,k)
    

def BezierBruteForce(t,result:Line,line:Line):
    temp = line.head
    points = []
    while(temp):
        points.append(temp)
        temp = temp.next
    n = len(points)
    tNew = 0;
    while(tNew<=1):
        px = 0
        py = 0
        for i in range(len(points)):
                bez = (1-tNew)**(len(points)-i-1)*tNew**i
                bez = bez*binomialCoeff(n-1,i)
                px += points[i].x*bez
                py += points[i].y*bez
        result.pushback(Point(px,py))
        tNew += t;
