names = ['James', 'Claire', 'Tommy', 'Jimmmy', 'Paulie']

count = 0
for i in range(20,25):
	print "My name is {0} and I am {1} years old.".format(names[count], i)
	count += 1

for j in range(10,-1,-1):
	print j,

p = 10
while p >= 0:
	print p,
	p -= 1

print " ".join([str(i) for i in range(10,-1,-1)])