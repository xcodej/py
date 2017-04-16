l = sorted([36, 5, -12, 9, -21])
print(l)
absL = sorted([36, 5, -12, 9, -21], key=abs)
print(absL)
strL = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(strL)

lowerStrL = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(lowerStrL)

reverseLowerStrL = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(reverseLowerStrL)

