def insertion_sort(custom_list):
    for i in range(1, len(custom_list)):
        key = custom_list[i]
        j = i - 1
        while j >= 0 and key < custom_list[j]:
            custom_list[j + 1] = custom_list[j]
            j = j - 1
        custom_list[j + 1] = key
    return custom_list



my_list = [5, 3, 4, 7, 2, 8, 6, 9, 1]
print("Before:", my_list)
print("After:", insertion_sort(my_list))