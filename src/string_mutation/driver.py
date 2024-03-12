from utils import string_mutation
import logging
logging.basicConfig(level= logging.INFO, format= '%(message)s')

s = input().strip()
position, character = map(str, input().split())
result = string_mutation(s, int(position), character)
logging.info((result))