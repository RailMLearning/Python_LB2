import sys
import logging
import functools
from typing import Any, Callable, Optional, Union

HandleType = Union[logging.Logger, Any]


def logger(func: Optional[Callable] = None, *, handle: HandleType = sys.stdout):
    """
    Параметризуемый декоратор логирования.

    Логирует:
        - INFO: старт вызова функции + аргументы
        - INFO: успешное завершение функции + результат
        - ERROR: тип и текст исключения (с повторным пробрасыванием)

    Поведение:
        - Если handle — logging.Logger: используется log.info() / log.error()
        - Иначе: используется handle.write(...)

    Args:
        func: декорируемая функция (или None для параметризации)
        handle: объект-поток или логгер (stdout по умолчанию)

    Returns:
        Обёрнутая функция с логированием.
    """

    def _is_logger(h: HandleType) -> bool:
        return isinstance(h, logging.Logger)

    def _write(stream: Any, text: str) -> None:
        if hasattr(stream, "write"):
            stream.write(text + "\n")
        else:
            sys.stdout.write(text + "\n")

    def decorator(inner_func: Callable):
        @functools.wraps(inner_func)
        def wrapper(*args, **kwargs):
            if _is_logger(handle):
                handle.info(f"Start {inner_func.__name__} args={args}, kwargs={kwargs}")
            else:
                _write(handle, f"[INFO] Start {inner_func.__name__} args={args}, kwargs={kwargs}")

            try:
                result = inner_func(*args, **kwargs)
                if _is_logger(handle):
                    handle.info(f"Success {inner_func.__name__} result={result}")
                else:
                    _write(handle, f"[INFO] Success {inner_func.__name__} result={result}")
                return result
            except Exception as e:
                if _is_logger(handle):
                    handle.error(f"Error in {inner_func.__name__}: {type(e).__name__}: {e}")
                else:
                    _write(handle, f"[ERROR] Error in {inner_func.__name__}: {type(e).__name__}: {e}")
                raise
        return wrapper

    if func is None:
        return decorator
    return decorator(func)
