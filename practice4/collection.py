# collection  = singele "Variable" used to store multiple values
#       List  = [] ordered and changeable. Duplicates OK
#       Set   = {} ordered and immutable, but Add?/Remove OK. NO Duplicates
#       Tuple = () oredered and uncahngeable. Duplicates OK. FASTER than List

fruits = ("apple", "orange", "banana", "coconut")
#print(dir(fruits))
#print(help(fruits))
#print(fruits[::-1])
#print(len(fruits))
#print("pineapple" in fruits)

#print(fruits.index("apple"))
print(fruits.count("coconut"))

#fruits.add("pineapple")
#fruits.remove("apple")
#fruits.pop()
#fruits.clear()

#fruits[1] = "pineapple"
#fruits.append("pineapple")
#fruits.remove("apple")
#fruits.insert(0, "pineapple")
#fruits.sort()
#fruits.reverse()
#fruits.clear()
#print(fruits.index(""))
#print(fruits.count("pineapple"))

print(fruits)
for fruit in fruits:
    print(fruit)