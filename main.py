from models.deck import Deck
from concurrent.futures import ThreadPoolExecutor


def main():
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(runSimulation, range(10000)))  # Run 10,000 simulations
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
    decks = 0
    while not matched:
        matched, cards = tryAndMatch(Deck(shuffled=False), Deck(shuffled=True))
        decks += 1
    return cards+(decks-1)*52

def tryAndMatch(deck1, deck2):
    cardsDrawn = 0
    while deck1.size() > 0 and deck2.size() > 0:
        matched = compareCards(deck1, deck2)
        cardsDrawn += 1
        if matched:
            return matched, cardsDrawn
    return False, cardsDrawn

def compareCards(deck1, deck2):
    card1 = deck1.draw()
    card2 = deck2.draw()
    if card1.rank == card2.rank and card1.suit == card2.suit:
        return True
    return False

if __name__ == '__main__':
    main()