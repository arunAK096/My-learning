def linear_search(numbers_list, target):
    for index in range(len(numbers_list)):
        if numbers_list[index] == target:
            return index  

my_list = [5, 9, 3, 12, 8, 4, 7]
search_target = 7

result = linear_search(my_list, search_target)

if result != -1:
    print(f"Target found at position index {result}!")
else:
    print("Target not found in the list.")