# numerical-methods

Các phương pháp số cài đặt bằng Python (môn Numerical Methods).

## Đã có
- Phương pháp chia đôi (`bisection.py`)
- Phương pháp Newton-Raphson (`newton.py`)
- Quy tắc Simpson 1/3 (`simpson.py`)
- Khử Gauss giải hệ phương trình tuyến tính (`gauss.py`)
- Quy tắc hình thang tính tích phân (`trapezoid.py`)
- Runge-Kutta bậc 4 giải phương trình vi phân (`rk4.py`)
## Cách chạy

    python bisection.py
    python newton.py
    python simpson.py
    python gauss.py
    python trapezoid.py
    python rk4.py
## Kết quả mẫu

Giải x³ - x - 2 = 0, nghiệm khoảng 1.521380:
- Chia đôi: khoảng 20 lần lặp
- Newton-Raphson: khoảng 3 lần lặp

Tích phân sin(x) từ 0 đến π bằng Simpson (n = 100): 2.000000

Giải hệ 3 phương trình bằng khử Gauss: nghiệm [2.0, 3.0, -1.0]

## Cấu trúc
- `bisection.py`, `newton.py`, `simpson.py`, `gauss.py`: cài đặt các phương pháp
- `test_*.py`: test tương ứng cho từng phương pháp

## Chạy test

    python -m unittest
## Đã có 
    - Nội suy Lagrange (`lagrange.py`)
    - Phương pháp Euler giải phương trình vi phân (`euler.py`)
    python lagrange.py
    python euler.py

## Yêu cầu
- Python 3.8+