from classes.school import School 



school = School('Ridgemont High') 

while True:
   choice =  input("""
    What would you like to do?
Options:
    1.List all Students
    2.View Individul Student <student_id>
    3. Add a Student
    4.Remove a student <student_id>
    5.Quit 
""")
   if choice == '1':
        school.list_students()
   elif choice =='2':
       student_id = input ("Enter student id: \n")
       student = school.find_student_by_id(student_id)
       print(student)
   elif choice == '5':
        print("Goodbye!")
        break
        
     