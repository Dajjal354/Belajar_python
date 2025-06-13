# keyword arguments = an argument preceded by an indentifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional 2. default 3.KEYWORD 4. arbitrary

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=62, area=812, first=5932, last=7675)

print(phone_num)