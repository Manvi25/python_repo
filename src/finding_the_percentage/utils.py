def finding_the_percentage(student_marks, query_name):
    for key, value in student_marks.items():
        if key == query_name:
            average_score = sum(value) / len(value)
    print("{:.02f}".format(average_score))