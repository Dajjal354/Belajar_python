#logical operators = evaluate multiple conditions (or, and, not)
#                    or = at least one condition must be True
#                   and = both conditions must be True
#                   not = inverts the condition (not False, not True)

#or
#temp = 20
#is_raining = True

#if temp > 35 or temp < 0 or is_raining:
    #print("the outdoor event is cancelled")
#else:
    #print("The outdoor event is still scheduled")

#and 
temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is Cold Outside")
    print("It is SUNNY")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside")
    print("It is SUNNY")
elif temp >= 28 and not is_sunny:
    print("It is hot outside")
    print("It is Cloudy")
elif temp <= 0 and not is_sunny:
    print("It is Cold Outside")
    print("It is Cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside")
    print("It is Cloudy")
