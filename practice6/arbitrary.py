# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#           * unpacking operator
#            1. positional, 2. default, 3.keyword, 4.ARBITRARY

#def add(*args):
    #total = 0
    #for arg in args:
        #total += arg
    #return total

#print(add(1, 2, 3, 4, 5))

#def display_name(*args):
    #for arg in args:
        #print(arg, end=" ")

#display_name("DR.", "Muhammad", "Aliffio", "Faroldi")

#def print_address(**kwargs):
    #for key, value in kwargs.items():
        #print(f"{key}: {value}")

#print_address(street="354 street",
              #blok="U49",
              #city="Surabaya", 
              #state="jawa Timur", 
              #zip="54321")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    
    if "perum" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('perum')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Aliffio", "Faroldi", "I",
               street="124 fake st",
               pobox="PO box #U49",
               city="Surabaya",
               state="East Java",
               zip="123456")