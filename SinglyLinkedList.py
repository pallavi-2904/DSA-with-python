class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def insertBegin(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    def insertEnd(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newNode
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
            print("SLL is empty")
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            del temp
    def delEnd(self):
        if self.head is None:
            print("SLL is empty")
        else:
            temp=self.head
            while temp.next.next:
                temp=temp.next
            delNode=temp.next
            temp.next=None
            del delNode
    def length(self):
        c=0
        temp=self.head
        while temp:
            c+=1
            temp=temp.next
        print(c)
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
sll=SinglyLinkedList()
sll.insertBegin(10)
sll.insertBegin(20)
sll.insertBegin(30)
sll.insertBegin(40)
sll.insertBegin(50)
sll.display()
print()
sll.insertEnd(300)
sll.insertEnd(70)
sll.display()
print()
sll.search(100)
sll.search(300)
print()
sll.delBegin()
sll.display()
print()
sll.delEnd()
sll.display()
print()
sll.length()
    
            
            
    
    
        
