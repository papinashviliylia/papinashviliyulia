def binary_array_to_number(arr):
    number = 0
    
    for i in arr:
        number = number * 2 + i
        
    return number