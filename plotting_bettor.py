import random
import matplotlib
import matplotlib.pyplot as pyplot

def rollDice():
	roll = random.randint(1, 100)

	if(roll == 100):
		return False
	elif roll <= 50:
		return False
	elif 50 < roll < 100:
		return True

def simple_bettor(funds, initial_wager, wager_count):
	value = funds
	wager = initial_wager
	global simple_busts
	global simple_profits

	wX = []
	vY = []
	currentWager = 1

	while currentWager <= wager_count:
		if rollDice():
			value += wager
			wX.append(currentWager)
			vY.append(value)
		else:
			value -= wager
			wX.append(currentWager)
			vY.append(value)

		currentWager += 1

	if value <= 0:
		simple_busts += 1
		value = 'broke'

	print 'Funds: ', value
	pyplot.plot(wX, vY)
	if value > funds:
		value = 0
		simple_profits += 1

# single bettor
#simple_bettor(10000,100,100)

x = 0
sampleSize = 100

simple_busts = 0.0
simple_profits = 0.0

# 100 bettors
while x < sampleSize:
	simple_bettor(10000, 100, 10000)
	x += 1

print 'simple bettor bust chance', (simple_busts/sampleSize) * 100.00
print 'simple bettor profit chances', (simple_profits/sampleSize) * 100.00

pyplot.ylabel('Account Value')
pyplot.xlabel('Wager Count')
pyplot.show()
