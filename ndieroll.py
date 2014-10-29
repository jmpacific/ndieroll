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
# n -- number of times to roll the die
n = int(raw_input("How many times do you want to roll the %d-sided die? n = " % N))


for i in range(0, n):
	print random.randint(1,N)

