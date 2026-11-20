def rk4(f, x0, y0, x_end, n=100):
    """Giải y' = f(x, y), y(x0) = y0 bằng Runge-Kutta bậc 4, trả về y(x_end)."""
    if n <= 0:
        raise ValueError("n phải là số nguyên dương")
    h = (x_end - x0) / n
    x, y = x0, y0

def rk4(f, x0, y0, x_end, n=100):
    """Giải y' = f(x, y), y(x0) = y0 bằng Runge-Kutta bậc 4, trả về y(x_end)."""
    if n <= 0:
        raise ValueError("n phải là số nguyên dương")
    h = (x_end - x0) / n
    x, y = x0, y0
    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        k3 = f(x + h / 2, y + h * k2 / 2)
        k4 = f(x + h, y + h * k3)
        y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
    return y

def rk4(f, x0, y0, x_end, n=100):
    """Giải y' = f(x, y), y(x0) = y0 bằng Runge-Kutta bậc 4, trả về y(x_end)."""
    if n <= 0:
        raise ValueError("n phải là số nguyên dương")
    h = (x_end - x0) / n
    x, y = x0, y0
    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        k3 = f(x + h / 2, y + h * k2 / 2)
        k4 = f(x + h, y + h * k3)
        y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
    return y


if __name__ == "__main__":
    import math

    approx = rk4(lambda x, y: y, 0, 1, 1, n=10)
    print(f"y(1) ≈ {approx:.6f} (giá trị đúng e = {math.e:.6f})")