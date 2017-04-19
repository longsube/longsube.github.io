def cut_sls(input):

	after_cut = input.split('...sls')
	after_join = '...'.join(after_cut)
	return after_join


input = '....slsslslsls...sls'
print cut_sls(input)
 

 #result: ....slslsls...