def sparse_matrix_multiplication(matrix_a, matrix_b):
    if len(matrix_a) == 0 or len(matrix_a[0]) != len(matrix_b):
        return [[]]

    else:
        result = [[0 for i in range(len(matrix_b[0]))] for j in range(len(matrix_a))]
        # do matrix multiplication and return
        for i in range(len(matrix_a)):
            this_row = matrix_a[i]
            for j in range(len(matrix_b[0])):
                this_column = [matrix_b[k][j] for k in range(len(matrix_b))]
                this_dot_product = sum([this_row[k] * this_column[k] for k in range(len(matrix_b))])
                result[i][j] = this_dot_product
        return result
    return [[]]


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

    assert expected_res == real_res, "Algorithm output did not match expected output"
    print("Passed")
