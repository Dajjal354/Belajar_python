
#name = input("Enter your full name: ")
#phone_number = input("Enter your phone #: ")

#esult = len(name)
#result = name.find("o")
#result = name.rfind("q")
#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#result = name.isdigit()
#result = name.isalpha()
#result = phone_number.count("-")
#phone_number = phone_number.replace("-", "")

#print(phone_number)

#exercise
#1. username is no more than 12 characters
#2. username is must not contain spaces
#3. username must not contain digits

username = input("enter a username: ")



if len(username) > 12:
    print("Your username can't be than more 12 characters")
elif not username.find(" ") == -1:
    print("your username can't contain spaces")
elif not username.isalpha():
    print("your username can't contain number")
else:
    print(f"Welcome{username}")