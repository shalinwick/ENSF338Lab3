def merge(arr, left, middle, right):
    size_left = middle - left + 1
    size_right = right - middle

    
    left_array = [0] * size_left
    right_array = [0] * size_right

    
    for x in range(size_left):
        left_array[x] = arr[left + x]
    for y in range(size_right):
        right_array[y] = arr[middle + 1 + y]

    
    x = 0  
    y = 0  
    z = left 

    while x < size_left and y < size_right:
        if left_array[x] <= right_array[y]:
            arr[z] = left_array[x]
            x += 1
        else:
            arr[z] = right_array[y]
            y += 1
        z += 1

    
    while x < size_left:
        arr[z] = left_array[x]
        x += 1
        z += 1

    
    while y < size_right:
        arr[z] = right_array[y]
        y += 1
        z += 1

