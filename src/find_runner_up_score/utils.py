import logging
logging.basicConfig(level= logging.INFO, format= '%(message)s')
def runner_up():
    a=int(input())
    n=set(map(int, input().split()))
    n = list(n)
    n.sort()
    logging.info((n[-2]))
    return (n[-2])
