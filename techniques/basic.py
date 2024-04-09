
from concurrent.futures import ThreadPoolExecutor
import random


def runBasic(printStats=True):
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
    cardsTotal = 1
    while random.randint(1, 53) != 1:
        cardsTotal += 1
    return cardsTotal


if __name__ == '__main__':
    runBasic(printStats=True)