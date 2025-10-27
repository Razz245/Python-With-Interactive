## 🎓 Student Grade Calculator with GPA

# Input section
print("=== Student Grade Calculator ===")
name = input("Enter student name: ")

# Dictionary for subjects and marks
subjects = {
    "Bangla": 0, "English": 0, "Math": 0, "Science": 0, "Social Science": 0,
    "Religion": 0, "ICT": 0, "Physical Education": 0, "Art": 0, "Music": 0,
    "Agriculture": 0, "Economics": 0
}

# Taking input for each subject
for sub in subjects:
    subjects[sub] = float(input(f"Enter marks for {sub}: "))

# Calculation section
total_marks = sum(subjects.values())
average = total_marks / len(subjects)

# Grade logic and GPA mapping
def get_grade_point(mark):
    if mark >= 80:
        return ("A+", 5.00)
    elif mark >= 70:
        return ("A", 4.00)
    elif mark >= 60:
        return ("A-", 3.50)
    elif mark >= 50:
        return ("B", 3.00)
    elif mark >= 40:
        return ("C", 2.00)
    elif mark >= 33:
        return ("D", 1.00)
    else:
        return ("F", 0.00)

# Individual grades and total GPA
total_gpa = 0
failed = False
print("\n=== Individual Subject Grades ===")
for sub, mark in subjects.items():
    grade, point = get_grade_point(mark)
    print(f"{sub}: {mark} → Grade: {grade}, GPA: {point}")
    total_gpa += point
    if grade == "F":
        failed = True

# Final GPA
gpa = total_gpa / len(subjects)

# Output section
print("\n=== Final Result Summary ===")
print("Name:", name)
print("Average Marks:", round(average, 2))
if failed:
    print("Grade: F (Failed in one or more subjects)")
    print("Final GPA: 0.00")
else:
    print("Final GPA:", round(gpa, 2))
    if gpa >= 5.00:
        print("Overall Grade: A+")
    elif gpa >= 4.00:
        print("Overall Grade: A")
    elif gpa >= 3.50:
        print("Overall Grade: A-")
    elif gpa >= 3.00:
        print("Overall Grade: B")
    elif gpa >= 2.00:
        print("Overall Grade: C")
    elif gpa >= 1.00:
        print("Overall Grade: D")
    else:
        print("Overall Grade: F")
print("=== End of Report ===")
print("Developed by Rajib Sharma")