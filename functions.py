def avg(marks):
    sum = 0
    for m in marks:
        sum = sum + m
    average = sum / len(marks)
    print(average)

avg(marks = [99, 89, 97, 95, 88])