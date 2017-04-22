l = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l)

def f(x):
	return x * x

def build(x, y):
    return lambda: x * x + y * y
