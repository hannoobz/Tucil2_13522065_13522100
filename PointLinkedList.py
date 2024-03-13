class Point:
    def __init__(self,x = 0,y = 0,level = None, next = None):
        self.x = x if x is not None else 0
        self.y = y if y is not None else 0
        self.next = next if next is not None else None
        self.level = level if level is not None else 0


class PointLinkedList:
    def __init__(self):
        self.headval = None

    def pushback(self, x, y, level = None):
        new_point = Point(x,y,level)
        if self.head is None:
            self.head = new_point
            return
        current_point = self.head
        while(current_point.next):
            current_point = current_point.next
        current_point.next = new_point  

    def pushfront(self, x, y, level = None):
        new_point = Point(x,y,level)
        if self.head is None:
            self.head = new_point
            return
        else:
            new_point.next = self.head
            self.head = new_point


def midpoint(p1,p2):
    return Point((p2.x+p1.x)/2,(p2.y+p1.y)/2,p1,p1.level+1)


def recursive_print(start):
    print(repr(start))
    if start.next is not None:
        print(start.x,start.y,start.next.x,start.next.y)
        recursive_print(start.next)
    else:
        pass


# How to use :
# lines = PointLinkedList()
# lines.head = Point(5,10)
# lines.pushback(100,200)
# lines.pushback(150,200)
# lines.pushback(150,350)

# recursive_print(lines.head)

