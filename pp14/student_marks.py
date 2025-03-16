#elektroniczny dziennik z ocenami studentów
#wprowadzanie ocen
#wyświetlanie ocen wraz z wprowadzoną średnią

#students = {"Tomek" : [2,3,4], "Agata": [5,5,5]}

def average(marks):
    return sum(marks)/len(marks)
def get_data():
    students = {}
    while True:
        student = input("Podaj imię studenta: ")
        if student == "":
            break
        mark = float(input("Podaj ocenę: "))
        if mark <2 or mark >5:
            break
        if student in students:
            marks = students[student]
            marks.append(mark)
        else:
            marks = [mark]
        students.update({student: marks})
    return students
def print_summary(students):
    counter = 1
    for student in sorted(students.keys()):
        print(counter, student, students[student])
        counter +=1

print(get_data())
print_summary(get_data())





