def power(x, n = 2):
	s = 1
	while n > 0:
		n -= 1
		s *= x
	return s

print(power(5, 3))

def enroll(name, gender, age = 6, city = 'Shanghai'):
	print('name:', name)
	print('gender:', gender)
	print('age:', age)
	print('city:', city)

enroll('XuJian', 'Male')

# only immutale variable can set a default parameter
def add_end(L = []):
	L.append('END')
	return L

print(add_end())
print(add_end())

# solution
def add_end_improved(L = None):
	if L is None:
		L = []
	L.append('END')
	return L

print(add_end_improved())
print(add_end_improved())
print(add_end_improved())
print(add_end_improved())


def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print(calc(1, 2, 3, 6))


def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)

person('XuJian', '23')

dicParam = {'brith': '1993', 'BoP': 'Xinxiang'}
person('XuJian', '23', **dicParam)


def f1(a, b, c = 0, *args, **kw):
	print('a = ', a, 'b = ', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c = 0, *, d, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


