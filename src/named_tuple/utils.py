import logging
logging.basicConfig(level= logging.INFO, format= '%(message)s')
from collections import namedtuple
def named_tuple():
    num_students = int(input())
    columns = input().split()
    Student = namedtuple('Student', columns)
    average_marks = sum([int(Student(*input().split()).MARKS) for _ in range(num_students)]) / num_students
    logging.info(f"{average_marks:.2f}")