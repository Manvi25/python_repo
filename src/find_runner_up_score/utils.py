import logging
logging.basicConfig(level= logging.INFO, format= '%(message)s')
def runner_up(n):
    n = list(n)
    n.sort()
    logging.info((n[-2]))