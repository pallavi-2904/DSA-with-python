class queue:
    def __init__(self):
        self.qu=[]
    def isEmpty(self):
        if self.qu==[]:
            return True
        else:
            return False
    def Enqueue(self,x):
        self.qu.append(x)
    def Dequeue(self):
        if self.isEmpty():
            return -1
        else:
            popped=self.qu.pop(0)
            return popped
    def peek(self):
        if self.isEmpty():
            return -1
        else:
            return self.qu[0]
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            for i in range(len(self.qu)):
                print(self.qu[i])
                print('------')
            print()
    def search(self,target):
        if self.isEmpty():
            return -1
        else:
            for i in range(len(self.qu)):
                if self.qu[i]==target:
                    print("found")
                    break
            else:
                print("not found")
q1=queue()
while True:
    print('---operations---')
    print('1.ENQUEUE')
    print('2.DEQUEUE')
    print('3.PEEK')
    print('4.SEARCH')
    print('5.DISPLAY')
    print('6.EXIT')
    option=int(input("Enter operation"))
    if option==1:
        ele=int(input("Enter ele: "))
        q1.Enqueue(ele)
    elif option==2:
        res=q1.Dequeue()
        if res!=-1:
            print(f'popped:{res}')
        else:
            print("underflow")
    elif option==3:
        res=q1.peek()
        if res==-1:
            print("underflow")
        else:
            print(f'top ele is:{res}')
    elif option==4:
        target=int(input("Enter the ele: "))
        q1.search(target)
    elif option==5:
        q1.display()
    elif option==6:
        break
    else:
        print("Enter the valid option")

            


            


            
