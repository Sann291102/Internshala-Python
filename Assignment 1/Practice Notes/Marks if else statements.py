marks = int(input())
grade = 'A' if marks >= 90 else 'B' if marks >= 80 else 'B+' if marks >= 70 else 'C' if marks >=60 else 'D' if marks >= 45 else 'F'
print(f"Your grade is: {grade}")
