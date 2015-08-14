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

'''
def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll > 50:
        return True
'''

def rollDice():
    roll = random.randint(1,100)

    if roll <= 50:
        return False
    elif roll >= 51:
        return True

def dAlembert(funds,initial_wager,wager_count):
    global ret
    global da_busts
    global da_profits

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

    ret += value

    if value > funds:
        da_profits += 1

daSampSize = 100000
counter = 1
ret = 0.0
da_busts = 0.0
da_profits = 0.0

while counter <= daSampSize:
    dAlembert(startingFunds,wagerSize,wagerCount)
    counter += 1


print 'Total invested:',daSampSize*startingFunds
print 'Total return:',ret
print 'ROI:',ret - (daSampSize*startingFunds)
print 'Bust rate:',(da_busts/daSampSize)*100.00
print 'Profit rate:',(da_profits/daSampSize)*100.00
