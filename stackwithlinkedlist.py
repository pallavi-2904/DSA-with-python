class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stackll:
    def __init__(self):
        self.top=None
    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False
    def push(self,data):
        newnode=Node(data)
        if self.top is None:
            self.top=newnode
        else:
            newnode.next=self.top
            self.top=newnode
    def POP(self):
        if self.isEmpty():
            return-1
        else:
            delnode=self.top
            popped=delnode.data
            self.top=self.top.next
            delnode.next=None
            del delnode
            return popped
    def peek(self):
        if self.isEmpty():
            print("st is Empty")
        else:
            return self.top.data
    def display(self):
        if self.isEmpty():
            print("st is Empty")
        else:
            temp=self.top
            while temp:
                print(temp.data)
                print('----')
                temp=temp.next
            print()
    def search(self,target):
        if self.isEmpty():
            print("st is Empty")
        else:
            temp=self.top
            while temp:
                if temp.data==target:
                    print("found")
                    break
                else:
                    temp=temp.next
            else:
                print("not found")
s1=stackll()
while True:
    print('---operations---')
    print('1.PUSH')
    print('2.POP')
    print('3.PEEK')
    print('4.SEARCH')
    print('5.DISPLAY')
    print('6.EXIT')
    option=int(input("Enter operation"))
    if option==1:
        ele=int(input("Enter ele: "))
        s1.push(ele)
    elif option==2:
        res=s1.POP()
        if res!=-1:
            print(f'popped:{res}')
        else:
            print("underflow")
    elif option==3:
        res=s1.peek()
        if res==-1:
            print("underflow")
        else:
            print(f'top ele is:{res}')
    elif option==4:
        target=int(input("Enter the ele: "))
        s1.search(target)
    elif option==5:
        s1.display()
    elif option==6:
        break
    else:
        print("Enter the valid option")

            


            
