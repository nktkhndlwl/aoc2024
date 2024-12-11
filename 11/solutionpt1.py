from functools import lru_cache


with open('11/input.txt', 'r') as file:
    line = file.read()

numbers = [int(c.strip()) for c in line.split()]

N = 25


@lru_cache(maxsize=None)
def change(number: int) -> list[int]:
    if number == 0:
        return [1]
    elif len(str(number)) % 2 == 0:
        left, right = int(str(number)[:len(str(number))//2]), int(str(number)[len(str(number))//2:])
        return [left, right]
    else:
        return [number*2024]


for _ in range(N):
    new_numbers = list()
    for i in range(len(numbers)):
        number = numbers[i]
        for new_number in change(number):
            new_numbers.append(new_number)
    numbers = new_numbers

print(len(numbers))
