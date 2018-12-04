# first star

file = open('1_input.txt')

s = 0

for line in file:
	op = line[0]
	num = int(line[1:])
	if op == '+':
		s += num
	elif op == '-':
		s -= num
	print(op, num, s)

print(s)

# second star

s = 0
x = [0]
c = True

while True:
	file = open('2_input.txt')
	for line in file:
		op = line[0]
		num = int(line[1:])
		if op == '+':
			s += num
		elif op == '-':
			s -= num
		print(s)
		if s in x:
			print(s)
			c = False
			break
		else:
			x.append(s)
	if c == False:
		break