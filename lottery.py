"""

    Lottery Sim

    Using the powerball as my example

    Grand Prize:

    jackpots started at $40 million (annuity) and increased by a minimum of $10 million (annuity) between drawings.

    Grand Prize (40 mil):    1 in 292,201,338.00
    Million:                1 in 11,688,053.52
    50K:                    1 in 913,129.18
    100:                    1 in 36,525.17
    100:                    1 in 14,494.11
    7:                      1 in 579.76
    7:                      1 in 701.33
    4:                      1 in 91.98
    4:                      1 in 38.32

"""

import random
import pandas as pd
import matplotlib.pyplot as plt

numberOfPeople = 2000000
costToPlay = 10
weeks = 260

def checkWinnings():
    winnings = 0

    # check grand prize
    check = random.randint(1, 292201338)
    if check == 1:
        winnings = 40000000
        return winnings

    # check Million
    check = random.randint(1, 11688053)
    if check == 1:
        winnings = 1000000
        return winnings   
  
    # check 50K
    check = random.randint(1, 913129)
    if check == 1:
        winnings = 50000
        return winnings   

    # check 100
    check = random.randint(1, 36525)
    if check == 1:
        winnings = 100
        return winnings   
    # check 100
    check = random.randint(1, 14494)
    if check == 1:
        winnings = 100
        return winnings   
    
    # check 7
    check = random.randint(1, 579)
    if check == 1:
        winnings = 7
        return winnings  
    # check 7
    check = random.randint(1, 701)
    if check == 1:
        winnings = 7
        return winnings  

    # check 4
    check = random.randint(1, 92)
    if check == 1:
        winnings = 4
        return winnings  
    # check 4
    check = random.randint(1, 38)
    if check == 1:
        winnings = 4
        return winnings        

    return winnings


#r1 = random.randint(0, 10)
#print("Random number between 0 and 10 is % s" % (r1))
summaryResults = []

for iwk in range(weeks):
    rows = []

    for idx in range(numberOfPeople):
        gainLoss = checkWinnings() - costToPlay
        rows.append([gainLoss])

    df = pd.DataFrame(rows, columns=["Portfolio"])
    df.sort_values(by=['Portfolio'], inplace=True, ascending=False)
    df = df.reset_index(drop=True)
    df = df.reset_index()

    Total = df['Portfolio'].sum()
    lotteryIncome = numberOfPeople * costToPlay
    summaryResults.append([iwk, lotteryIncome, Total, lotteryIncome+Total])

df2 = pd.DataFrame(summaryResults)

writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
df2.to_excel(writer, sheet_name='welcome', index=False)
writer.save()

    # print('<><><><><><><><><><><><><><>')

    
    # print(lotteryIncome)
    # print(Total)
    # print(lotteryIncome+Total)
    # print('<><><><><><><><><><><><><><>')

    #df.plot(x='index', y='Portfolio', kind='scatter')
    #plt.show()