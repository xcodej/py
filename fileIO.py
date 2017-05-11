try:
	f = open('text', 'r')
	print(f.read())
finally:
	if f:
		f.close()

with open('text','r') as f:
	print(f.read())
