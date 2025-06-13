# Match-case statement (switch): An alternative to using many 'elif' statement
#                                Execute some code if a value matches\(==) a 'case'
#                                Benefits: cleaner and syntax is more readable
#                                or can be replace with (|)

def is_weekend(day):
    match day:
        case "sunday" | "saturday":
            return True
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return False
        case _:
            return "Its not valid"

print(is_weekend("sunday"))
