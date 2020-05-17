import logging

FORMAT = '%(asctime)-15s %(name)s %(levelname)-8s %(message)s'
logging.basicConfig(format=FORMAT)


def get_logger(name):
    logger = logging.getLogger(name)
    return logger
