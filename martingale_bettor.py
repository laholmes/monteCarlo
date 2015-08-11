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

	wX = []
	vY = []

	currentWager = 1
	previousWager = 1
	previousWagerAmount = initial_wager

	while currentWager <= wager_count:
		if previousWager == 1:
			print 'won last round'
			if rollDice():
				value += wager
				print value
				wX.append(currentWager)
				vY.append(value)
			else:
				value -= wager
				previousWager = 0
				print value
				previousWagerAmount = wager
				wX.append(currentWager)
				vY.append(value)
				if value < 0:
					print 'we went broke after ',currentWager,' bets'
					break

		elif previousWager == 0:
			print 'we lost the last one, so double down'
			if rollDice():
				wager = previousWagerAmount * 2
				print 'we won ',wager
				value += wager
				print value
				wager = initial_wager
				previousWager = 1
				wX.append(currentWager)
				vY.append(value)
			else:
				wager = previousWagerAmount * 2
				print 'we lost',wager
				value -= wager
				if value < 0:
					print 'we went broke after ',currentWager,' bets'
					break

				print value
				previousWager = 0

				previousWagerAmount = wager
				wX.append(currentWager)
				vY.append(value)

		currentWager += 1

	print value
	pyplot.plot(wX, vY)

x = 0
while x < 100:
	martingale_bettor(10000, 100, 100)
	x += 1

pyplot.ylabel('Account Value')
pyplot.xlabel('Wager Count')
pyplot.show()
time.sleep(555)
