def merge(custom_list, left, middle, right):
    n1 = middle - left + 1 
    n2 = right - middle 
    left_part = [0] * n1
    right_part = [0] * n2
    for i in range(n1):
        left_part[i] = custom_list[left + i]
    
    for j in range(n2): 
        right_part[j] = custom_list[middle + 1 + j]
    i = 0     
    j = 0     
    k = left  
    while i < n1 and j < n2:
        if left_part[i] <= right_part[j]:
            custom_list[k] = left_part[i]
            i += 1
        else:
            custom_list[k] = right_part[j]
            j += 1
        k += 1
    while i < n1:
        custom_list[k] = left_part[i]
        i += 1
        k += 1
    while j < n2:
        custom_list[k] = right_part[j]
        j += 1
        k += 1
        
def merge_sort(custom_list, left, right):
    if left < right:
        middle = (left + right) // 2
        merge_sort(custom_list, left, middle)
        merge_sort(custom_list, middle + 1, right)
        merge(custom_list, left, middle, right)
    return custom_list



my_list = [6, 4, 7, 3, 1, 5, 2]
merge_sort(my_list, 0, len(my_list) - 1)
print(my_list)