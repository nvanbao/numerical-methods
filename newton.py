def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """Tìm nghiệm của f(x) = 0 bằng phương pháp Newton-Raphson."""
    if tol <= 0:
        raise ValueError("tol phải dương")
    x = x0
    for i in range(1, max_iter + 1):
        d = df(x)
        if d == 0:
            raise ZeroDivisionError("Đạo hàm bằng 0, không thể tiếp tục")
        x_new = x - f(x) / d
        if abs(x_new - x) < tol:
            return x_new, i
        x = x_new
    return x, max_iter


if __name__ == "__main__":
    f = lambda x: x**3 - x - 2
    df = lambda x: 3 * x**2 - 1
    root, iters = newton_raphson(f, df, 1.5)
    print(f"Nghiệm: {root:.6f} sau {iters} lần lặp")