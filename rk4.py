def rk4(f, x0, y0, x_end, n=100):
    """Giải y' = f(x, y), y(x0) = y0 bằng Runge-Kutta bậc 4, trả về y(x_end)."""
    if n <= 0:
        raise ValueError("n phải là số nguyên dương")
    h = (x_end - x0) / n
    x, y = x0, y0