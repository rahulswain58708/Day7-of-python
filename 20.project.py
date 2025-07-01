# Student Marks Report Generate.
def Student_report():
    print("------------Student Marks Report--------------")
    
    # Student information
    name = input("Enter student name: ")
    roll_number = int(input("Enter Student Roll number: "))
    
    # Subject marks input
    mark1 = float(input("Enter Student odia mark (0-100): "))
    mark2 = float(input("Enter Student English mark (0-100): "))
    mark3 = float(input("Enter Student math mark (0-100): "))
    mark4 = float(input("Enter Student physics mark (0-100): "))
    mark5 = float(input("Enter Student chemistry mark (0-100): "))

    # Total and percentage calculation
    total = mark1 + mark2 + mark3 + mark4 + mark5
    print(f"\nStudent Name: {name}")
    print(f"Roll Number: {roll_number}")
    print(f"Total Marks = {total} out of 500")
    
    percentage = total / 500 * 100
    print(f"Percentage = {percentage:.2f}%")

    # Grade logic
    if total >= 480:
        grade = "A"
    elif total >= 400:
        grade = "B"
    elif total >= 360:
        grade = "C"
    else:
        grade = "D"

    print(f"Grade: {grade}")

# Call the function
Student_report()
