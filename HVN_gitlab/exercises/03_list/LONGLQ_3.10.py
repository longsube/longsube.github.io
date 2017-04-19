def ten_prime(input):
	prime_list = [1,2]
	number = 3
	check = True
	while len(prime_list) < input:
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


ten_prime(10)
    	
#result: [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]