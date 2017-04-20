def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

<<<<<<< HEAD

=======
f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
>>>>>>> c3404955f80cbead7cc61978e56e8b1c72de0688
