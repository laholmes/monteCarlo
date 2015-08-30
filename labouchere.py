import random
import time
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

broke_count = 0

def Labouchere():
    global broke_count
    starting_funds = 100
    goal = 10
    # can adjust risk by distributing return across more bets: 1,1,1,1,1 rather than 1,2,2
    # wager size can get very big
    system = []
    profit = 0
    current_funds = starting_funds
    wagerSizes = []
    plot_funds = []
    broke = False

    wins = 1
    losses = 1

    while profit < goal and !broke:
        if len(system) > 1:
            size = system[0] + system[-1]
        else:
            size = system[0]

        wagerSizes.append(size)
        plot_funds.append(current_funds)

        if current_funds <= 0:
            broke = True
            broke_count += 1
        elif current_funds - wagerSize <= 0:
            size = current_funds

        dice = random.randrange(1,101)

        if dice < 51:
            losses += 1
            system.append(size)
            current_funds -= size

        else:
            wins += 1
            current_funds += size
            profit = current_funds - starting_funds

            if profit != goal:
                try:
                    del system[0]
                    del system[-1]
                except:
                    pass

        wagerSizes.append(size)
        plot_funds.append(current_funds)

        s1.plot(wagerSizes)
        s2.plot(plot_funds)

f = plt.figure()
s1 = f.add_subplot(211)
s2 = f.add_subplot(212)

sampleSize = 100

for x in range(sampleSize):
    Labouchere()

print("Broke percentage", (float(broke_count) / sample_size)*100.00)

plt.show()
