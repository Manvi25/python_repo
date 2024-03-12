
def calculate_average(records, student_name):
    if student_name in records:
        marks = records[student_name]
        average = sum(marks) / len(marks)
        logging.info(f'{average:.2f}')
    else:
        logging.info("Student not found.")
