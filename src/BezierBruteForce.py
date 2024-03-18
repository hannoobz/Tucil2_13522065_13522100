from PointListClass import *

def binomialCoeff(n,k):
    if k==0:
        return 1
    if n==k:
        return 1
    else:
        return binomialCoeff(n-1,k-1)+binomialCoeff(n-1,k)
    

def BezierBruteForce(t:float,result:Line,line:Line):
    temp = line.head
    n = line.length
    tNew = 0;
    while tNew<=1:
        px = 0
        py = 0
        for i in range(n):
            bez = ((1-tNew)**(n-i-1))*(tNew**i)*binomialCoeff(n-1,i)
            px += temp.x*bez
            py += temp.y*bez
            temp = temp.next
        temp = line.head
        result.pushback(Point(px,py))
        tNew += t
    result.pushback(line.tail)