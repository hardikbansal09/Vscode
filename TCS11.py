# Taking user input for the array
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

start = 0
end = len(arr) - 1

while start < end:
    # Swap the elements at start and end
    arr[start], arr[end] = arr[end], arr[start]
    # Move the pointers towards the center
    start += 1
    end -= 1

print("Reversed array:", arr)
