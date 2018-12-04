# first star

# file = open('2_input.txt')

# three = 0
# two = 0

# for line in file:
# 	d = {}
# 	for c in line:
# 		if c in d:
# 			d[c] += 1
# 		else:
# 			d[c] = 1
# 	dthree = False
# 	dtwo = False
# 	for i in d:
# 		if d[i] == 3 and dthree == False:
# 			three += 1
# 			dthree = True
# 		if d[i] == 2 and dtwo == False:
# 			two += 1
# 			dtwo = True

# print(three * two)

# second star

file = open('2_input.txt')
x = list(file)
x = [i.replace('\n', '') for i in x]
a, b = '', ''

lenx = len(x)
for i in range(0, lenx):
	for j in range(i + 1, lenx - 1):
		st1 = x[i]
		st2 = x[j]
		leni = len(st1)
		c = 0
		for ii in range(0, leni):
			if st1[ii] != st2[ii]:
				c += 1
		if c == 1:
			print(st1, st2)
		