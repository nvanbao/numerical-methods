def simpson(f, a, b, n=100):
    """Tính tích phân của f trên [a, b] bằng quy tắc Simpson 1/3."""
    if n <= 0 or n % 2 != 0:
        raise ValueError("n phải là số chẵn dương")
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4 if i % 2 == 1 else 2) * f(a + i * h)
    return total * h / 3


if __name__ == "__main__":
    import math

    print(f"Tích phân sin(x) từ 0 đến pi: {simpson(math.sin, 0, math.pi):.6f}")