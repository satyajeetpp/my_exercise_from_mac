'''translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

s = "MCMXCIV"

r= [translations[e] for e in s[::-1] ]
total=sum(r)
print(r)
for k,v in  r:
    if r[k]>r[k+1] and k!=len(r)-1:
        total-r[k+1]*2
print(total)
'''
strs = ["flower","flow","flight"]
print(sorted(strs,key=len))
r=[]
for e in range(len(strs)):
    if strs[e][0]==