def electric_fee(input):
	if input <= 50:
		fee = input * 1230
	elif 50 < input <= 100:
		fee = 50 * 1230 + (input - 50)* 1530
	elif input > 100:
		fee = 50*1230 + 50*1530 + (input-100)*1786
	return fee


def month_electric(input):
	sum_bills = []
	for i in input:
		month_fee = electric_fee(i)
		sum_bills.append(month_fee)
	return sum_bills



input = 50
bill = electric_fee(input)
print bill


li = [1, 29, 1235, 69, 100]
sum_bills = month_electric(li)
print sum_bills

#result: [1230, 35670, 2165110, 90570, 138000]