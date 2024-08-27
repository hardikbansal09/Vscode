t=int(input())
e=[]
for _ in range(t):
    e.append(int(input()))

l=[]
for _ in range(t):
    l.append(int(input()))

cg=0
mg=0
for i in range(t):
    cg+=e[i]-l[i]
    if cg>mg:
        mg=cg

print(mg)