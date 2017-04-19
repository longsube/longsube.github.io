prime_list = [1,2]
number = 3
check = True
while len(prime_list) < 10:
	#		for number in range (2, count):
	check = True
	for i in range (2, number):
		if number % i == 0:
			check = False
	if check == True:
		prime_list.append(number)
		number += 1
	else:
		number += 1

print prime_list


