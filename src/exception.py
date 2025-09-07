import sys
from src.logger import logging


def error_mesege_detail(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_mesege = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_mesege

class CustomException(Exception):
    def __init__(self, error_mesege, error_detail: sys):
        super().__init__(error_mesege)
        self.error_mesege = error_mesege_detail(error_mesege, error_detail)

    def __str__(self):
        return self.error_mesege

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero attempted")
        raise CustomException(e, sys)
