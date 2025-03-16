from employee import Employee

employees = []
employees.append(Employee("Jan", "Kowalski", 25, 4500))
employees.append(Employee('Edmund', 'Kaczmarczyk', 32, 5500))
employees.append(Employee('Agata', 'Nowak', 38, 8500))

print("Lista płac")
print("_"*30)
for employee in employees:
    print(employee.get_salary())


