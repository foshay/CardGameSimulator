import math
from techniques import fancy, dull, basic, dullOptimized
import time
from concurrent.futures import ThreadPoolExecutor

def main():
    # Warm up the CPU
    print('Warming up the CPU...')
    for i in range(10000000):
        math.sqrt(i)
    print('Dull:')
    # Calculate time taken for dull
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(timeFunction, [dull.runDull]*10, [{'printStats': False}]*10)) # Run 10 simulations of 10,000 runs
    # Calculate the average time taken
    dullTimeTaken = sum(results) / len(results)
    print(f'Time taken: {dullTimeTaken}')
    print('Dull Optimized:')
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(timeFunction, [dullOptimized.runDullOptimized]*10, [{'printStats': False}]*10)) # Run 10 simulations of 10,000 runs
    dullOptimizedTimeTaken = sum(results) / len(results)
    print(f'Time taken: {dullOptimizedTimeTaken}')
    percentage = ((dullTimeTaken - dullOptimizedTimeTaken) / dullTimeTaken) * 100
    print(f'Dull Optimized is {percentage:.2f}% faster than Dull')
    print('Fancy:')
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(timeFunction, [fancy.runFancy]*10, [{'printStats': False}]*10)) # Run 10 simulations of 10,000 runs
    fancyTimeTaken = sum(results) / len(results)
    print(f'Time taken: {fancyTimeTaken}')
    # Calculate the percentage difference
    percentage = ((fancyTimeTaken - dullTimeTaken) / fancyTimeTaken) * 100
    print(f'Dull is {percentage:.2f}% faster than Fancy')
    print('Basic:')
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(timeFunction, [basic.runBasic]*10, [{'printStats': False}]*10)) # Run 10 simulations of 10,000 runs
    basicTimeTaken = sum(results) / len(results)
    print(f'Time taken: {basicTimeTaken}')
    percentage = ((dullTimeTaken - basicTimeTaken) / dullTimeTaken) * 100
    print(f'Basic is {percentage:.2f}% faster than Dull')

def timeFunction(function, args=None):
    start = time.time()
    function(**args)
    return time.time() - start

if __name__ == '__main__':
    main()