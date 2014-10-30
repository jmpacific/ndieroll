# ndieroll.py
#
# N-Die-Roll simulator
#
# by jmpacific
import random
import sys

def getDieRolls(N,n):
# returns a list of n die rolls of die with N number of sides.
    results = []    

    for i in range(0,n):
        results.append(random.randint(1,N))

    return results
# end def getDieRolls()

def userInput():
# Ask user for the number of sides for simulated die
# Ask user for the number of times to roll a die with sides N

    # N -- max integer on the die
    N = int(raw_input("How many sides does the die have? N = "))

    # while improper number of sides is given, prompt for proper input
    while N <= 0:
        N = int(raw_input("Please provide a positive integer for the number of sides. N = "))

    isPlatonic(N)
        

    # n -- number of times to roll the die
    n = int(raw_input("How many times do you want to roll the %d-sided die? n = " % N))

    # while improper input is given, prompt for proper input
    while n <= 0:
        n = int(raw_input("A postive integer value is required for the number of rolls. n = "))

    return(N,n)
# end def userInput()

def isPlatonic(x):
# Checks to see if the number of sides for the die is a Platonic solid
    if x not in [4,6,8,12,20]:
        print "This is not a Platonic solid; just saying..."

def promptQuit():
    choice = raw_input("Do you want to roll again? (yes/no) ")
    while choice != 'yes' and choice != 'no':
        choice = raw_input("Please answer 'yes' or 'no': ")
    return choice
# end def promptQuit()

def runDieSim(x):

    rolls = getDieRolls(x[0],x[1])

    print "The die rolls are:"
    for i in rolls:
        print i

# end def runDieSim()

#####
# Run the simulator given no command line arguments
#####

if len(sys.argv) >= 3:
    print "\nUsing command line arguments for dies sides and rolls..."
    x = []
    x.append(int(sys.argv[1]))
    x.append(int(sys.argv[2]))
    isPlatonic(x[0])
    runDieSim(x)
else:

    print """
    Welcome to the N-Die-Roll simulator.
    You will be asked to supply 'N', the
    number of sides for the die, and 'n',
    the number of times to roll said N-sided
    die.
    """

    rollAgain = 'yes'

    while rollAgain == 'yes':

        x = userInput()
        runDieSim(x)

        rollAgain = promptQuit()
