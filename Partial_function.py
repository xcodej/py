i = int('12345', base=8)
print(i)
i = int('12345', 16)
print(i)

def int2(x, base=2):
	return int(x, base)

i2 = int2('1000000')
print(i2)
i2 = int2('1010101')
print(i2)

import functools
int2 = functools.partial(int, base=2)
i3 = int2('1000000')
print(i3)

