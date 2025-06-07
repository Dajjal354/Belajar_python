# dictionary = a collection of {key:value} pairs
#            = ordered and changeable. No duplicates

capitals = {"Indonesia": "Jakarta",
            "India": "New Delhi",
            "Denmark" : "Koppenhagen",
            "China": "Beijing"}

#print(dir(capitals))

#print(capitals.get("Japan"))

#if capitals.get("China"):
 #   print("That capital exist")
#else:
 #   print("That capital doesn't exist")

#capitals.update({"Germany": "Berlin"})
#capitals.update({"Indonesia": "Detroit"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()

#keys = capitals.keys()

#for key in capitals.keys():
    #print(key)

#values = capitals.values()
#for value in capitals.values():
    #print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")