from typing import List, Dict
import requests


def get_currencies(currency_codes: List[str],
                   url: str = "https://www.cbr-xml-daily.ru/daily_json.js") -> Dict[str, float]:
    """
    Получает курсы валют с API ЦБ РФ.

    Args:
        currency_codes: список символьных кодов валют (например, ["USD", "EUR"])
        url: адрес API (по умолчанию официальный ЦБ РФ)

    Returns:
        Словарь вида {"USD": 93.25, "EUR": 101.7}

    Raises:
        ConnectionError: если API недоступен
        ValueError: если JSON некорректный
        KeyError: если нет ключа 'Valute' или валюта отсутствует
        TypeError: если курс валюты имеет неверный тип
    """
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException as e:
        raise ConnectionError("API недоступен") from e

    try:
        data = response.json()
    except Exception as e:
        raise ValueError("Некорректный JSON") from e

    if "Valute" not in data:
        raise KeyError("Нет ключа 'Valute'")

    valute = data["Valute"]
    result: Dict[str, float] = {}
    for code in currency_codes:
        if code not in valute:
            raise KeyError(f"Валюта {code} отсутствует")
        value = valute[code]["Value"]
        if not isinstance(value, (int, float)):
            raise TypeError(f"Курс валюты {code} имеет неверный тип")
        result[code] = float(value)
    return result
