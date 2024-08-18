a=input()
b=list(map(int,a.split()))

def zeros(b):
    non_zero_list=[]
    zero_count=0
    for i in b:
        if i==0:
            zero_count+=1
        else:
            non_zero_list.append(i)

    non_zero_list.extend([0]*zero_count)

    return non_zero_list


print(zeros(b))
