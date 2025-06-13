# Membership operators = used to test wheter a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

#word = "APPLE"

#letter = input("guess the letter in the secret word: ")

#if letter not in word:
    #print(f"{letter} was not found")
#else:
    #print(f"There is a {letter}")

#students = {"Aliffio", "Iqbal", "Nata"}

#student = input("enter the name of a stydent: ")

#if student not in students:
    #print(f"{student} was not found")
#else:
    #print(f"{student} is a students")

#grades = {"Aliffio": "A", 
          #"Dajjal": "B", 
          #"Iqbal": "C", 
          #"Nata": "E"}


#student = input("Enter the name of student: ")

#if student in grades:
    #print(f"{student}'s grade is {grades[student]}")
#else:
    #print(f"{student} was not found")

email = "dajjal@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")