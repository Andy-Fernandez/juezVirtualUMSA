#matrix multiplication:
def matrix_mult(m1, m2):
    """
    Multiplies two matrices together
    """
    if len(m1[0]) != len(m2):
        return None
    else:
        result = []
        for i in range(len(m1)):
            result.append([])
            for j in range(len(m2[0])):
                result[i].append(0)
                for k in range(len(m2)):
                    result[i][j] += m1[i][k] * m2[k][j]
        return result

#raise a matrix to an exponent
def matrix_pow(m, n):
    """
    Raises a matrix to an exponent
    """
    if n == 0:
        return [[1 if i == j else 0 for i in range(len(m))] for j in range(len(m))]
    elif n == 1:
        return m
    else:
        return matrix_mult(m, matrix_pow(m, n-1))

#inout numbers of a line to a vector
def line_to_vector(line):
    """
    Converts a line of numbers to a vector
    """
    return [int(x) for x in line.split()]

#print formated matrix
def print_matrix(m):
    """
    Prints a matrix
    """
    for i in range(len(m)):
        v = ""
        for j in range(len(m[i])):
            v += str(m[i][j]) + " "
        print(v[:-1])

import sys
a,n= map(int,sys.stdin.readline().split())
m = []
for i in range(a):
    m.append(line_to_vector(sys.stdin.readline()))

print_matrix(matrix_pow(m,n))