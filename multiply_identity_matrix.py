"""Write a Python function multiply_by_identity(matrix) that takes a 2D list matrix as input, representing an 
n×n matrix. The function should multiply the input matrix by the corresponding identity matrix of the same size and return the resulting matrix.
"""

def multiply_by_identity(matrix):
    n = len(matrix)

    identity_matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    
    result = [[0 for _ in range(n)] for _ in range(n)]
     
    for i in range(n):
        for j in range(n):
            result[i][j] = sum(matrix[i][k] * identity_matrix[k][j] for k in range(n))

    
    return result
    



   

print(multiply_by_identity([[2,3,4],[5,6,7], [8,9,10]]))

