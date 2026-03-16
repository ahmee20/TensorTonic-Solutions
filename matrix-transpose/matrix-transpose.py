import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    rows=len(A)
    col=len(A[0])
    B=np.zeros((col,rows))

    for x in range(rows):
        for y in range(col):
            B[y][x]=A[x][y]

    return B
    pass
