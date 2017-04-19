#3.1
def binary(input):
    try:
        number = bin(input)[2:]
        number_cut = number[number.rfind('1'):]
        return number_cut
except TypeError:
    print "Require a number"


#3.2
def check_number(number):
    try:
        if number < 0:
            result = "This is negative number"
        elif number == 0:
            result =  " This is zero"
        elif number > 0:
        result =  "This is positive number"
        return result
    except TypeError:
        print "Require a number"

#3.3
def output(start,end,i):
    try:
        ran = range(start,end,i)

        for count in range(0, len(ran)- 1):
            print "{0} {1}".format(ran[count], ran[count + 1])

    except TypeError:
    print "Require a range"      