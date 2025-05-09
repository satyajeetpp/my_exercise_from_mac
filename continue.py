'''
print('Hello')
i=1
while i<=10:
    x=input('Enter Even numbers ')
    k=int(x)
    if k%2!=0:
        print('not a even number,please enter again')
        continue
    print(i,' even number =',x)
    i+=1
if i==11:
    print('you have successfully entered 10 even numbers')

class Test:
    def __init__(self,length) -> None:
        self.l=length
    def display(self):
        return  print(self.l)
    def __add__(self,other):
        return Test(self.l+other.l)
        

d=Test(2)
e=Test(4)
m=d+e

m.display()

x=12
def f():
    global x
    x=10
    print(x)
f()
print(x)

x=122

def f():
    x=10
    print(globals()['x'],x)

f()



from collections import *
print(Counter('abrakadabra'))
'''


class Solution:
    def isvalid(self,sides):
        for i in sides:
            if i>=sum(sides)-i:
                return False
        return True
    def perimeter(self,sides):
        if self.isvalid(sides):
            return sum(sides)
        return 'Not a valid polygon'