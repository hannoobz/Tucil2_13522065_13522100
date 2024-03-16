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