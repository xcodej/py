class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
# bart = Student()
	def print_score(self):
		print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
print(bart.name,bart.score)
bart.print_score()
bart.age = 10
print(bart.age)
