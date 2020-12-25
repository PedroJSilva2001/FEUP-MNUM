from numpy import reshape
from numpy import array
def print_matrix(matrix, m, n):
    print(reshape(array(matrix), (m,n)))


def setup_matrices(A, b, n): 
    #vai alocar espaço para a Matriz A mais o Vetor b
    a = [[0 for column in range(n+1)] for row in range(n)]
    #vai preencher a com os valores de A e b
    for row in range(n):
        for column in range(n+1):
            #preencher os valores de b
            if column >= n:
                a[row][column] = b[row]
            else:
            #preencher os valores de A
                a[row][column] = A[row][column]
    return a

def get_solution_vector(a, n):
    X = [1 for row in range(n)]
    for i in range(n-1, -1, -1):
        xi = 0.0
        for col in range(i+1, n):
            xi += a[i][col]*X[col]
        X[i] = a[i][n] -xi
    return X

def gauss_method(A, b):
    n = len(A)
    a = setup_matrices(A,b, n)

    for i in range(n):
        for column in range(i+1, n+1):
            a[i][column] /= a[i][i]
        a[i][i] = 1
        for row in range(i+1, n):
            for col in range(i+1, n+1):
                a[row][col] -= a[row][i]* a[i][col]
            a[row][i] = 0

    print_matrix(a, n, n+1)
    X = get_solution_vector(a, n)
    print(X)

gauss_method([[1.0, 0.5, 1/3],[0.5, 1/3, 0.25],[1/3, 0.25, 0.2]], [-1.0, 1.0, 1.0])