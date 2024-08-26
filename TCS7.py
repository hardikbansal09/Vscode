n=int(input())
a=[int(input()) for x in range(n)]
if n==0:
    print('0')
else:
    max_so_far=a[0]
    count=1
    for i in range(1,n):
        if a[i]>max_so_far:
            count+=1
            max_so_far=a[i]
    print(count)