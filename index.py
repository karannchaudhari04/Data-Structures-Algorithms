Emp = [
    (101, "Alice", 50000), 
    (102, "Bob", 65000), 
    (103, "Charlie", 55000)
]

EmpID = int(input("Enter Employee ID: "))

found = False

for emp in Emp:
    if emp[0] == EmpID:
        print(f"Employee ID Found: {emp}")
        found = True
        break

if not found:
    print("Employee ID does not found")