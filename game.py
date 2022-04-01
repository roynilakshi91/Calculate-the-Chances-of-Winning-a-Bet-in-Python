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

#random walk

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]
    print(x)

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0,step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)

#Visualize the walk
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()

#Distribution
#To get an idea about how big your chances are of reaching 60 steps, you can repeatedly simulate the random walk and collect the results.
# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)


# numpy and matplotlib imported, seed set.


# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
#Transposing the 2D NumPy array was crucial; otherwise Python misunderstood.
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()
