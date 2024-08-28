# 2nd largest no. in an array
array = [10, 20, 4, 45, 99, 99]

if len(array) < 2:
    second_largest = None
else:
    first, second = float('-inf'), float('-inf')

    for num in array:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    if second == float('-inf'):
        second_largest = None
    else:
        second_largest = second

print("The second largest number is:", second_largest)
