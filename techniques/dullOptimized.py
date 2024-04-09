
from concurrent.futures import ThreadPoolExecutor
import random


def runDullOptimized(printStats=True):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(runSimulation, range(10000)))  # Run 10,000 simulations
    if printStats:
        print(f'Lowest number of Cards: {min(results)}')
        print(f'Highest number of Cards: {max(results)}')
        totalCards = sum(result for result in results)
        averageCards = totalCards / len(results)
        print(f'Average number of Cards: {averageCards}')
        results.sort()
        if len(results) % 2 == 0:
            median = (results[len(results)//2] + results[len(results)//2 - 1]) / 2
        else:
            median = results[len(results)//2]
        print(f'Median number of Cards: {median}')
        meanAverageDeviation = sum(abs(result - averageCards) for result in results) / len(results)
        print(f'Mean Average Deviation: {meanAverageDeviation}')
        standardDeviation = (sum((result - averageCards) ** 2 for result in results) / len(results)) ** 0.5
        print(f'Standard Deviation: {standardDeviation}')

def runSimulation(_):
    matched = False
    cardsTotal = 0
    while not matched:
        matched, cards = compareDecks()
        cardsTotal += cards
    return cardsTotal

def compareDecks():
    # Create a list of the numbers 1 through 52
    numbers1 = list(range(1, 53))
    numbers2 = list(range(1, 53))
    # Shuffle the numbers
    random.shuffle(numbers1)
    # random.shuffle(numbers2) # You don't need to shuffle the second list
    # Check if any of the numbers match in the same position
    for i in range(len(numbers1)):
        if numbers1[i] == numbers2[i]:
            return True, i + 1
    return False, len(numbers1)

if __name__ == '__main__':
    runDullOptimized(printStats=True)