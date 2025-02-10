import time
import logging


def time_function(func, *args):
    start = time.time()
    func(*args)
    logging.info(time.time() - start)


logging.basicConfig(level=logging.INFO)
time_function(time.sleep, 0.2)
