# numerical-methods

Các phương pháp số cài đặt bằng Python (môn Numerical Methods).

## Đã có
- Phương pháp chia đôi (`bisection.py`)
- Phương pháp Newton-Raphson (`newton.py`)
- Quy tắc Simpson 1/3 (`simpson.py`)

## Cách chạy

    python bisection.py
    python newton.py
    python simpson.py

## Kết quả mẫu

Giải x³ - x - 2 = 0, nghiệm khoảng 1.521380:
- Chia đôi: khoảng 20 lần lặp
- Newton-Raphson: khoảng 3 lần lặp

Tích phân sin(x) từ 0 đến π bằng Simpson (n = 100): 2.000000

## Cấu trúc
- `bisection.py`, `newton.py`, `simpson.py`: cài đặt các phương pháp
- `test_bisection.py`, `test_newton.py`, `test_simpson.py`: test tương ứng

## Chạy test

    python -m unittest

## Yêu cầu
- Python 3.8+