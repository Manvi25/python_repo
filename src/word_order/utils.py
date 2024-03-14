from collections import Counter
def count_word_occurences():
    n = int(input("Enter the number of elements: "))
    l = []

    for i in range(n):
        l.append(input(f"Enter element {i + 1}: "))

    c = Counter(l)
    return ' '.join(str(value) for value in c.values())