# conditional experession = A one-line for the if-else statement (ternary operator)
#                           Print or aasign one of two values based on a condition
#                           X if condition else Y

num = 7
a = 6
b = 7
age = 17
temperature = 19
user_role = "Alifio"


#print("Positive" if num > 0 else "Negative")
#result = "Even" if num % 2 == 0 else "ODD"
#max_num = a if a > b else b
#min_num = a if a < b else b
#status = "Adult" if age >= 18 else "Child"
#weather = "HOT" if temperature > 20 else "COLD"
acces_level = "Full acces" if user_role == "admin" else "Limited Acces"
print(acces_level)