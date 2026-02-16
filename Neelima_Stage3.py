student_name = input("Enter the student's name: ")
mark1 = float(input("Enter the first mark: "))
mark2 = float(input("Enter the second mark: "))     
mark3 = float(input("Enter the third mark: "))  

total_marks = mark1 + mark2 + mark3     
percentage = (total_marks / 300) * 100
print(f"{student_name}'s total marks: {total_marks}")
print(f"{student_name}'s percentage: {percentage:.2f}%")

if percentage >= 75:        
    print(f"{student_name} has achieved an A grade.")
elif percentage >= 60:        
    print(f"{student_name} has achieved a B grade.")
elif percentage >= 40:        
    print(f"{student_name} has achieved a C grade.")    
else:
    print(f"{student_name} has achieved a F grade.")
    

