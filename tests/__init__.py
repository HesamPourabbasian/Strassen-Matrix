import time


def read_matrices_from_file(filename):
    matrices = []
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                # Convert line of numbers to list of integers
                row = [int(x) for x in line.split()]
                matrix.append(row)
            else:
                if matrix:
                    matrices.append(matrix)
                    matrix = []
        if matrix:
            matrices.append(matrix)
    return matrices


def matrix_add(A, B):
    n = len(A)
    m = len(A[0])
    result = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = A[i][j] + B[i][j]
    return result


def matrix_sub(A, B):
    n = len(A)
    m = len(A[0])
    result = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = A[i][j] - B[i][j]
    return result


def standard_multiplication(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)
    result = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                result[i][j] += A[i][k] * B[k][j]
    return result


def strassen_multiplication(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    # Split matrices into quadrants
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Strassen's seven multiplications
    M1 = strassen_multiplication(matrix_add(A11, A22), matrix_add(B11, B22))
    M2 = strassen_multiplication(matrix_add(A21, A22), B11)
    M3 = strassen_multiplication(A11, matrix_sub(B12, B22))
    M4 = strassen_multiplication(A22, matrix_sub(B21, B11))
    M5 = strassen_multiplication(matrix_add(A11, A12), B22)
    M6 = strassen_multiplication(matrix_sub(A21, A11), matrix_add(B11, B12))
    M7 = strassen_multiplication(matrix_sub(A12, A22), matrix_add(B21, B22))

    # Compute quadrants of result
    C11 = matrix_add(matrix_sub(matrix_add(M1, M4), M5), M7)
    C12 = matrix_add(M3, M5)
    C21 = matrix_add(M2, M4)
    C22 = matrix_add(matrix_sub(matrix_add(M1, M3), M2), M6)

    # Combine quadrants into result matrix
    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])
    return C


def matrices_equal(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != B[i][j]:
                return False
    return True


def main():
    matrices = read_matrices_from_file('matrices.txt')
    results = []
    for i in range(0, len(matrices), 2):
        A, B = matrices[i], matrices[i + 1]
        n, m = len(A), len(A[0])
        print(f'Calculating for {n}x{m} matrices...')

        start = time.time()
        result_standard = standard_multiplication(A, B)
        standard_time = time.time() - start

        start = time.time()
        result_strassen = strassen_multiplication(A, B)
        strassen_time = time.time() - start

        # Verify results match
        if not matrices_equal(result_standard, result_strassen):
            print(f"Warning: Results for {n}x{m} matrices do not match!")

        results.append([n, standard_time, strassen_time])

    # Print results table
    print("Matrix Size  Standard Time (s)  Strassen Time (s)")
    for row in results:
        print(f"{row[0]:<11}  {row[1]:<17.6f}  {row[2]:<17.6f}")

    # Save to CSV
    with open('results.csv', 'w') as f:
        f.write('Matrix Size,Standard Time (s),Strassen Time (s)\n')
        for row in results:
            f.write(f'{row[0]},{row[1]:.6f},{row[2]:.6f}\n')


if __name__ == '__main__':
    main()