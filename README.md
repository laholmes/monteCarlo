# monteCarlo
Monte Carlo simulations + stochastic calculus playground in python

simple_bettor makes wagers which win based on random number (1-100, 51-99 is a win)
it runs the simulation for 100 bettors, all starting with 10000, betting 100 each round, and betting until broke or 10000 rounds reached.

plotting_bettor is as above, but plots the results using matplotlib

martingale_bettor doubles current wager when the bettor lost in the previous round. also includes a multiple_bettor strategy which randomises the multiple on the current wager. running multiple times enables us to find the optimal increment size

d'Alembert increments the bet size when you lose, decrements on a win. this is a relatively 'safe' strategy, requiring a smaller bankroll. If the number of wins is the same as the number of losses, you will always be in profit by the number of bets.

Labouchere is a split martingale system for even-money prop bets, set desired win x, split into array with sum x, then wage array[0] + array[n-1] (n = array length) repeatedly, removing the items from the list in the case of a win, adding the amount lost to the tail of the list in the case of a loss. continue til won, or broke. bankroll is the limiting factor/risk as usual, as losses cause bets to become increasingly large
