# Version 1.1 - Practising Git change tracking
def Add_Student(Students):
    while True:
        name = input("Name of student: ").strip()
        if name.strip() == "" or name.isdigit() == True:
            print("Invalid name. Please enter a valid name.")
            continue  
        else:
            break
    subject = ["Python", "DBMS", "Math", "Computer Network", "Statistic"]
    marks = {}
    for sub in subject:
        while True:
            try:
                mark = float(input(f"Enter the mark for {sub}: "))
                if mark < 0 or mark > 100:
                    print("Mark must be between 0 and 100.")
                    continue
                else:
                    marks[sub] = mark
                break
            except ValueError:
                print("Mark must be integer or float.")
    Students.append({"Name" : name, "marks" : marks})

def display_result(Students):
  if len(Students) == 0:
      print("No students found.")
      return
  else:
    total_students = len(Students)
    total_marks = 0
    top_student = Students[0] if total_students > 0 else None
    for index, student in enumerate(Students):
        total_mark = 0
        # Directly access the keys inside each expense dictionary
        print(
            f"Student {index + 1} : {student['Name']}"
        )
        for sub, mark in student['marks'].items():
            print(f"    •{sub} : {mark}/100")
            total_mark += mark
        total_marks += total_mark
        # Calculate top grade student
        if top_student is None or total_mark > sum(top_student['marks'].values()):
            top_student = student
        # Calculate percentage and grade
        percentage = total_mark / (len(student['marks']) * 100) * 100
        print(f"    Total Marks: {total_mark} / {len(student['marks']) * 100}")
        print(f"    Percentage: {percentage:.2f}%")
        if percentage >= 90 and percentage <= 100:
            print("    Grade: A+")
        elif percentage >= 80 and percentage < 90:
            print("    Grade: A")
        elif percentage >= 70 and percentage < 80:
            print("    Grade: B+")
        elif percentage >= 60 and percentage < 70:
            print("    Grade: B")
        elif percentage >= 50 and percentage < 60:
            print("    Grade: C+")
        elif percentage >= 40 and percentage < 50:
            print("    Grade: C")
        else:
            print("    Grade: F")
        
        print("_" *30)
    class_average = total_marks / (total_students * len(student['marks']))
    print(f"Class Average: {class_average:.2f}%")
    if top_student:
        print(f"Top Student: {top_student['Name']} with {sum(top_student['marks'].values())} marks")

def main():
    Students = []
    while True:
        print("1. Add Student")
        print("2. View Results")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice : "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        match choice:
            case 1:
                Add_Student(Students)
                continue
            case 2:
                display_result(Students)
                continue
            case 3:
                break
            case _:
                print("Invalid choice")
                continue


if __name__ == "__main__":
    main()
            
            
# Feature: student average calculation
# Project maintained and version-controlled with Git