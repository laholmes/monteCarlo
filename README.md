# monteCarlo
Monte Carlo simulations + stochastic calculus playground in python

simple_bettor makes wagers which win based on random number (1-100, 51-99 is a win)
it runs the simulation for 100 bettors, all starting with 10000, betting 100 each round, and betting until broke or 10000 rounds reached.

plotting_bettor is as above, but plots the results using matplotlib

martingale_bettor doubles current wager when the bettor lost in the previous round

d'Alembert increments the bet size when you lose, decrements on a win. this is a relatively 'safe' strategy, requiring a smaller bankroll. If the number of wins is the same as the number of losses, you will always be in profit by the number of bets.
