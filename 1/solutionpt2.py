from typing import List
from collections import Counter


with open('1/input.txt', "r") as file:
    lines = file.readlines()

left: List[int] = []
right: List[int] = []

for line in lines:
    left.append(int(line.split()[0]))
    right.append(int(line.split()[1]))

left.sort()
right.sort()

counter = Counter(right)

sum: int = 0
for num in left:
    if num in counter:
        sum += num * counter[num]

print(sum)
