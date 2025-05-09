'''s='SATYAJEET MISHRA'
s.split(' ')
' '.join(s.split(' '))

k=input('enter comma separated numbers')
m=[int(e) for e in k.split(',')]
print(type(m[1]))


z='bunty'
k='{} guha khia'
print(k.format(z))


k=int(input('enter the number'))
if k<0:
    k=-k
print(len(str(k)))
'''

print(sum([int(i) for i in input('enter comma separated values').split(',')])) 