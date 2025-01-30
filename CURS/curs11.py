import numpy as np
"""matrix=np.random.randint(1, 5, (3,3))
normalized_matrix=(matrix - np.min(matrix))/(np.max(matrix)-np.min(matrix))
determinant=np.linalg.det(matrix)
non_singular=determinant!=0
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print (f"Original Matrix\n{matrix}\n")
print (f"Normalized Matrix\n{normalized_matrix}\n")
print (f"Determinant\n{determinant}\n")"""

def determinant(matrix):
    """
    Calculează determinantul unei matrici pătratice folosind dezvoltarea Laplace.
    :param matrix: list[list[float]] - matricea de intrare
    :return: float - determinantul matricei
    """
    n = len(matrix)

    # Cazul de bază: matrice 1x1
    if n == 1:
        return matrix[0][0]

    # Cazul de bază: matrice 2x2
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(n):
        # Construim matricea minoră (fără prima linie și coloana curentă)
        minor = [row[:col] + row[col + 1:] for row in matrix[1:]]

        # Calculăm determinantul recursiv
        det += ((-1) ** col) * matrix[0][col] * determinant(minor)

    return det
matrix = [[1, 2, 3], [4, 1, 3], [4, 2, 4]]
print(f"Determinantul matricei este: {determinant(matrix)}")

