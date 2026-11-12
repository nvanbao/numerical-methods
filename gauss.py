def gauss_elimination(A, b):
    """Giải hệ Ax = b bằng khử Gauss có chọn phần tử trụ."""
    n = len(A)
    if n == 0 or any(len(row) != n for row in A):
        raise ValueError("A phải là ma trận vuông")
    if len(b) != n:
        raise ValueError("b phải có cùng số dòng với A")
    M = [row[:] + [b[i]] for i, row in enumerate(A)]

    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(M[r][col]))
        if abs(M[pivot][col]) < 1e-12:
            raise ValueError("Hệ không có nghiệm duy nhất")
        M[col], M[pivot] = M[pivot], M[col]
        for r in range(col + 1, n):
            factor = M[r][col] / M[col][col]
            for c in range(col, n + 1):
                M[r][c] -= factor * M[col][c]

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (M[i][n] - s) / M[i][i]
    return x