def gauss_elimination(A, b):
    """Giải hệ Ax = b bằng khử Gauss có chọn phần tử trụ."""
    n = len(A)
    if n == 0 or any(len(row) != n for row in A):
        raise ValueError("A phải là ma trận vuông")
    if len(b) != n:
        raise ValueError("b phải có cùng số dòng với A")