# hacker-statistics-to-calculate-your-chances-of-winning-a-bet
Case Study: Hacker Statistics_random number generators, loops, and Matplotlib in Python
You are taking a stairs in empire state building and playing a game with your friend. You throw a die one hundred times.
If it's 1 or 2 you'll go one step down. If it's 3, 4, or 5, you'll go one step up.
If you throw a 6, you'll throw the dice again and will walk up the resulting number of steps. Of course, you can not go lower than step number 0. And also, you admit that you're a bit clumsy and have a chance of 0.1% of falling down the stairs when you make a move. Falling down means that you have to start again from step 0. With all of this in mind, you bet with your friend that you'll reach 60 steps high.
What is the chance that you will win this bet?

One way to solve this problem is Analytically.
What is the chance that you will win this bet? It's a complex assignment. One way to solve it would be to calculate the chance analytically using equations. Another possible approach, is to simulate this process thousands of times, and see in what fraction of the simulations that you will reach 60 steps. This is a form of -hacker statistics-. As you can probably guess, we're going to opt for the second approach.

9. Random generators
The first thing we'll need are random generators, so we can simulate the die. You need to import numpy, and inside numpy, there is the random package. Inside that package we find the "rand" function. Let's try it out: we get a random number between zero and one. How was this random number created? Well, computers typically generate so-called pseudo-random numbers. Those are random numbers that are generated using a mathematical formula, starting from a random seed. This seed was chosen by Python when we called the rand function, but you can also set this manually. Suppose we set it to 123, just a number I chose, like this, and then call the rand function twice. We get two random numbers.

10. Random generators
Now, if I set the seed back to 123, and call rand twice more, we get the exact same random numbers. This is funky: you're generating random numbers, but for the same seed, you're generating the same random numbers. That's why it's called pseudo-random; it's random but consistent between runs; this is very useful, because this ensures "reproducibility". Other people can reproduce your analysis. Let's use this randomness in a new example now.

11. Coin toss
Suppose we want to simulate a coin toss. First set the seed - again, this could be anything - and then use the randint() function. To have it randomly generate either 0 or 1, we pass two arguments: the first argument should be 0, the second one 2, because 2 is not going to be included. If we print out coin, and then run the script, we get a random integer, 0. You can now use this coin to play a game.

12. Coin toss
We extend the code with an if-else statement: if coin equals 0, we print out "heads". If it equals 1, we print out "tails". If we now run this script again, coin will again equal 0, because the seed is the same. This also means that the if condition is True, so the string heads is printed out. This was a first example on how you can use random numbers to simulate real life situations that involve chance, or probability.


If you use a dice to determine your next step, you can call this a random step. What if you use a dice 100 times to determine your next step? You would have a succession of random steps, or in other words, a random walk.

3. Random Walk
This is a well known concept in science. For example, the path traced by a molecule as it travels in a liquid or a gas can be modeled as a random walk. The financial status of a gambler is another example. To record every step in your random walk, you need to learn how to gradually build a list with a for loop.

4. Heads or Tails
Have a look at this code. It keeps the outcomes for playing a game of heads or tails ten times, with the random number generator we coded up in the previous video. After importing numpy and setting a seed for the random number generator, we initialize an empty list "outcomes". Next, we build a for loop that should run ten times. We can do this with the range() function, that generates a list of numbers that you can use to iterate over. Inside this for loop, we generate a random integer coin that's either zero or one. Zero corresponds to heads, 1 to tails. If coin is zero, we append the string heads to the list. Else, we append the string tails. In both cases, we do this with the append method, which you learned about in the intro course. Finally, we print the outcomes list we've built up in these 10 iterations. If we run this script, eventually a list with 10 strings will be printed out. This list is random, but it's not a random walk, because the items in the list are not based on the previous ones. It's just a bunch of random steps.

5. Heads or Tails: Random Walk
You could turn this example into a random walk by tracking the -total- number of tails while you're simulating the game. In this case, you start by creating a list, tails, that already contains the number 0, because at the start, you haven't thrown any tails. Then you again start a for loop that runs 10 times, using the range function. In there, you again generate a random number. Instead of the if-else structure, you can simplify things. If coin is 0, so heads, the number of tails you've thrown shouldn't change. If a 1 is generated, the number of tails should be incremented with 1. This means that you can simply add coin to the previous number of tails, and add this count to the list with append. Finally, you again print the list tails. After running this script, a list with 11 elements will be printed out. The final element in this list tells you how often tails was thrown.

6. Step to Walk
If you compare the output of the first script to the output of the second script, you can see that the numbers in the tails list are incremented by one each time you threw tails. This is exactly how a bunch of random steps are converted into a random walk.




