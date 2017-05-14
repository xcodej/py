try:
	f = open('text', 'r')
	print(f.read())
finally:
	if f:
		f.close()

with open('text','r') as f:
	print(f.read())


for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉

try:
	f - open('text', 'w')
	f.write('Hello, world!')
finally:
	if f:
		f.close()
