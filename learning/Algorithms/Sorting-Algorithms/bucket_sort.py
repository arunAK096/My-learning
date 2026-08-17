import math


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr 

def bucket_sort(custom_list):
    number_of_buckets = round(math.sqrt(len(custom_list)))
    max_value = max(custom_list)
    buckets = []
    for i in range(number_of_buckets):
        buckets.append([])
    for number in custom_list:
        bucket_index = math.ceil(number * number_of_buckets / max_value)
        bucket_index = bucket_index - 1
        buckets[bucket_index].append(number)
    for i in range(number_of_buckets):
        buckets[i] = insertion_sort(buckets[i])
    k = 0  
    for i in range(number_of_buckets):       
        for j in range(len(buckets[i])):     
            custom_list[k] = buckets[i][j]   
            k += 1               
    
    return custom_list 


my_list = [5, 3, 4, 7, 2, 8, 6, 9, 1]
sorted_list = bucket_sort(my_list)
print(sorted_list)