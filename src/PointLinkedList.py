from math import ceil,floor

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


def recursive_print(start):
    if start.next is not None:
        print(start.x,start.y,start.next.x,start.next.y)
        print(start.level)
        recursive_print(start.next)
    else:
        pass


# root = tkinter.Tk()
# canvas = tkinter.Canvas(root)
# canvas.pack()

def recursive_draw(start):
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
        
        result1 = bezierInterpolate(temp1)
        result2 = bezierInterpolate(temp2)
        temp3 = Line()

        temp = result1.head
        while(temp.next):
            temp3.pushback(temp.x,temp.y,temp.level)
            temp = temp.next
            if temp.next is None:
                lev = max(temp.level,result2.head.level)
                mid_temp = midpoint(temp,result2.head)

        temp = result2.head
        while(temp):
            temp3.pushback(temp.x,temp.y,temp.level)
            temp = temp.next
        
        return temp3



lines = Line()
lines.head = Point(5,10)
lines.pushback(5,200)
lines.pushback(110,200)
lines.pushback(150,350)
# print
# lines.insertAt(1,150,150)
bejir = bezierCurve(lines,2)
# print(bejir)

# recursive_print(lines.head)
recursive_print(bejir.head)

print("PASS")

# print(midpoint(lines.head,lines.head.next,max(lines.head.level,lines.head.next.level)).level)
# root.mainloop()
