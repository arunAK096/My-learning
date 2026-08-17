def binary_search(custom_array, value):
    start = 0
    end = len(custom_array) - 1
    middle = (start + end) // 2
    while custom_array[middle] != value and start <= end:
        if value < custom_array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = (start + end) // 2
    if custom_array[middle] == value:
        return middle  
    else:
        return -1  
    
my_list = [8, 9, 11, 12, 15, 17, 20, 25, 28]
target = 12

result = binary_search(my_list, target)
print(f"Target found at index: {result}")