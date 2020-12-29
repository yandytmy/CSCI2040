#python_version == '3.7'

def roman_to_decimal(roman):
    romanlist = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    for i in range(len(roman)):
        if i > 0 and romanlist[roman[i]] > romanlist[roman[i - 1]]:
            value += romanlist[roman[i]] - 2 * romanlist[roman[i - 1]]
        else:
            value += romanlist[roman[i]]
    return value
