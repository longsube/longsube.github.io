def check_number(number):
    if number < 0:
        result = "This is negative number"
    elif number == 0:
        result =  " This is zero"
    elif number > 0:
        result =  "This is positive number"
    return result

input = 26
result = check_number(input)
print result

     
#result: This is positive number