# make a student database 
# print how many students are present today?
# make a list and use contiune

students = [
    "mohit",
    "john",
    "suresh",
    "rajendra",
    "steve",
    "alex",
    "michael",
]

absent_students = ["mohit", "alex", "rajendra"]
present_students = []

# Check if the student in absent list or not.
for student in students:
    if student in absent_students:
        continue 
    present_students.append(student)

# Display Data
if len(absent_students) == 1:
    print(f"Total {len(present_students)} students are present and {len(absent_students)} is absent")
else: 
    print(f"Total {len(present_students)} students are present and {len(absent_students)} are absent")
    
print(f"\nHere is List of Present Students: ")
for present_student in present_students:
    print(present_student.title())
    
print(f"\nHere is List of Absent Students: ")
for absent_student in absent_students:
    print(absent_student.title())
