def practice(n):
    if n < 1:
        print("Less than 1")
    else:
        practice(n-1)
        print(n)
        
practice(5)