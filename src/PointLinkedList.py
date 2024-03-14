from math import ceil,floor
import tkinter

class Point:
    def __init__(self,x = 0,y = 0,level = None, next = None):
        self.x = x if x is not None else 0
        self.y = y if y is not None else 0
        self.level = level if level is not None else 0
        self.next = next if next is not None else None
        
class Line:
    def __init__(self):
        self.head = None

    def pushback(self, x, y, level = 0):
        new_point = Point(x,y,level)
        if self.head is None:
            self.head = new_point
            return
        current_point = self.head
        while(current_point.next):
            current_point = current_point.next
        current_point.next = new_point  

    def pushfront(self, x, y, level = 0):
        new_point = Point(x,y,level)
        if self.head is None:
            self.head = new_point
            return
        else:
            new_point.next = self.head
            self.head = new_point
    
    def insertAt(self,index,x,y,level = 0):
        new_point = Point(x,y,level)
        current_point = self.head
        id = 0
        if id==index:
            self.pushfront(x,y,level)
        else:
            while(current_point != None and id+1 != index):
                id += 1
                current_point = current_point.next
            if current_point != None :
                new_point.next = current_point.next
                current_point.next = new_point
            else:
                pass

    def lineLength(self):
        temp = self.head;
        count = 0;
        while (temp):
            count +=1;
            temp = temp.next;
        return count
            
        

def midpoint(p1,p2):
    return Point((p2.x+p1.x)/2,(p2.y+p1.y)/2,max(p1.level,p2.level)+1)


def recursive_print(start:Point):
    if start.next is not None:
        print(start.x,start.y,start.next.x,start.next.y)
        print(start.level)
        recursive_print(start.next)
    else:
        pass


# root = tkinter.Tk()
# canvas = tkinter.Canvas(root)
# canvas.pack()

def recursive_draw(start:Point):
    if start.next is not None:
        # canvas.create_line(start.x,start.y,start.next.x,start.next.y, fill="red", width=3)
        recursive_draw(start.next)
    else:
        pass

def bezierInterpolate(line:Line):
    if line.lineLength()==1:
        return line
    elif line.lineLength()==2:
        mid = midpoint(line.head,line.head.next)
        line.insertAt(1,mid.x,mid.y,mid.level)
        return line
    else:
        temp =  line.head
        temp1 =  Line()
        temp2 = Line()
        for i in range(int(ceil(line.lineLength()/2))):
            temp1.pushback(temp.x,temp.y,temp.level)
            temp = temp.next
        while(temp):
            temp2.pushback(temp.x,temp.y,temp.level)
            temp = temp.next
        
        print(temp2.lineLength(),temp2.head.x)
        result1 = bezierInterpolate(temp1)
        result2 = bezierInterpolate(temp2)
        recursive_print(result2.head)
        temp3 = Line()

        temp = result1.head
        while(temp.next):
            temp3.pushback(temp.x,temp.y,temp.level)
            temp = temp.next
            if temp.next is None:
                mid_temp = midpoint(temp,result2.head)
                temp3.pushback(mid_temp.x,mid_temp.y,mid_temp.level)

        temp = result2.head
        while(temp):
            temp3.pushback(temp.x,temp.y,temp.level)
            temp = temp.next
        
        return temp3

def bezierCurve(line:Line,iteration):
    setup = line
    for i in range(iteration):
        temp = Line()
        tempbezier = bezierInterpolate(setup)
        tempHead = tempbezier.head
        temp.pushback(tempHead.x,tempHead.y,0)
        while(tempHead.next):
            print("X")
            if(tempHead.level!=0):
                print("Y")
                temp.pushback(tempHead.x,tempHead.y,0)
            tempHead = tempHead.next
        temp.pushback(tempHead.x,tempHead.y,0)
        setup = temp
    return setup


root = tkinter.Tk()
canvas = tkinter.Canvas(root)
canvas.pack()

def recursive_draw(start:Point,color:str):
    if start.next is not None:
        canvas.create_line(start.x,start.y,start.next.x,start.next.y, fill=color, width=3)
        recursive_draw(start.next,color)
    else:
        pass

lines = Line()
lines.pushback(70,250)
lines.pushback(20,110)
lines.pushback(220,60)
# lines.pushback(200,200)
# print
# lines.insertAt(1,150),150)
# bejir = (bezierCurve(lines,1))
# print(bejir)

# recursive_print(lines.head)
print("PASS")
# recursive_print(bejir.head)



# recursive_draw(lines.head,'red')
# recursive_draw(bejir.head,'blue')

for i in range(0,50):
    recursive_draw(bezierCurve(lines,i).head,'red')

# print(midpoint(lines.head,lines.head.next,max(lines.head.level,lines.head.next.level)).level)
root.mainloop()
