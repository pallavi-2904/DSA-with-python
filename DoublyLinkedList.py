class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertBegin(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
    def insertEnd(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.prev=self.tail
            self.tail.next=newNode
            self.tail=newNode
    def search(self,target):
        if self.head is None:
            print("SLL is empty")
        else:
            temp=self.head
            while temp:
                if temp.data==target:
                    print("found the target")
                    break
                else:
                    temp=temp.next
            else:
                print("not found")
    def delBegin(self):
        if self.head is None:
            print("DLL is empty")
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            self.head.prev=None
            del temp
    def delEnd(self):
        if self.head is None:
            print("DLL is empty")
        else:
            temp=self.tail
            self.tail=self.tail.prev
            temp.prev=None
            self.tail.next=None
            del temp   
    def length(self):
        c=0
        temp=self.head
        while temp:
            c+=1
            temp=temp.next
        print(c)
    def display(self):
        if self.head is None:
            print("DLL is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=' ')
                temp=temp.next
    def displayrev(self):
        if self.head is None:
            print("DLL is empty")
        else:
            temp=self.tail
            while temp:
                print(temp.data,end=' ')
                temp=temp.prev

dll=DoublyLinkedList()
dll.insertBegin(56)
dll.insertBegin(67)
dll.insertBegin(29)
dll.insertBegin(34)
dll.insertBegin(14)
dll.display()
print()
dll.insertEnd(37)
dll.insertEnd(73)
dll.display()
print()
dll.search(100)
dll.search(34)
dll.delBegin()
dll.display()
print()
dll.delEnd()
dll.display()
print()
dll.displayrev()
print()
dll.length()

    
            
            
    
    
        



