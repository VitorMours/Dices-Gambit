import logging
import os

import mypy
from datetime import date, datetime



def create_log_directory(path: str = None) -> None:

    if not path and os.path.isdir("/log"):
        os.mkdir("log")


    else:
        pass

def create_logger() -> None:
    create_log_directory()


    logging.basicConfig(
            filename="log/logger.log",
            filemode="a",
            format= "%(asctime)s %(name)s [%(levelname)s] %(message)s",
            encoding="utf-8",
            level=logging.DEBUG,
            datefmt="%d-%b-%y %H:%M:%S")





