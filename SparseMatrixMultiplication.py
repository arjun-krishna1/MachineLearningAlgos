def sparse_matrix_multiplication(matrix_a, matrix_b):
    ''' The linear algebra matrix multiplication of two matrices.
    :param matrix_a: matrix of integers
    :param matrix_b: matrix of integers
    :return: result: matrix of integers

    SPACE-TIME COMPLEXITY
    ---------------------
    - O(ar * bc) SPACE
        - where ar is the number of rows in matrix_a and bc is the number of columns in matrix_b
    - O(ar * bc * br)
        - where br is the number of rows in matrix_b
    '''
    # check that the matrices are compatible
    # the number of columns in A must be equal to the number of rows in B
    if len(matrix_a) == 0 or len(matrix_a[0]) != len(matrix_b):
        return [[]]

    else:
        # set up result with the correct shape
        result = [[0 for i in range(len(matrix_b[0]))] for j in range(len(matrix_a))]
        # do matrix multiplication and return
        for i in range(len(matrix_a)):
            for k in range(len(matrix_a[0])):
                if matrix_a[i][k] != 0:
                    for j in range(len(matrix_b[0])):
                        if matrix_a[i][k] != 0 and matrix_b[k][j] != 0:
                            result[i][j] += matrix_a[i][k] * matrix_b[k][j]

        return result


if __name__ == '__main__':
    mat_a = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    mat_b = [
        [7, 8],
        [9, 10],
        [11, 12],
    ]

    expected_res = [
        [58, 64],
        [139, 154]
    ]
    real_res = sparse_matrix_multiplication(mat_a, mat_b)

    assert expected_res == real_res

    mat_a = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    mat_b = [
        [7, 8],
        [9, 10],
        [11, 12],
    ]

    expected_res = [
        [58, 64],
        [139, 154]
    ]
    real_res = sparse_matrix_multiplication(mat_a, mat_b)
    assert expected_res == real_res, "Algorithm output did not match expected output"
    print("Passed")
