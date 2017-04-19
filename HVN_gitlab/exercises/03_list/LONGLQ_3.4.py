def output(start,end,i):
    ran = range(start,end,i)

    for count in range(0, len(ran)- 1):
        print "{0} {1}".format(ran[count], ran[count + 1])
    
li = (1,10,1)
output(1,10,1)

# result: 
# 1 2
# 2 3
# 3 4
# 4 5
# 5 6
# 6 7
# 7 8
# 8 9




