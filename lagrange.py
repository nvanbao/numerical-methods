def lagrange(xs, ys, x):
    """Nội suy Lagrange: tính giá trị đa thức đi qua các điểm (xs[i], ys[i]) tại x."""
    if len(xs) != len(ys) or len(xs) == 0:
        raise ValueError("xs và ys phải cùng độ dài và không rỗng")
    if len(set(xs)) != len(xs):
        raise ValueError("Các giá trị trong xs phải khác nhau")
    n = len(xs)
    total = 0.0
    for i in range(n):
        term = ys[i]
        for j in range(n):
            if j != i:
                term *= (x - xs[j]) / (xs[i] - xs[j])
        total += term
    return total