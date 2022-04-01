# Import numpy as np
import numpy as np

# Set the seed
#seed(): sets the random seed, so that your results are reproducible between simulations. 
#As an argument, it takes an integer of your choosing. 
#If you call the function, no output will be generated.

np.random.seed(123)

# Generate and print random float
#rand(): if you don't specify any arguments, it generates a random float between zero and one.

print(np.random.rand())

#randint(), also a function of the random package, to generate integers randomly. The following call generates the integer 4, 5, 6 or 7 randomly. 8 is not included.

import numpy as np
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))

#your next move depends on the number of eyes you throw with the dice. 
#If dice is 1 or 2, you go one step down.
#if dice is 3, 4 or 5, you go one step up.
#Else, you throw the dice again. The number of eyes is the number of steps you go up.
#Print out dice and step. Given the value of dice, was step updated correctly?


# NumPy is imported, seed is set
import numpy as np
# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice >2 and dice<=5:
    step = step+1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)


