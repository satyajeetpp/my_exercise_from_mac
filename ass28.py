'''
c=['cat','mat','sat','rat','vat']
n=len(c)
r=[]
for i in range(n-1):   
    p=[]    
    for j in range(i+1,n):
        q=[]
        q.append(c[i])
        q.append(c[j])
        v=set(q)
        p.append(v)       
    r.append(p)
print(r)
'''
m=int(input(('enter first number ')))
n=int(input('enter second number '))
l=[m,n]
#l=[3462,8940]
y=[]
while l!=[1,1]:
    for e in range(2,max(l)+1):
        if l[0]%e==0 or l[1]%e==0:
            if l[0]%e==0 and l[1]%e==0:
                v=int(l[1]/e)
                r=int(l[0]/e)
                l.clear()
                l.append(v) 
                l.append(r)      
            elif l[0]%e!=0 :
                r=int(l[1]/e)
                del(l[1])
                l.append(r)
            else :#l[1]%e!=0:
                r=int(l[0]/e)
                del(l[0])
                l.append(r)
            y.append(e)
            break    
for z in y:
    r=z*r       
print(r,y)
