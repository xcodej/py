from functools import reduce
def add(x, y):
	return x + y
tmp = reduce(add, [1, 3, 5, 7, 9])
print(tmp)

def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn, map(char2num,s))
print(str2int('12345'))

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def lStr2int(s):
	reduce(lambda x, y: x * 10 + y, map(char2num, s))

print(lStr2int('12345'))

