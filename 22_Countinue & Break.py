absent = [2, 5]
no = [6]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no:
        print("{0}".format(student))
        break
    print("{0}".format(student))

