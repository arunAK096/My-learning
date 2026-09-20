def arrayrev(nums):
    n = list(nums)
    for i in range(len(nums)//2):
        n[i],n[len(n)-i-1]= n[len(n)-i-1],n[i]
        result = ''.join(n)
    return result

print(arrayrev("Hello World"))