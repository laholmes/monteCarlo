import random
import matplotlib
import matplotlib.pyplot as pyplot
import time

lower_bust = 31.235
higher_profit = 63.208
sampleSize = 100
martingale_busts = 0.0
martingale_profits = 0.0

startingFunds = 10000
wagerSize = 100
wagerCount = 100

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

def multiple_bettor(funds, initial_wager, wager_count):
	global multiple_busts
	global multiple_profits

	value = funds
	wager = initial_wager
	wX = []
	vY = []

	currentWager = 1
	previousWager = 1

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
					multiple_busts += 1
					break

		elif previousWager == 0:
			if rollDice():
				wager = previousWagerAmount * random_multiple

				if (value - wager) < 0:
					wager = value

				value += wager
				wager = initial_wager
				previousWager = 1
				wX.append(currentWager)
				vY.append(value)
			else:
				wager = previousWagerAmount * random_multiple

				if (value - wager) < 0:
					wager = value

				value -= wager
				previousWagerAmount = wager
				wX.append(currentWager)
				vY.append(value)

				if value <= 0:
					multiple_busts += 1
					break

				previousWager = 0

		currentWager += 1

	print value
	#pyplot.plot(wX, vY)
	if value > funds:
		value = 0
		multiple_profits += 1

while True:
	multiple_busts = 0.0
	multiple_profits = 0.0
	multipleSampSize = 100000
	currentSample = 1

	random_multiple = random.uniform(0.1,10.0)

	while currentSample <= multipleSampSize:
		multiple_bettor(startingFunds, wagerSize, wagerCount)
		currentSample += 1

	if ((multiple_busts/multipleSampSize)*100.00 < lower_bust) and ((multiple_profits/multipleSampSize)*100.00 > higher_profit):
		print '##########################'
		print 'found winner, multiple:',random_multiple
		print 'lower bust to beat:',lower_bust
		print 'higher profit rate to beat:',higher_profit
		print 'bust rate:',(multiple_busts/multipleSampSize)*100.00
		print 'profit rate:',(multiple_busts/multipleSampSize)*100.00
		print '##########################'
	else:
		print '##########################'
		print 'found loser, multiple:',random_multiple
		print 'lower bust to beat:',lower_bust
		print 'higher profit rate to beat:',higher_profit
		print 'bust rate:',(multiple_busts/multipleSampSize)*100.00
		print 'profit rate:',(multiple_busts/multipleSampSize)*100.00
		print '##########################'

#print 'martingale bettor bust chance', (martingale_busts/sampleSize) * 100.00
#print 'martingale bettor profit chances', (martingale_profits/sampleSize) * 100.00

#pyplot.ylabel('Account Value')
#pyplot.xlabel('Wager Count')
#pyplot.axhline(0, color = 'r')
#pyplot.show()
#time.sleep(555)
