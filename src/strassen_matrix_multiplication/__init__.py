import time

# Import the time module to measure execution time of matrix operations

def read_matrices_from_file(filename):
    # Initialize an empty list to store all matrices
    matrices = []
    # Initialize an empty list to store the current matrix being built
    matrix = []
    # Open the specified file in read mode
    with open(filename, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Remove leading/trailing whitespace from the line
            line = line.strip()
            if line:
                # Convert line of numbers to list of integers
                row = [int(x) for x in line.split()]
                # Append the row to the current matrix
                matrix.append(row)
            else:
                # If line is empty and matrix is not empty, append matrix to matrices
                if matrix:
                    matrices.append(matrix)
                    # Reset matrix for the next matrix
                    matrix = []
        # If there is a matrix after the last empty line, append it
        if matrix:
            matrices.append(matrix)
    # Return the list of matrices
    return matrices


def matrix_add(A, B):
    # Get the dimensions of matrix A
    n = len(A)
    m = len(A[0])
    # Initialize result matrix with zeros
    result = [[0 for _ in range(m)] for _ in range(n)]
    # Iterate through each element
    for i in range(n):
        for j in range(m):
            # Add corresponding elements of A and B
            result[i][j] = A[i][j] + B[i][j]
    # Return the resulting matrix
    return result


def matrix_sub(A, B):
    # Get the dimensions of matrix A
    n = len(A)
    m = len(A[0])
    # Initialize result matrix with zeros
    result = [[0 for _ in range(m)] for _ in range(n)]
    # Iterate through each element
    for i in range(n):
        for j in range(m):
            # Subtract corresponding elements of B from A
            result[i][j] = A[i][j] - B[i][j]
    # Return the resulting matrix
    return result


def standard_multiplication(A, B):
    # Get dimensions: n = rows of A, m = columns of B, p = columns of A/rows of B
    n = len(A)
    m = len(B[0])
    p = len(B)
    # Initialize result matrix with zeros
    result = [[0 for _ in range(m)] for _ in range(n)]
    # Iterate through each element of result
    for i in range(n):
        for j in range(m):
            for k in range(p):
                # Compute the dot product for position (i,j)
                result[i][j] += A[i][k] * B[k][j]
    # Return the resulting matrix
    return result


def strassen_multiplication(A, B):
    # Get the size of the square matrix
    n = len(A)
    # Base case: 1x1 matrix multiplication
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Calculate midpoint for splitting matrices
    mid = n // 2

    # Split matrices into quadrants
    # Top-left quadrant of A
    A11 = [row[:mid] for row in A[:mid]]
    # Top-right quadrant of A
    A12 = [row[mid:] for row in A[:mid]]
    # Bottom-left quadrant of A
    A21 = [row[:mid] for row in A[mid:]]
    # Bottom-right quadrant of A
    A22 = [row[mid:] for row in A[mid:]]
    # Top-left quadrant of B
    B11 = [row[:mid] for row in B[:mid]]
    # Top-right quadrant of B
    B12 = [row[mid:] for row in B[:mid]]
    # Bottom-left quadrant of B
    B21 = [row[:mid] for row in B[mid:]]
    # Bottom-right quadrant of B
    B22 = [row[mid:] for row in B[mid:]]

    # Strassen's seven multiplications
    # M1 = (A11 + A22)(B11 + B22)
    M1 = strassen_multiplication(matrix_add(A11, A22), matrix_add(B11, B22))
    # M2 = (A21 + A22)B11
    M2 = strassen_multiplication(matrix_add(A21, A22), B11)
    # M3 = A11(B12 - B22)
    M3 = strassen_multiplication(A11, matrix_sub(B12, B22))
    # M4 = A22(B21 - B11)
    M4 = strassen_multiplication(A22, matrix_sub(B21, B11))
    # M5 = (A11 + A12)B22
    M5 = strassen_multiplication(matrix_add(A11, A12), B22)
    # M6 = (A21 - A11)(B11 + B12)
    M6 = strassen_multiplication(matrix_sub(A21, A11), matrix_add(B11, B12))
    # M7 = (A12 - A22)(B21 + B22)
    M7 = strassen_multiplication(matrix_sub(A12, A22), matrix_add(B21, B22))

    # Compute quadrants of result
    # C11 = M1 + M4 - M5 + M7
    C11 = matrix_add(matrix_sub(matrix_add(M1, M4), M5), M7)
    # C12 = M3 + M5
    C12 = matrix_add(M3, M5)
    # C21 = M2 + M4
    C21 = matrix_add(M2, M4)
    # C22 = M1 + M3 - M2 + M6
    C22 = matrix_add(matrix_sub(matrix_add(M1, M3), M2), M6)

    # Combine quadrants into result matrix
    C = []
    # Append top half (C11 | C12)
    for i in range(mid):
        C.append(C11[i] + C12[i])
    # Append bottom half (C21 | C22)
    for i in range(mid):
        C.append(C21[i] + C22[i])
    # Return the resulting matrix
    return C


def matrices_equal(A, B):
    # Check if dimensions are different
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False
    # Compare each element
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != B[i][j]:
                return False
    # Return True if all elements match
    return True


def main():
    # Read matrices from file
    matrices = read_matrices_from_file('matrices.txt')
    # Initialize list to store results
    results = []
    # Process matrices in pairs
    for i in range(0, len(matrices), 2):
        # Get the pair of matrices
        A, B = matrices[i], matrices[i + 1]
        # Get dimensions of matrix A
        n, m = len(A), len(A[0])
        # Print status message
        print(f'Calculating for {n}x{m} matrices...')

        # Measure time for standard multiplication
        start = time.time()
        result_standard = standard_multiplication(A, B)
        standard_time = time.time() - start

        # Measure time for Strassen multiplication
        start = time.time()
        result_strassen = strassen_multiplication(A, B)
        strassen_time = time.time() - start

        # Verify results match
        if not matrices_equal(result_standard, result_strassen):
            print(f"Warning: Results for {n}x{m} matrices do not match!")

        # Store results
        results.append([n, standard_time, strassen_time])

    # Print results table
    print("Matrix Size  Standard Time (s)  Strassen Time (s)")
    for row in results:
        print(f"{row[0]:<11}  {row[1]:<17.6f}  {row[2]:<17.6f}")

    # Save to CSV
    with open('results.csv', 'w') as f:
        # Write header
        f.write('Matrix Size,Standard Time (s),Strassen Time (s)\n')
        # Write each result row
        for row in results:
            f.write(f'{row[0]},{row[1]:.6f},{row[2]:.6f}\n')


if __name__ == '__main__':
    # Execute main function if script is run directly
    main()