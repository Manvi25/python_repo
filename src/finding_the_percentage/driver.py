import logging
logging.basicConfig(level=logging.INFO,format='%(message)s')
from utils import calculate_average

if __name__ == '__main__':
    n = int(input("Enter the number of students' records: "))
    student_marks = {}
    for _ in range(n):
        name, *line = input("Enter name and marks separated by space: ").split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input("Enter the name of the student to query: ")
    result = calculate_average(student_marks, query_name)
    logging.info(result)
