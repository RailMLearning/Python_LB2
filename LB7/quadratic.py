import math
import logging
from logger import logger

quad_log = logging.getLogger("quadratic")
quad_log.setLevel(logging.DEBUG)
if not quad_log.handlers:
    sh = logging.StreamHandler()
    fmt = logging.Formatter("%(levelname)s: %(message)s")
    sh.setFormatter(fmt)
    quad_log.addHandler(sh)


@logger(handle=quad_log)
def solve_quadratic(a, b, c):
    """
    Решает ax^2 + bx + c = 0.

    Демонстрация уровней:
    - INFO: при двух корнях
    - WARNING: при d < 0
    - ERROR: при некорректных данных
    - CRITICAL: невозможная ситуация (a = b = 0)
    """
    for name, value in zip(("a", "b", "c"), (a, b, c)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Coefficient '{name}' must be numeric")

    if a == 0 and b == 0:
        quad_log.critical("Невозможная ситуация: a=b=0")
        raise ValueError("Нет решения")

    if a == 0:
        return (-c / b,)

    d = b*b - 4*a*c
    if d < 0:
        quad_log.warning("Дискриминант < 0: нет действительных корней")
        return tuple()

    if d == 0:
        x = -b / (2*a)
        return (x,)

    sqrt_d = math.sqrt(d)
    x1 = (-b + sqrt_d) / (2*a)
    x2 = (-b - sqrt_d) / (2*a)
    return (x1, x2)


if __name__ == "__main__":
    print("Два корня:", solve_quadratic(1, -5, 6))
    print("Нет корней:", solve_quadratic(1, 0, 1))
    try:
        solve_quadratic("abc", 2, 3)
    except Exception:
        pass
    try:
        solve_quadratic(0, 0, 1)
    except Exception:
        pass
