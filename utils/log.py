"""

"""
from logging import getLogger, Logger, StreamHandler, Formatter


def __getLogger(name: str) -> Logger:
    """

    """
    handler = StreamHandler()
    formatter = Formatter()
    logger = getLogger(name)

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel('INFO')
    return logger


logger = __getLogger('aoc')
