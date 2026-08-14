import math  # 📌 We need this for square root and ceil functions


# First, we need a helper function to sort small buckets
# We use Insertion Sort for this (it must RETURN the sorted list)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr  # ✅ IMPORTANT: Must return, not print!

# 🎯 MAIN BUCKET SORT FUNCTION
def bucket_sort(custom_list):
    
    # ── STEP 1: Find how many buckets we need ──
    # Number of buckets = round( square root of list length )
    number_of_buckets = round(math.sqrt(len(custom_list)))
    
    # ── STEP 2: Find the biggest number ──
    max_value = max(custom_list)
    
    # ── STEP 3: Create empty buckets ──
    # We make a list of empty lists
    buckets = []
    for i in range(number_of_buckets):
        buckets.append([])  # Add an empty bucket
    
    # Now buckets looks like: [[], [], []]  (3 empty buckets)
    
    # ── STEP 4: Put each number into the right bucket ──
    for number in custom_list:
        # Find which bucket this number belongs to
        bucket_index = math.ceil(number * number_of_buckets / max_value)
        
        # Subtract 1 because lists start at position 0
        bucket_index = bucket_index - 1
        
        # Put the number into that bucket
        buckets[bucket_index].append(number)
    
    # ── STEP 5: Sort each bucket ──
    for i in range(number_of_buckets):
        # Use insertion sort and replace the bucket with sorted version
        buckets[i] = insertion_sort(buckets[i])
    
    # ── STEP 6: Merge all buckets back together ──
    k = 0  # This tracks where we are in the original list
    for i in range(number_of_buckets):       # Go through each bucket
        for j in range(len(buckets[i])):     # Go through each number in bucket
            custom_list[k] = buckets[i][j]   # Put number back into main list
            k += 1                             # Move to next position
    
    return custom_list 


my_list = [5, 3, 4, 7, 2, 8, 6, 9, 1]
sorted_list = bucket_sort(my_list)
print(sorted_list)