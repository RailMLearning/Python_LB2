import sys
import logging
from logger import logger
from currencies import get_currencies
from quadratic import solve_quadratic

# Логи будут выводиться в консоль
logging.basicConfig(level=logging.INFO)

@logger(handle=sys.stdout)   # вывод в stdout
def demo_quadratic_ok():
    return solve_quadratic(1, -3, 2)

@logger(handle=sys.stdout)
def demo_quadratic_fail():
    return solve_quadratic(1, 0, 1)

@logger(handle=sys.stdout)
def demo_currencies():
    return get_currencies(["USD", "EUR"])

if __name__ == "__main__":
    print("Quadratic OK:", demo_quadratic_ok())
    try:
        demo_quadratic_fail()
    except Exception:
        pass
    print("Currencies:", demo_currencies())
