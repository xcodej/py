d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d['Adam'] = 67
d['Jack'] = 90
d['Jack'] = 89
for kvc in d:
	print("%s : %d" % (kvc, d[kvc]))
print('Thomas' in d)
print(d.get('Thomas'))
print(d.get('Thomas', -1))
d.pop('Bob')
print(d)
