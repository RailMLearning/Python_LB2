Отчёт по лабораторной работе №7
Цели работы:

Освоить принципы разработки декораторов с параметрами;

научиться разделять ответственность функций (бизнес‑логика) и декораторов (сквозная логика);

научиться обрабатывать исключения, возникающие при работе с внешними API;

освоить логирование в разные типы потоков (sys.stdout, io.StringIO, logging);

научиться тестировать функцию и поведение логирования.



 Задание
Реализовать декоратор с параметрами.

Реализовать функцию get_currencies, получающую курсы валют с сайта ЦБ РФ (без логирования).

Сделать демонстрационный пример решения квадратного уравнения.

Продемонстрировать работу логирования (фрагменты логов).

Написать тесты: функции, декоратора, работы со StringIO.



 Исходный код
Декоратор с параметрами
```
import logging
from functools import wraps

def log_decorator(level=logging.INFO):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logging.log(level, f"Вызов функции {func.__name__} с args={args}, kwargs={kwargs}")
            try:
                result = func(*args, **kwargs)
                logging.log(level, f"Функция {func.__name__} вернула {result}")
                return result
            except Exception as e:
                logging.error(f"Ошибка в функции {func.__name__}: {e}")
                raise
        return wrapper
    return decorator
```

Функция get_currencies (без логирования)
```
import requests

def get_currencies(codes, url="https://www.cbr-xml-daily.ru/daily_json.js"):
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    result = {}
    for code in codes:
        if code not in data["Valute"]:
            raise KeyError(f"Валюта {code} не найдена")
        result[code] = data["Valute"][code]["Value"]
    return result
```

Демонстрационный пример (квадратное уравнение)
```
import math

def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        raise ValueError("Нет действительных корней")
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    return x1, x2

# Пример:
print(solve_quadratic(1, -3, 2))  # (2.0, 1.0)
```




<img width="1053" height="651" alt="изображение" src="https://github.com/user-attachments/assets/870928f6-02c1-40f5-b426-02de8ee6a38a" />




Тестирование
Тесты функции
```
import unittest

class TestQuadratic(unittest.TestCase):
    def test_roots(self):
        self.assertEqual(solve_quadratic(1, -3, 2), (2.0, 1.0))

    def test_no_roots(self):
        with self.assertRaises(ValueError):
            solve_quadratic(1, 0, 1)
```

```
import unittest
import logging
from io import StringIO

class TestDecorator(unittest.TestCase):
    def test_logging(self):
        log_stream = StringIO()
        logging.basicConfig(stream=log_stream, level=logging.INFO)

        @log_decorator(logging.INFO)
        def add(a, b):
            return a + b

        result = add(2, 3)
        self.assertEqual(result, 5)
        logs = log_stream.getvalue()
        self.assertIn("Вызов функции add", logs)
        self.assertIn("вернула 5", logs)
```

Тесты работы с StringIO
```
import unittest
import logging
from io import StringIO

class TestStringIO(unittest.TestCase):
    def test_log_capture(self):
        log_stream = StringIO()
        logging.basicConfig(stream=log_stream, level=logging.INFO)

        logging.info("Тестовое сообщение")
        self.assertIn("Тестовое сообщение", log_stream.getvalue())
```



В ходе лабораторной работы:

освоены принципы разработки декораторов с параметрами;

разделена ответственность функций и декораторов;

реализована обработка исключений при работе с внешним API ЦБ РФ;

продемонстрировано логирование в разные потоки;

написаны тесты для функций, декоратора и работы со StringIO.

Цель работы достигнута.
