def openRussiondoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussiondoll(doll-1)
        
openRussiondoll(5)