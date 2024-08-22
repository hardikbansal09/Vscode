n=int(input())
a=list(map(int,input().split()))

expected_sum=n*(n+1)//2
actual=sum(x for x in a if 1<=x<=n)
missing_number=expected_sum-actual
print(missing_number)
