def trapezoid(f, a, b, n=100):
    """Tính tích phân của f trên [a, b] bằng quy tắc hình thang với n đoạn."""
    if n <= 0:
        raise ValueError("n phải là số nguyên dương")
    h = (b - a) / n