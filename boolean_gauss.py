"""
    A simple way to solve boolean systems of the form :
    (a and x) ^ (b and y) ^ (c and z) = A 
    (d and x) ^ (e and y) ^ (f and z) = B
    ....

    Author : Arthur Correnson 
"""
import sys


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


def identity(size):
    """
    @brief      Return Identity matrix.
    """

    assert size > 0, "A size should be > 0"

    M = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        M[i][i] = 1;

    return M


def matmul(Ma, Mb):
    """
    @brief      Implements matrix multiplication.
    """
    
    assert len(Ma[0]) == len(Mb), \
        "Ma and Mb sizes aren't compatible"

    size = len(Mb)
    Mres = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                Mres[i][j] ^= Ma[i][k] * Mb[k][j]

    return Mres


def inverse(M):
    """
    @brief      Implements matrix inversion.
    """

    assert len(M) == len(M[0]), \
        "M should be a square matrix"
    assert is_boolean(M), \
        "M should be a boolean matrix"
    
    size = len(M)
    M_copy = copy(M)
    M_inv  = identity(size)
    
    # gauss method
    for j in range(size):
        search_for_ones(M_copy, j)
        for i in range(1+j, size):
            if M_copy[i][j] == 1:
                M_copy[i] = row_xor(M_copy[i], M_copy[j])
                M_inv[i] = row_xor(M_inv[i], M_copy[j])
    
    for j in range(size):
        for i in range(1+j, size):
            print(size-i-1, size-j-1)
            if M_copy[size-i-1][size-j-1] == 1:
                M_copy[size-i-1] = row_xor(M_copy[size-i-1], M_copy[size-j-1])
                M_inv[size-i-1]  = row_xor(M_inv[size-i-1], M_inv[size-j-1])

    return M_inv


def to_csv(M):
    """
    @brief      Convert a matric M into CSV format
    """
    
    for line in M:
        for row in line:
            print(row, end='; ')
        print('')


def from_csv(file):
    M = []
    with open(file) as f:
        for line in f:
            if line[0] != '#':
                M.append(list(map(lambda x : int(x), line.split(';')[:-1])))

    return M