def divide_3_5(input):
	li = []
#input = 100
	for i in range(0, input):
		if i % 5 == 0 and i %3 == 0 and i %2 ==0:
			li.append(i)
#			print "%d == %d * 5" %(i,i/5)
	return li

input = 1000
li = divide_3_5(input)
print li
su = sum(li)
print su

#result: 
# [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900, 930, 960, 990]
# 16830