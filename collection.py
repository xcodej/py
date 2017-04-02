classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
len(classmates)

# fetch the last element of the list
print(classmates[-1])

# list is a mutable ordered table.
classmates.insert(1, 'Jack')
print(classmates)

# use pop() to remove the last element of the list
print(classmates.pop())
print(classmates)

# use pop(index) to remove list[index]
print(classmates.pop(1))
print(classmates)

# tuple like a immutable list
familyMembers = ('Father', 'Mother', 'Little new')
print(familyMembers[-1])

# tuple trap : t = (1) defines a integer 
t = (1)
# t = (1,) means a tuple that only contains one element
t = (1,)

