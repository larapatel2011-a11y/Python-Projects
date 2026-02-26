subjects = {}

for i in range (4):
    subject = input("Choose a subject: ")
    marks = int(input("Enter how many marks: "))
    subjects[subject]=marks
print(subjects)

count = 0

for value in subjects.values():
    print(value)
    count = count+value

print(count)