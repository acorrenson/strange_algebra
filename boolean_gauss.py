"""
    A simple way to solve boolean systems of the form :
    (a and x) ^ (b and y) ^ (c and z) = A 
    (d and x) ^ (e and y) ^ (f and z) = B
    ....

    Author : Arthur Correnson 
"""


def copy(M):
    """
    @brief      Copy a Matrix M.
    """
    
    M_copy = []
    for i in M:
        a = []
        for j in i:
            a.append(j)
        M_copy.append(a)
    return M_copy


def is_boolean(M):
    """
    @brief      Test if a matrix M is a boolean matrix.
    """
    
    for i in M:
        for j in i:
            if j != 0 and j != 1:
                return False
    return True



def search_for_ones(M, j):
    """
    @brief      Ensure that M[j][j] == 1. Uses rows swap if needed.
    
    @param      M     A matrix valued in {0, 1}
    @param      j     Index concerned
    """
    
    size = len(M)
    assert j < size, "indexation error"
    k = j
    
    while M[j][j] != 1 and k < size:
        if M[k][j] == 1:
            temp = M[j]
            M[j] = M[k]
            M[k] = temp
        k += 1

    assert M[j][j] == 1, ("null column " + str(j))


def row_xor(a, b):
    """
    @brief      Apply xor on two boolean vectors.
    
    @param      a     { parameter_description }
    @param      b     { parameter_description }
    
    @return     { description_of_the_return_value }
    """
    
    assert len(a) == len(b), "incompatible length arguments"
    
    c = []
    
    for x,y in zip(a, b):
        c.append(x ^ y)

    return c


def gaussian_elimination(M):
    """
    @brief      Apply Gaussian elimination on matrix M
    
    @param      M     The system matrix
    @param      Y     The target
    
    @return     An equivalent, simplified system matrix.
    """
    
    assert len(M) == len(M[0]) - 1, \
        "M should be a square matrix"
    assert is_boolean(M), \
        "M should be a boolean matrix"
    
    size = len(M)
    M_copy = copy(M)
    
    for j in range(size):
        search_for_ones(M_copy, j)
        for i in range(1+j, size):
            if M_copy[i][j] == 1:
                M_copy[i] = row_xor(M_copy[i], M_copy[j])

    return M_copy


def to_csv(M):
    """
    @brief      Convert a matric M into CSV format
    """
    
    for line in M:
        for row in line:
            print(row, end='; ')
        print('')
