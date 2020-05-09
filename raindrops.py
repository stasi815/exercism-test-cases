def check_num(number):
    if isinstance(number, int) or isinstance(number, float):
        return True
    else:
        return False

def convert(number):
    result = ""
    if check_num(number)==True:
        if number%3==0:
            result += "Pling"
        if number%5==0:
            result += "Plang"
        if number%7==0:
            result += "Plong"
        if result == "":
            return str(number)

        return result
    else:
        raise Exception("Please enter a valid integer.")

# "Tests Cases:"

# "normal input:"
# print(check_num(35))
# print(convert(35))
# print(convert(105))
# print(convert(8))

# "bad input:"
# print(check_num("s"))
# print(convert("a"))
# print(convert('345tg5'))


# "edge case input:"
# print(check_num(5.67))
# print(convert(5.67))
# print(convert(-35))





