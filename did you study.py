did_you_study = str(input("Did you study for the Mid-Term? Type yes or no: "))
yes = ("yes")
no = ("no")
if did_you_study == yes:
    print("Good Job Mate!")
    print("--------------")
    print("Go play games!")
    exit()
else:
    print("Well then...")
    print("-------------")
    print("You're truly fucked!")
      
study_now = str(input("Did you study yet?"))             
while study_now == yes:
    print("Finally!")
    exit()
    
if study_now == no:
    print("You're Hopeless!")

