class Stack:
    def __init__(self):
        self.st=[]
    def isEmpty(self):
        if self.st==[]:
            return True
        else:
            return False
    def push(self,x):
        self.st.append(x)
    def POP(self):
        if self.isEmpty():
            return -1
        else:
            popped=self.st.pop()
            return popped
    def Peek(self):
        if self.isEmpty():
            return -1
        else:
            return self.st[-1]
    def display(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            for i in range(len(self.st)-1,-1,-1):
                print(self.st[i])
                print('--------')
            print()
    def search(self,target):
        if self.isEmpty():
            print("stack is empty")
        else:
            for i in range(len(self.st)-1,-1,-1):
                if self.st[i]==target:
                    print("found")
                    break
                else:
                    print("not found")
s1=Stack()
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
        res=s1.Peek()
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

            
