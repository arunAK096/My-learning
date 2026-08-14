def selection_sort(custom_list):
    n = len(custom_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if custom_list[j] < custom_list[min_index]:
                min_index = j
        custom_list[i], custom_list[min_index] = custom_list[min_index], custom_list[i]


numbers = [5, 7, 4, 1, 2]
selection_sort(numbers)
print("Sorted Array:", numbers)