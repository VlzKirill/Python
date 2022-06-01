x=[y**2 for y in range(1,11)]
y=x[:]
x.append(11)
y.append(12)
for xx in x:
	print (xx)
for yy in y:
	print (yy)