# Code to determine if the student pass or fail.
student_name=input("Please input the student name")
subject1_=int(input ("Input the marks for maths"))
subject2_=int(input("Input the marks for physics"))
subject3_=int(input("Input the marks for chemistry"))
subject4_=int(input("Input the marks for chemistry"))
average=(subject1_ + subject2_ + subject3_+ subject4_)/4
# The while loop without the break function
# it makes the code running forever
# Running like so, constitute a logic error
while True:
    if average > 40:
       print( student_name + "  Has passed  ")
    elif average < 40:
       print (student_name + "  Has failed ")
