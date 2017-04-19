def binary(input):
    number = bin(input)[2:]
    number_cut = number[number.rfind('1'):]
    return number_cut

input = 24

number = binary(input)
print number

#result: 1000
