def trapezoid(f, a, b, n=100):
    """Tính tích phân của f trên [a, b] bằng quy tắc hình thang với n đoạn."""
    if n <= 0:
        raise ValueError("n phải là số nguyên dương")
    h = (b - a) / n

def trapezoid(f, a, b, n=100):
    """Tính tích phân của f trên [a, b] bằng quy tắc hình thang với n đoạn."""
    if n <= 0:
        raise ValueError("n phải là số nguyên dương")
    h = (b - a) / n
    total = (f(a) + f(b)) / 2
    for i in range(1, n):
        total += f(a + i * h)
    return total * h