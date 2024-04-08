from techniques import fancy, dull
import time
from concurrent.futures import ThreadPoolExecutor

def main():
    print('Dull:')
    # Calculate time taken for dull
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(timeFunction, [dull.runDull]*10, [{'printStats': False}]*10)) # Run 10 simulations of 10,000 runs
    # Calculate the average time taken
    dullTimeTaken = sum(results) / len(results)
    print(f'Time taken: {dullTimeTaken}')
    print('Fancy:')
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(timeFunction, [fancy.runFancy]*10, [{'printStats': False}]*10)) # Run 10 simulations of 10,000 runs
    fancyTimeTaken = sum(results) / len(results)
    print(f'Time taken: {fancyTimeTaken}')
    # Calculate the percentage difference
    percentage = ((fancyTimeTaken - dullTimeTaken) / fancyTimeTaken) * 100
    print(f'Dull is {percentage:.2f}% faster than Fancy')

def timeFunction(function, args=None):
    start = time.time()
    function(**args)
    return time.time() - start

if __name__ == '__main__':
    main()