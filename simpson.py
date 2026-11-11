def simpson(f, a, b, n=100):
    """Tính tích phân của f trên [a, b] bằng quy tắc Simpson 1/3."""
    if n <= 0 or n % 2 != 0:
        raise ValueError("n phải là số chẵn dương")