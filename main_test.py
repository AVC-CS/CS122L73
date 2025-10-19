import main
import pytest


@pytest.mark.basic
def test_getRandom():
    N = 5
    numbers = main.getRandom(N)
    print(f'Generated numbers: {numbers}')
    assert len(numbers) == N
    for num in numbers:
        assert 1 <= num <= 100

@pytest.mark.basic
@pytest.mark.parametrize("numbers", [[1, 5, 10, 20]])
def test_main_1(numbers):
    # numbers = main.getRandom(N)
    print(f'The original list values : { numbers }')
    average = sum(numbers) / len(numbers)
    ret = main.filterAvg(numbers)
    print(f'The average value: {sum(numbers)/len(numbers)}')
    print(f'The return values from filterAvg() : { ret }')
    check = [v for v in ret if v < average]
    assert check == []

@pytest.mark.edge
@pytest.mark.parametrize("numbers", [[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]])
def test_main_2(numbers):
    # N = 10
    # numbers = main.getRandom(N)
    print(f'The original list values : { numbers }')
    average = sum(numbers) / len(numbers)
    ret = main.filterAvg(numbers)
    print(f'The average value: {sum(numbers)/len(numbers)}')
    print(f'The return values from filterAvg() : { ret }')
    check = [v for v in ret if v < average]
    assert check == []

@pytest.mark.bonus
def test_bonus():
    N = 1000
    numbers = main.getRandom(N)
    print(f'Generated numbers: {numbers}')
    assert len(numbers) == N
    ftlist = main.filterAvg(numbers)
    average = sum(numbers) / len(numbers)
    check = [v for v in numbers if v > average]
    assert len(ftlist) == len(check)
    assert check == ftlist 
        