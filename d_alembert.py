import random
import matplotlib
import matplotlib.pyplot as pyplot
import time

lower_bust = 31.235
higher_profit = 63.208

sampleSize = 1000
startingFunds = 10000
wagerSize = 100
wagerCount = 100

def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll > 50:
        return True

def dAlembert(funds,initial_wager,wager_count):
    da_busts = 0
    da_profits = 0

    value = funds
    wager = initial_wager
    currentWager = 1
    previousWager = 1
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 1:
            if wager == initial_wager:
                pass
            else:
                wager -= initial_wager

            if rollDice():
                value += wager
                previousWagerAmount = wager
            else:
                value -= wager
                previousWager = 0
                previousWagerAmount = wager

                if value <= 0:
                    da_busts += 1
                    break

        elif previousWager == 0:
            wager = previousWagerAmount + initial_wager
            if(value - wager) <= 0:
                wager = value

            if rollDice():
                value += wager
                previousWager = 1
                previousWagerAmount = wager
            else:
                value -= wager
                previousWagerAmount = wager

                if value <= 0:
                    da_busts += 1
                    break

        currentWager += 1

    print 'value', value
    if value > funds:
        da_profits += 1

dAlembert(startingFunds,wagerSize,wagerCount)
