def bisection(f, a, b, tol=1e-6, max_iter=100):
    """Tìm nghiệm của f(x) = 0 trong [a, b] bằng phương pháp chia đôi."""
    if a >= b:
        raise ValueError("Cần a < b")
    if tol <= 0:
        raise ValueError("tol phải dương")
    if f(a) * f(b) > 0:
        raise ValueError("f(a) và f(b) phải trái dấu")
    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < tol:
            return c, i
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2, max_iter


if __name__ == "__main__":
    f = lambda x: x**3 - x - 2
    root, iters = bisection(f, 1, 2)
    print(f"Nghiệm: {root:.6f} sau {iters} lần lặp")