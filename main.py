medical_cause = str(input("Do you have any medical history: "))
attendance = int(input("Please enter your daily attendance: "))
if medical_cause == "Y":
    print("You can take the exam.")
    
else:
    if attendance > 75:
        print("You can take the exam because of your attendance.")
    else:
        print("You cannot take the exam.")