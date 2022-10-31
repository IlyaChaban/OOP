class Queue:
    def __init__(self, maxsize=10):
        self.head = None
        self.tail = None
        self.maxsize = maxsize
    
    def put(self, data):
        # put data in a queue
        prev_for_tail = self.tail
        if self.head == None:
            self.head = data
            self.tail = data #Ринат говорит что тэйла тут не будет
            
        elif self.full():
            print("Queue is Full")
            
        
        elif not self.full():
            self.tail.next = data
            self.tail = self.tail.next
            self.tail.previous = prev_for_tail
    
    def get(self):
        # get data from a queue
        if self.head == None:
            return None
            
        head_to_return = self.head
        
        if self.head.next == None:
            self.head = None
            self.tail = None
            return head_to_return.data
            
        if self.head.next != None:
            self.head = self.head.next
            self.head.previous = None
            head_to_return.next = None
            return head_to_return.data

    def empty(self):
        # is queue empty?
        return True if self.head == None and self.tail == None else False
   
    def full(self):
        # is queue full?
        return True if self.size() == self.maxsize else False
    
    def size(self):
        # what is the size of a queue?
        start_head = self.head
        size = 0
        
        if self.head == None:
            return size
            
        while start_head != None:
            size += 1 
            start_head = start_head.next
            print(size)
        return size
        
    def printWholeQueue(self):
        start_head = self.head
        print("----------")
        while start_head != None:
            print(start_head.data)
            start_head = start_head.next
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None
        
        
queue = Queue(maxsize = 3)

print("---Test Case put expected to print abc---")
Node1 = Node("a")
queue.put(Node1)
print(queue.get())


Node2 = Node("b")
queue.put(Node2)
print(queue.get())

Node3 = Node("c")
queue.put(Node3)
print(queue.get())


print("---Test Case size expected to print 3---")
queue.put(Node1)
queue.put(Node2)
queue.put(Node3)
print(queue.size())

print("---Test Case get expected to print 32100---")
print(queue.size())
queue.get()
print(queue.size())
queue.get()
print(queue.size())
queue.get()
print(queue.size())
queue.get()
print(queue.size())

print("---Test Case empty expected to print True---")
print(queue.empty())

print("---Test Case get 1 from 2---")
queue.printWholeQueue()
queue.put(Node1)
queue.printWholeQueue()
queue.put(Node2)
queue.printWholeQueue()
queue.get()
queue.printWholeQueue()
print(queue.size())
print(queue.head.data, queue.tail.data)

print("---Test Case empty expected to print False---")
print(queue.empty())

print("---Test Case full expected to print False---")
print(queue.full())

print("---Test Case full expected to print True---")
queue.put(Node1)
queue.put(Node2)
Node4 = Node("d")
queue.put(Node4) 