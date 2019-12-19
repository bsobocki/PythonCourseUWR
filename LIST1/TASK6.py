def table(x1, x2, y1, y2):
    print("\t", end='')
    for i in range(x1, x2):
        print(i, end='\t')
    
    print(' ')

    for i in range(y1, y2):
        print(i, end='\t')
        for j in range(x1, x2):
            print(j*i, end='\t')
        
        print(' ')


table(2,11,10,13)