import matplotlib.pyplot as plt
import numpy as np
from PointListClass import *
    
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

