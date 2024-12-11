from functools import lru_cache
from collections import defaultdict


with open('11/input.txt', 'r') as file:
    line = file.read()

numbers = [int(c.strip()) for c in line.split()]

N = 75


@lru_cache(maxsize=None)
def change(number: int) -> list[int]:
    if number == 0:
        return [1]
    elif len(str(number)) % 2 == 0:
        left, right = int(str(number)[:len(str(number))//2]), int(str(number)[len(str(number))//2:])
        return [left, right]
    else:
        return [number*2024]


counter = defaultdict(int)
for number in numbers:
    counter[number] += 1

for _ in range(N):
    new_counter = defaultdict(int)
    for number, count in counter.items():
        for new_number in change(number):
            new_counter[new_number] += count
    counter = new_counter

total = 0
for number, count in counter.items():
    total += count

print(total)
