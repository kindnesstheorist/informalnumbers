# If formality is False, the function will attempt to construct an informal
# phrase for the number. Formality affects only numbers from 100 to 10000, with
# the exception of 100,000, which has an informal variant. Negative and non-
# integer numbers will always be formal. Numbers with an absolute value of one
# million or higher will be converted to strings with Python's built-in
# function. Non-number input will cause a crash.
#
# Decimal functionality not tested with non-US locales.
def word(number, formality=True):
    if number != int(number):
        letters = str(number)
        parts = letters.split(".")
        constructed = word(int(parts[0])) + " point"
        for letter in parts[1]:
            constructed = constructed + " " + word(int(letter))
        return constructed
    if number < 0:
        return "negative " + word(abs(number))
    if number == 0:
        return "zero"
    if number == 1:
        return "one"
    if number == 2:
        return "two"
    if number == 3:
        return "three"
    if number == 4:
        return "four"
    if number == 5:
        return "five"
    if number == 6:
        return "six"
    if number == 7:
        return "seven"
    if number == 8:
        return "eight"
    if number == 9:
        return "nine"
    if number == 10:
        return "ten"
    if number == 11:
        return "eleven"
    if number == 12:
        return "twelve"
    if number == 13:
        return "thirteen"
    if number == 15:
        return "fifteen"
    if number == 18:
        return "eighteen"
    if number < 20:
        return word(number%10) + "teen"
    if number == 20:
        return "twenty"
    if number == 30:
        return "thirty"
    if number == 40:
        return "forty"
    if number == 50:
        return "fifty"
    if number == 60:
        return "sixty"
    if number == 70:
        return "seventy"
    if number == 80:
        return "eighty"
    if number == 90:
        return "ninety"
    if number < 100:
        return word(truncate(number, 10)) + "-" + word(number%10)
    if number == 100:
        if formality:
            return "one hundred"
        else:
            return "a hundred"
    if number < 1000:
        if exact(number, 100):
            return word(int(number/100)) + " hundred"
        if formality:
            separator = " hundred "
        else:
            separator = " hundred and "
        return word(int(number/100)) + separator + word(number%100)
    if number == 1000:
        if formality:
            return "one thousand"
        else:
            return "a thousand"
    if number < 1020:
        if formality:
            separator = " "
        else:
            separator = " and "
        return word(1000, formality) + separator + word(number%1000)
    if number < 2000:
        if not formality and exact(number, 100):
            return word((int(number/100))) + " hundred"
    if number == 100000:
        if not formality:
            return "a hundred thousand"
    if number < 1000000:
        if exact(number, 1000):
            return word((int(number/1000))) + " thousand"
        if not formality:
            if number < 10000 and number%1000 < 100 and exact(number, 10):
                return word(truncate(number, 1000), formality) + " and " + word(number%1000)
        return word(int(number/1000)) + " thousand " + word(number%1000)
    return str(number)

def truncate(number, precision):
    return number-number%precision

def exact(number, precision):
    return number == truncate(number, precision)

