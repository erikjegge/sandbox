from itertools import permutations

diceSides = [1,2,3,4,5,6]
diceRolls = []
possibleOutcomes = []

for w in diceSides:
    for x in diceSides:
        for y in diceSides:
            for z in diceSides:
                diceRolls.append((w,x,y,z))
                out1 = w + x
                out2 = w + y
                out3 = w + z
                out4 = x + y
                out5 = x + z
                out6 = y + z
                sortedList = [out1,out2,out3,out4,out5,out6]
                possibleOutcomes.append(set(sortedList))

print(diceRolls)
print(len(diceRolls))
print(len(possibleOutcomes))

dict = {
  2: 0, 
  3: 0,
  4: 0,
  5: 0,
  6: 0,
  7: 0,
  8: 0,
  9: 0,
  10: 0,
  11: 0,
  12: 0
}

for x in possibleOutcomes:
    for y in x:
        dict[y] += 1

print(dict)

print(dict[2]/len(possibleOutcomes))
print(dict[3]/len(possibleOutcomes))
print(dict[4]/len(possibleOutcomes))
print(dict[5]/len(possibleOutcomes))
print(dict[6]/len(possibleOutcomes))
print(dict[7]/len(possibleOutcomes))
print(dict[8]/len(possibleOutcomes))
print(dict[9]/len(possibleOutcomes))
print(dict[10]/len(possibleOutcomes))
print(dict[11]/len(possibleOutcomes))
print(dict[12]/len(possibleOutcomes))

# 6 7 8

counter = 0
for x in possibleOutcomes:
    if 6 in x:
        counter += 1
    elif 7 in x:
        counter += 1
    elif 8 in x:
        counter += 1

print(counter/len(possibleOutcomes))

numbers = [2,3,4,5,6,7,8,9,10,11,12]

allPermThree = list(permutations(numbers,3))

results = []

for r in allPermThree:
    for y in possibleOutcomes:
        found = False
        for x in r:
            if x in y:
               found = True
        if found:
            print(r)
            print(y)

