import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
def finding_the_percentage():
    n = int(input().strip())
    student_marks = {}
    for _ in range(n):
        name, *line = input().strip().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    return student_marks

def calculate_average_marks(student_marks, query_name):
    if query_name in student_marks:
        avg_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
        return avg_marks
    else:
        logging.error("Student name not found in records")

def average_marks():
    student_marks = finding_the_percentage()
    query_name = input().strip()
    avg_marks = calculate_average_marks(student_marks, query_name)
    if avg_marks:
        logging.info(f"{avg_marks:.2f}")
    else:
        logging.error("Failed to calculate average marks")
