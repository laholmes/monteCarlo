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
	global martingale_busts
	global martingale_profits

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
					martingale_busts += 1
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
					martingale_busts += 1
					break

				previousWager = 0

		currentWager += 1

	print value
	pyplot.plot(wX, vY)
	if value > funds:
		value = 0
		martingale_profits += 1

x = 0
sampleSize = 100
martingale_busts = 0.0
martingale_profits = 0.0

while x < sampleSize:
	martingale_bettor(10000, 100, 100)
	x += 1

print 'martingale bettor bust chance', (martingale_busts/sampleSize) * 100.00
print 'martingale bettor profit chances', (martingale_profits/sampleSize) * 100.00

pyplot.ylabel('Account Value')
pyplot.xlabel('Wager Count')
pyplot.axhline(0, color = 'r')
pyplot.show()
time.sleep(555)
