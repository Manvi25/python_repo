import numpy as np
import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
def determinant():
    # Read matrix size
    n = int(input())

    # Read matrix elements
    arr = [list(map(float, input().split())) for _ in range(n)]

    # Convert the matrix to numpy array
    matrix = np.array(arr)

    # Calculate the determinant
    det = np.linalg.det(matrix)

    # Round the determinant to 2 decimal places
    det_rounded = round(det, 2)

    # Print the determinant
    logging.info(det_rounded)
    return det_rounded