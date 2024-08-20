def sum_of_starting_10_multiple(a):
    b=0
    for i in range(1,11):
        c=a*i
        b+=c
    return b
a=int(input())
result=sum_of_starting_10_multiple(a)
print(result)