import logging
from logger import logger
from currencies import get_currencies


def build_file_logger(name: str = "currency_file", filename: str = "currency.log") -> logging.Logger:
    """
    Создаёт и настраивает логгер, пишущий в файл.
    """
    log = logging.getLogger(name)
    log.setLevel(logging.INFO)
    if not log.handlers:
        fh = logging.FileHandler(filename, encoding="utf-8")
        fmt = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
        fh.setFormatter(fmt)
        log.addHandler(fh)
    return log


file_logger = build_file_logger()


@logger(handle=file_logger)
def get_currencies_file(currency_codes, url="https://www.cbr-xml-daily.ru/daily_json.js"):
    return get_currencies(currency_codes, url=url)


if __name__ == "__main__":
    print(get_currencies_file(["USD", "EUR"]))
    print("Логи записаны в currency.log")
