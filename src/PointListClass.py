class Point:
    def __init__(self,x = 0,y = 0, prev = None, next = None, id = None):
        self.x = x if x is not None else 0
        self.y = y if y is not None else 0
        self.prev = prev if prev is not None else None
        self.next = next if next is not None else None
        self.id = id if id is not None else None
    
    def copy(self):
        copy = Point(self.x,self.y)
        copy.next = self.next
        copy.prev = self.prev
        copy.id = self.id
        return copy

    
class Line:
    def __init__(self):
        self.head = None
        self.child = None
        self.tail = None
        self.length = 0

    def pushback(self, a:Point):
        p = a.copy()
        if not self.head:
            self.head = p
            self.tail = p
        else:
            p.prev = self.tail
            self.tail.next = p
            self.tail = p
        self.length += 1
        return self      
    
    def pushfront(self, a:Point):
        p = a.copy()
        if not self.head:
            self.head = p
            self.tail = p
        else:
            p.next = self.head
            self.head.prev = p
            self.head = p
        self.length += 1
        return self
