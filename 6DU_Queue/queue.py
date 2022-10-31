class Queue:
    def __init__(self, maxsize=10):
        self.head = None
        self.tail = None
        self.maxsize = maxsize
    
    def put(self, data):
        # put data in a queue
        New_Node = Node()
        New_Node.data = data
        New_Node.previous = None
        New_Node.next = None
        
        if self.size() == self.maxsize:
            print("queue is full")
        
        if self.size() >= 1 and self.size() < self.maxsize :
            New_Node.previous = self.tail
            self.tail.next = New_Node
            self.tail = self.tail.next
        
        if self.size() == 0:
            self.head=New_Node
            self.tail=New_Node
            New_Node.previous = None
            New_Node.next = None

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
        return size
        
    def printWholeQueue(self):
        start_head = self.head
        print("\----------",end=' ')
        while start_head != None:
            print(start_head.data,end=' ')
            start_head = start_head.next
        print("----------/")    
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None
        
queue = Queue(maxsize=3) 

print("---Test Case put expected to print abc---")
queue.put("a")
print(queue.get())
queue.put("b")
print(queue.get())
queue.put("c")
print(queue.get())

print("\n\n---Test Case: size expected to print 3---")
queue.put("a")
queue.put("b")
queue.put("c")
print(queue.size())

print("\n\n---Test Case: get expected to print 32100---")
print(queue.size())
queue.get()
print(queue.size())
queue.get()
print(queue.size())
queue.get()
print(queue.size())
queue.get()
print(queue.size())

print("\n\n---Test Case: empty expected to print True---")
print(queue.empty())

print("\n\n---Test Case: get 1 element from queue of size 2---")
queue.printWholeQueue()
queue.put("a")
queue.printWholeQueue()
queue.put("b")
queue.printWholeQueue()
queue.get()
queue.printWholeQueue()
print('size is:',queue.size())
print('head is:',queue.head.data,',tail is:', queue.tail.data)

print("\n\n---Test Case: empty expected to print False---")
print(queue.empty())

print("\n\n---Test Case: full expected to print False---")
print(queue.full())

print("\n\n---Test Case: full expected to print True---")
queue.put("a")
queue.put("b")
queue.put("d") 
print(queue.full())