def heapify(custom_list, n, i):
    smallest = i          
    left = 2 * i + 1      
    right = 2 * i + 2     
    if left < n and custom_list[left] < custom_list[smallest]:
        smallest = left
    if right < n and custom_list[right] < custom_list[smallest]:
        smallest = right
    if smallest != i:
        custom_list[i], custom_list[smallest] = custom_list[smallest], custom_list[i]
        heapify(custom_list, n, smallest)


def heap_sort(custom_list):
    n = len(custom_list)
    for i in range(n // 2 - 1, -1, -1):
        heapify(custom_list, n, i)
    for i in range(n - 1, 0, -1):
        custom_list[0], custom_list[i] = custom_list[i], custom_list[0]
        heapify(custom_list, i, 0)
    custom_list.reverse()
    return custom_list


my_list = [15, 10, 40, 20, 50, 5, 30]
print("Original List:", my_list)

sorted_list = heap_sort(my_list)
print("Sorted List:  ", sorted_list)