def dec(n):
    assert n>=0 and int(n) == n, 'The number must be positive integer only'
    if n == 0:
        return 0
    else:
        return n%2 +10 * dec(int(n/2)) 

print(dec(13))