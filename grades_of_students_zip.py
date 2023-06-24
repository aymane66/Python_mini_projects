student_names = [
    "John Smith", "Emily Johnson", "Michael Williams", "Sarah Brown", "David Taylor",
    "Jessica Davis", "Matthew Anderson", "Olivia Martinez", "Christopher Thomas", "Sophia Rodriguez",
    "Daniel Wilson", "Ava Taylor", "James Garcia", "Mia Thomas", "Joseph Davis",
    "Emma Martinez", "Jacob Anderson", "Abigail Johnson", "William Smith", "Sophia Taylor",
    "Alexander Davis", "Emily Anderson", "Michael Johnson", "Ella Brown", "Daniel Wilson",
    "Olivia Garcia", "Matthew Smith", "Grace Johnson", "David Anderson", "Isabella Davis",
    "Andrew Taylor", "Sofia Williams", "Joseph Martinez", "Charlotte Wilson", "Christopher Davis",
    "Avery Thomas", "Mia Martinez", "Samuel Smith", "Scarlett Johnson", "Logan Brown",
    "Evelyn Anderson", "Jacob Taylor", "Victoria Davis", "Jackson Johnson", "Emily Wilson",
    "Ethan Thomas", "Harper Smith", "Benjamin Anderson", "Amelia Garcia", "Michael Martinez",
    "Liam Davis", "Elizabeth Taylor", "Daniel Smith", "Mila Johnson", "Matthew Brown",
    "Avery Anderson", "Sofia Wilson", "Joseph Thomas", "Ella Davis", "Oliver Johnson",
    "Sophia Taylor", "Alexander Davis", "Emily Anderson", "Michael Johnson", "Ella Brown",
    "Daniel Wilson", "Olivia Garcia", "Matthew Smith", "Grace Johnson", "David Anderson",
    "Isabella Davis", "Andrew Taylor", "Sofia Williams", "Joseph Martinez", "Charlotte Wilson",
    "Christopher Davis", "Avery Thomas", "Mia Martinez", "Samuel Smith", "Scarlett Johnson",
    "Logan Brown", "Evelyn Anderson", "Jacob Taylor", "Victoria Davis", "Jackson Johnson",
    "Emily Wilson", "Ethan Thomas", "Harper Smith", "Benjamin Anderson", "Amelia Garcia",
    "Michael Martinez", "Liam Davis", "Elizabeth Taylor", "Daniel Smith", "Mila Johnson",
    "Matthew Brown"
]


grades = [
    18, 15, 19, 14, 20, 16, 17, 13, 19, 12,
    14, 16, 17, 18, 15, 13, 16, 19, 20, 14,
    15, 18, 19, 17, 13, 16, 12, 15, 18, 20,
    14, 17, 19, 16, 13, 15, 18, 20, 19, 14,
    16, 17, 12, 19, 15, 18, 16, 20, 14, 13,
    17, 19, 15, 18, 14, 16, 17, 20, 13, 19,
    15, 18, 14, 16, 17, 12, 19, 15, 18, 16,
    14, 17, 20, 13, 19, 15, 18, 14, 16, 17,
    12, 19, 15, 18, 14, 16, 17, 20, 13, 19,
    15, 18, 14, 16, 17, 12, 19, 15, 18, 16
]


observations = [
    "Excellent", "Average", "Improving", "Inconsistent", "Outstanding",
    "Satisfactory", "Promising", "Struggling", "Good", "Needs improvement",
    "Outstanding", "Average", "Improving", "Inconsistent", "Excellent",
    "Promising", "Satisfactory", "Good", "Needs improvement", "Outstanding",
    "Good", "Improving", "Inconsistent", "Excellent", "Promising",
    "Average", "Satisfactory", "Needs improvement", "Struggling", "Outstanding",
    "Promising", "Satisfactory", "Good", "Inconsistent", "Excellent",
    "Improving", "Outstanding", "Average", "Needs improvement", "Struggling",
    "Promising", "Satisfactory", "Good", "Excellent", "Improving",
    "Inconsistent", "Outstanding", "Needs improvement", "Average", "Satisfactory",
    "Promising", "Good", "Struggling", "Outstanding", "Excellent",
    "Improving", "Inconsistent", "Satisfactory", "Needs improvement", "Good",
    "Outstanding", "Promising", "Improving", "Excellent", "Satisfactory",
    "Inconsistent", "Good", "Needs improvement", "Outstanding", "Struggling",
    "Promising", "Average", "Excellent", "Improving", "Satisfactory",
    "Outstanding", "Good", "Inconsistent", "Needs improvement", "Promising",
    "Average", "Struggling", "Excellent", "Outstanding", "Improving"
]

numbers = 0
for name, grade, observation in zip(student_names, grades, observations):
    numbers += 1
    print(f"Student number {numbers}:\nStudent name: {name}\nGrade: {grade}/20\nTeacher´s observation: {observation}\n")
