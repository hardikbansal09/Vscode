r=int(input("r:"))
unit = int(input("unit:"))
n=int(input("n:"))
arr=list(map(int,input().split()))


def calculate(r,unit,n,arr):
    total=r*unit
    a=0
    for i in range(n-1):
        a+=i
        if a>=total:
            return i-1

print(calculate(r,unit,n,arr))
