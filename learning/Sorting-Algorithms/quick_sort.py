def quicksort(arr, start, end):
    if start >= end:
        return
    pivot = arr[start]
    smaller_index = start
    for i in range(start + 1, end + 1):
        if arr[i] < pivot:
            smaller_index = smaller_index + 1
            arr[smaller_index], arr[i] = arr[i], arr[smaller_index]
    arr[start], arr[smaller_index] = arr[smaller_index], arr[start]
    quicksort(arr, start, smaller_index - 1)
    quicksort(arr, smaller_index + 1, end)



my_list = [3, 5, 0, 6, 2, 1, 4]
quicksort(my_list, 0, 6)
print(my_list)


