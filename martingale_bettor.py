import random
import matplotlib
import matplotlib.pyplot as pyplot
import time

def rollDice():
	roll = random.randint(1, 100)

	if(roll == 100):
		return False
	elif roll <= 50:
		return False
	elif 50 < roll < 100:
		return True

def martingale_bettor(funds, initial_wager, wager_count):
	value = funds
	wager = initial_wager
	global broke_count

	wX = []
	vY = []

	currentWager = 1
	previousWager = 1
	previousWagerAmount = initial_wager

	while currentWager <= wager_count:
		if previousWager == 1:
			if rollDice():
				value += wager
				wX.append(currentWager)
				vY.append(value)
			else:
				value -= wager
				previousWager = 0
				previousWagerAmount = wager
				wX.append(currentWager)
				vY.append(value)
				if value < 0:
					broke_count += 1
					break

		elif previousWager == 0:
			if rollDice():
				wager = previousWagerAmount * 2

				if (value - wager) < 0:
					wager = value

				value += wager
				wager = initial_wager
				previousWager = 1
				wX.append(currentWager)
				vY.append(value)
			else:
				wager = previousWagerAmount * 2

				if (value - wager) < 0:
					wager = value

				value -= wager
				previousWagerAmount = wager
				wX.append(currentWager)
				vY.append(value)

				if value <= 0:
					broke_count += 1
					break

				previousWager = 0

		currentWager += 1

	print value
	pyplot.plot(wX, vY)

x = 0
broke_count = 0

while x < 1000:
	martingale_bettor(10000, 100, 100)
	x += 1

print 'death rate:', (broke_count / float(x)) * 100
print 'survival rate:', 100 - ((broke_count / float(x)) * 100)
pyplot.ylabel('Account Value')
pyplot.xlabel('Wager Count')
pyplot.axhline(0, color = 'r')
pyplot.show()
time.sleep(555)
