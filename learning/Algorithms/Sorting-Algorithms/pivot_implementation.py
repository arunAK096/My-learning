def swap(my_list, index_one, index_two):
    my_list[index_one], my_list[index_two] = my_list[index_two], my_list[index_one]

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    
    for i in range(pivot_index + 1, end_index + 1):
        
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def quicksort_helper(my_list, left, right):

    if left < right:
        pivot_index = pivot(my_list, left, right)
        quicksort_helper(my_list, left, pivot_index - 1)
        quicksort_helper(my_list, pivot_index + 1, right)
    
    return my_list