# Kyle S. Geltmaker
# Honor_Roll/Dean's_List_Checker
# A program that tests a student's GPA to see if they qualify for Honor Roll, Dean's List, or Nether

# Acquire student's last name or QUIT command.
student_LastName = input("Enter student's last name or ZZZ to quit: ")
# Test if student last name entered is QUIT command "ZZZ".
while student_LastName != "ZZZ":
    # Acquire student's first name.
    student_FirstName = input("Enter student's first name: ")
    # Acquire student's GPA.
    student_GPA = float(input("Enter student's GPA: "))
    # Test if GPA is greater than or equal to 3.5.
    if student_GPA >= 3.5:
        # If so, print confirmation of accomplishment.
        print("With a GPA of {}, {} {} has made the Dean's List.".format(str(student_GPA), student_FirstName, student_LastName))
    # Test if GPA is greater than or equal to 3.25.
    if student_GPA >= 3.25:
        # If so, print confirmation of accomplishment.
        print("With a GPA of {}, {} {} has made the Honor Roll.".format(str(student_GPA), student_FirstName, student_LastName))
    else:
        # Test if GPA is less than 3.25.
        if student_GPA < 3.25:
            # If so, print denial of accomplishment.
            print("With a GPA of {}, {} {} did not make the Honor Roll or Dean's List. Better luck next time.".format(str(student_GPA), student_FirstName, student_LastName))
    # Acquire student last name or QUIT command.
    student_LastName = input("Enter student's last name or ZZZ to quit: ")



