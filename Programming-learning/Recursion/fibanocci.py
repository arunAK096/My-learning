def fibanooci(n):
    assert n>=0 and int(n) == n, 'The number must be positive integer only'
    if n in [0,1]:
        return n
    else:
        return fibanooci(n-1) + fibanooci(n-2)
        
print(fibanooci(5))
        
