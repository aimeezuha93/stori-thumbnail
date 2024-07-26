import logging

logger = logging.getLogger('data-services')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)s.%(funcName)s:%(lineno)d')
ch.setFormatter(formatter)
logger.addHandler(ch)


def get_logger():
    return logger
