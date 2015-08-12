import random

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

	currentWager = 0

	while currentWager < wager_count:
		if rollDice():
			value += wager
		else:
			value -= wager

		currentWager += 1

	if value <= 0:
		simple_busts += 1
		value = 'broke'

	print 'Funds: ', value
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
