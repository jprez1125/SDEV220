#jennifer perez
#student_qualification_app
#this app takes in students names and GPAs
#it will then determine if the student is qualified for the deans list or for honor roll
#the program stops when the user enters 'zzz'

while True:
    last_name =input("Enter the student's last name or 'ZZZ' to quit process: " ) 
    if last_name.upper( )=="ZZZ":
        print("Exiting program")
        break
    first_name =input("Enter the student's first name: ")
    gpa=float(input("Enter the student's GPA: "))
    if gpa >=3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >=3.25:
        print(f"{first_name} {last_name} has made Honor Roll.")
    else:
        print(f"{first_name} {last_name} has not made the Dean's List or the Honor Roll.")

