var = -1
while var != 'q':
	var = raw_input ("Enter something, or 'q' to quit: ")
	print var
	if var == 'q':
		break
	print 'looping'
print 'Bye'