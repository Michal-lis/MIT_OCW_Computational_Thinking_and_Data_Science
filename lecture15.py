import random

numCasesPerYear = 36000
numYears = 3
stateSize = 10000
communitySize = 10
numCommunities = stateSize // communitySize

numTrials = 100
numGreater = 0
for x in range(10):
    numGreater = 0
    for t in range(numTrials):
        locs = [0] * numCommunities
        for i in range(numYears * numCasesPerYear):
            num = random.choice(range(numCommunities))
            locs[num] += 1
            if locs[num] >= 143:
                numGreater += 1
    prob = round(numGreater / numTrials, 6)
    print(prob)
