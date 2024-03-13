import logging


def print_formatted():
    number = int(input())
    width = len(bin(number)[2:])
    ans = '\n'
    #logging.basicConfig(level=logging.INFO, format='%(message)s')
    for i in range(1, number + 1):
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexadecimal = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        #logging.info(f"{decimal} {octal} {hexadecimal} {binary}")
        ans += f"{decimal} {octal} {hexadecimal} {binary}\n"
    return ans