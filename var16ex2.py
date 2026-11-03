def comp(a, b):
    
    if a is None or b is None:
        return False
    
    if len(a) != len(b):
        return False
    
    squares = []
    for i in a:
        squares.append(i * i)
    
    squares.sort()
    b_sorted = []
    for j in b:
        b_sorted.append(j)
    b_sorted.sort()
    
    return squares == b_sorted