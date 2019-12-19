def diamond(n):
    height = 2*n-1
    number_of_hashes = -1
    increaseNumOfHash = 2

    for i in range(height, 0, -1):
        if(number_of_hashes >= height):
            increaseNumOfHash = -2

        number_of_hashes += increaseNumOfHash
        number_of_white_spaces = int((height-number_of_hashes)/2)
        
        for j in range(0, number_of_white_spaces):
            print(' ',end='')
        
        for j in range(0, number_of_hashes):
            print('#',end='')
        
        for j in range(0, number_of_white_spaces):
            print(' ',end='')
        
        print('')

diamond(4)
