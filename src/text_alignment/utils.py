import logging
logging.basicConfig(level= logging.INFO, format= '%(message)s')
def print_logo():
    thickness = int(input())
    c = 'H'
    # Top cone
    for i in range(thickness):
        logging.info(((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1)))
    # Top pillars
    for i in range(thickness + 1):
        logging.info(((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)))
    # Middle belt
    for i in range((thickness + 1) // 2):
        logging.info(((c * thickness * 5).center(thickness * 6)))
    # Bottom pillars
    for i in range(thickness + 1):
        logging.info(((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)))
    # Bottom cone
    for i in range(thickness):
        logging.info((((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6)))