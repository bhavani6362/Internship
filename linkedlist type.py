class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=newNode
    def insert_at_beginning(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
    def insert_at_position(self,data,position):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        elif position == 1:
            newNode.next=self.head
            self.head=newNode
        else:
            current=self.head
            count=0
            while current:
                count+=1
                if count == position-1:
                    newNode.next=current.next
                    current.next=newNode
                    break
                current=current.next
            if count < position-1:
                self.insert_at_end(data)



            elif self.head.data==data:
                self.delete_at_beginning()
            else:
                current=self.head
                count=0
                while current.next:
                    if current.next.data==data:
                        count=count+1
                        current.next=current.next.next
                        break
                    current=current.next
                if count==0:
                    print("no data found")
    def search(self,key):
        current=self.head
        count=0
        while current:
            count=count+1
            if current.data==key:
                print("data found at position",count)
                count = -1
                break
            current=current.next
        if count!=-1:
            print("data not found")


obj=linkedlist()
obj.insert_at_beginning(5)
obj.insert_at_beginning(8)
obj.insert_at_beginning(7)
obj.insert_at_beginning(3)
obj.search(5)



class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=newNode
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
obj=linkedlist()
obj.insert_at_end(5)
obj.insert_at_end(6)
obj.insert_at_end(2)
obj.display()

