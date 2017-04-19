def one_time_chars(input):
#input = "cho meo ga chuot vit ngan"
	li = []
	for char in input:
		cnt = input.count(char)
		if cnt == 1:
 			li.append(char)
	return li
	

input = "cho meo ga chuot vit ngan"
li = one_time_chars(input)
print li

#result: ['m', 'e', 'u', 'v', 'i']
