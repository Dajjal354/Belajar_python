# fucntion = A block of code reuseable code
#            palce () after the function name to invoke it

#def happy_birtday(name, age):
    #print(f"Happy birthday to {name}!")
    #print(f"You are {age} years old!")
    #print("Happy birthday to you!")
    #print()

#happy_birtday("Bro", 20)
#happy_birtday("Aliffio", 19)
#happy_birtday("Nata", 15)

#def display_invoice(username, amount, due_date):
    #print(f"Hello {username}")
    #print(f"Your Bill of ${amount:.2f} is due: {due_date}")

#display_invoice("Aliffio", 43.90, "02/24")

# return = statement used to end a function
#          and send a result back to the caller

#def add(x, y):
    #z = x + y
    #return z

#def subtract(x, y):
    #z = x - y
    #return z

#def multiply(x, y):
    #z = x * y
    #return z

#def divide(x, y):
    #z = x / y
    #return z

#print(add(1, 2))
#print(subtract(1, 2))
#print(multiply(1, 2))
#print(divide(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Spongebob", "squarepants")

print(full_name)