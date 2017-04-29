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


class Student_limit(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
	def set_score(self,score):
		self.__score = score
bart = Student_limit('Bart Simpson', 98)
bart.__name


# extends
class Animal(object):
	def run(self):
		print('Animal is running')

class Dog(Animal):
	pass

class Cat(Animal):
	pass

dog = Dog()
dog.run()

cat = Cat()
cat.run()


