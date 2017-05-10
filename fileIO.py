try:
	f = open('text', 'r')
	print(f.read())
finally:
	if f:
		f.close()

