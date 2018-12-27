from sys import stdout
k = [-1]*(100000 + 1)
o = [-1]*(100000 + 1)
oop = [0]*(1000 + 1)

c = input().split()
n = int(c[0])
m = int(c[1])

for i in range(m):
    j = input().split()
    k[i] = int(j[0])
    o[i] = int(j[1])

subject = input().split()
for i in range(n):
    oop[int (subject[i])] = i+1# have to be int to prevent error at test 15
    #1 2 4 5 3 = 2 4 5 3 null
boolean = True
for i in range(m):
    if oop[k[i]] > oop[o[i]]:
        # if the index visited is more then the index to be visited mark it as correct
        boolean = False
        break
        

if  boolean==True:# visited according to sequence
    stdout.write("YES")
else:
    stdout.write("NO")# visited not similar to the sequence

