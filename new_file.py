def min_sum_submatrix(matrix, X, Y):
    N = len(matrix)
    M = len(matrix[0])

    # Step 1: Compute the prefix sum matrix
    prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            prefix_sum[i][j] = matrix[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][
                j - 1]
    print(prefix_sum)
    # Step 2: Find the minimum sum submatrix of size X x Y
    min_sum = float('inf')
    top_left = (0, 0)

    for i in range(X, N + 1):
        for j in range(Y, M + 1):
            total = (prefix_sum[i][j] - prefix_sum[i - X][j] - prefix_sum[i][j - Y] + prefix_sum[i - X][j - Y])

            if total < min_sum:
                min_sum = total
                top_left = (i - X, j - Y)

    # Step 3: Return the result
    return min_sum, top_left
matrix = [
    [1, 2,  3,  4],
    [0, 0, -1, -1],
    [1, 0,  1,  0]
]

X, Y = 2, 2  # Example submatrix size

min_sum, position = min_sum_submatrix(matrix, X, Y)
print("Minimum Sum:", min_sum)
print("Top-left position:", position)
