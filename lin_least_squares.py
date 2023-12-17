
'''
Module that calculates the Globali linear least squares approximation of a function, given two points.
'''

def least_square(x_set: list[float], y_set: list[float]):
    """
    Given a data set, determines the discrete form of a linear least square approximation

    Args:
        y_set: An array of the y-values for a set of data points

        x_set: An array of the x-values for a set of data points

    Yields:
        A list containing the calculated constants for the approximation function
    """

    # Generate the Ac|b augmented matrix
    matrix = []
    # Generate the rows (2 for a linear approximation)
    for n_row in range(0, 2):
        matrix.append([])
        # Generate the columns (3 for a linear approximation)
        for n_col in range(0, 3):
            # If we reach the last column, sum the product of the x to the power of the current row with the corresponding y-value.
            if (n_col == 2):
                sum = 0
                for k_x, k_y in zip(x_set, y_set):
                    sum += (k_x**n_row) * k_y
                matrix[n_row].append(sum)
                break
            # For each position, sum the product of each x to the power of the current row and the same x to the power of the current column
            sum = 0
            for k_x in x_set:
                sum += (k_x**n_row) * (k_x**n_col)
            matrix[n_row].append(sum)

    # Solve the matrix to reveal the constant values
    # Perform operations on each row to bring the matrix to Row Echelon Form
    for n_row in range(0, 2):
        # For the current row, generate the 1 value for the upper triangle
        diagonal_value = matrix[n_row][n_row]
        for n_col in range(0, 3):
            matrix[n_row][n_col] /= diagonal_value
        
        # Make the elements below the first pivot point 0
        for k_row in range(n_row + 1, 2):
            factor = matrix[k_row][n_row]
            for k_col in range (0, 3):
                matrix[k_row][k_col] -= factor * matrix[n_row][k_col]

    # Perform a backsolving operation to solve the first row
    factor = matrix[0][1]
    for n_col in range(0, 3):
        matrix[0][n_col] -= factor * matrix[1][n_col]
    
    constants = []
    for n_row in range(0, 2):
        constants.append(matrix[n_row][2])
        
    return constants