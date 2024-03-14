import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def no_idea():
    num_elements, num_sets = map(int, input().split())
    elements = list(map(int, input().split()))
    set_A = set(map(int, input().split()))
    set_B = set(map(int, input().split()))
    happiness = 0
    for element in elements:
        if element in set_A:
            happiness += 1
        elif element in set_B:
            happiness -= 1
    logging.info(happiness)
    return happiness
