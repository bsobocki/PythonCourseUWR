import itertools as it

def m_print(solutions):
    print('\n{ ', solutions[0])

    for i in range(1, len(solutions)):
        print(solutions[i])
    
    print('}\n')

def is_correct(solution, a1, a2, a3):
    # generators
    b1 = (str(solution[elem]) for elem in a1)
    b2 = (str(solution[elem]) for elem in a2)
    b3 = (str(solution[elem]) for elem in a3)
    # create string and convert to int
    number1 = int(''.join(b1))
    number2 = int(''.join(b2))
    number3 = int(''.join(b3))

    return number1 + number2 == number3

def cryptarithm(str1, str2, str3):
    a1, a2, a3 = list(str1), list(str2), list(str3)
    letters = list(set(str1 + str2 + str3))
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    solutions = []
    solutions += [str1+' + '+str2+' = '+str3]

    # permutations of digits with len = len(letters) 
    for perm in it.permutations(digits, len(letters)):
        # we must create a new solution for each iteration
        # else we give to solutions a reference 
        # to the one created solution at the beggining, 
        # which may will be changed in next iterations 
        solution = {}
        # letters are ordered in 'letters' variable, 
        # so it is enough to connect i-th element from perm with i-th letter
        # to get a new permutation of both sets
        for i in range(0, len(letters)):
            solution[letters[i]] = perm[i]
            
            
        if is_correct(solution, a1, a2, a3):
            solutions += [solution]
            
    return solutions

# A + B = C   -->   there are a lot solutions
m_print(cryptarithm("A","B","C"))

# e.g 12 + 14 = 26
# AB + AC = BD
m_print(cryptarithm("AB", "AC", "BD"))

# KIOTO + OSAKA = TOKIO -> one solution
m_print(cryptarithm("KIOTO", "OSAKA", "TOKIO"))

# AAA + AAA = CAA  -->   there's no solutions
m_print(cryptarithm("AAA","AAA","CAA"))

# MOM + DAD = KIDS   -->   there are a lot solutions 
m_print(cryptarithm("MOM","DAD","KIDS"))
