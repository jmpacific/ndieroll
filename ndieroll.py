import random

print """
Welcome to the N-Die-Roll simulator.
You will be asked to supply 'N', the
number of sides for the die, and 'n',
the number of times to roll said N-sided
die.
"""
# N -- max integer on the die
N = int(raw_input("How many sides does the die have? N = "))

# while improper number of sides is given, prompt for proper input
while N <= 0:
	N = int(raw_input("Please provide a positive integer for the number of sides. N = "))

# n -- number of times to roll the die
n = int(raw_input("How many times do you want to roll the %d-sided die? n = " % N))

# while improper input is given, prompt for proper input
while n <= 0:
	n = int(raw_input("A postive integer value is required for the number of rolls. n = "))

print "The following are %d simulated die rolls of a %d-sided die:" % (n,N)

for i in range(0, n):
	print random.randint(1,N)

