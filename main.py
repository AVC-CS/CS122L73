import random
def getRandom(N):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    numbers = [random.randint(1, 100) for _ in range(N)]
    return numbers

def filterAvg(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    average = sum(numbers) / len(numbers)
    filtered = [v for v in numbers if v > average]
    return filtered

def main():
    N = 5
    numbers = getRandom(N)
    print(f'The original list values : { numbers }')
    ret = filterAvg(numbers)
    print(f'The average value: {sum(numbers)/len(numbers)}')
    print(f'The return values from filterAvg() : { ret }')


if __name__ == '__main__':
    main()
