# Program to calculate average marks of students

def calculate_average(marks)
    total = 0
    for i in range(len(marks)):
        total = total + marks[i]
    average = total / len(marks)
    return average

students = ["Alice", "Bob", "Charlie"]
marks = [85, 90, "78"]

avg = calculate_average(mark)
print("Average marks is: " + avg)

if avg > 80
    print("Grade: A")
else:
    print("Grade: B"
