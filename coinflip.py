def coinFlipper(numFlips):
    import random
    results = []
    possibleOutcomes = ['H', 'T']
    for event in range(numFlips):
        results.append(possibleOutcomes[random.randint(0,1)])
    return results


def streakChecker(flips):
    if len(set(coinFlipper(flips))) == 1:
        return True

def coinStreakExperiment(streakLength, permutations):
    streaks = 0
    for seq in range(permutations):
        if streakChecker(streakLength): 
            streaks += 1
    return 'The occurence of streaks(H/T) for the provided parameters is {} %'.format(streaks/permutations*100)

print(coinStreakExperiment(13, 10000))


