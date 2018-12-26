
oop = [None]*(100000 + 1)
k = [None]*(100000 + 1)
o = [-1]*(1000 + 1)

c = input().split()
n = int(c[0])
m = int(c[1])

for i in range(m):
    j = input().split()
    k[i] = int(j[0])
    o[i] = int(j[1])

subject = list(map(int,input().split()))
for i in range(n):
    oop[ (int (subject[i]))] = i+1
correct = True
for i in range(m):
    if oop[k[i]] > oop[o[i]]:
        correct = False
        break

if correct:
    print("YES")
else:
    print("NO")

