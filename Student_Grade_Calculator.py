try:
    name = input("Enter the student's name: ")

    marks = [(input("Enter marks for subject 1: ")), (input("Enter marks for subject 2: ")), (input("Enter marks for subject 3: "))]

    marks = [int(mark) for mark in marks]

    if marks[0] < 0 or marks[0] > 100 or marks[1] < 0 or marks[1] > 100 or marks[2] < 0 or marks[2] > 100:
        print("Error: Marks should be between 0 and 100.")
        exit()
except ValueError:
    print("Error: Please enter valid integer marks.")
    exit()
    
total_marks = sum(marks)
average_marks = total_marks / len(marks)

if average_marks >= 80:
    grade = "A+"
elif average_marks >= 70:
    grade = "A"
elif average_marks >= 60:
    grade = "B"
elif average_marks >= 50:
    grade = "C"
else:
    grade = "F"

print(f"Student Name: {name}")
print(f"Total Marks: {total_marks}")
print(f"Average: {average_marks:.2f}")
print(f"Grade: {grade}")
