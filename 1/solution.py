from typing import List
from os import getcwd, path


with open(path.join(getcwd(), '1', 'input.txt'), "r") as file:
    lines = file.readlines()

left: List[int] = []
right: List[int] = []

for line in lines:
    left.append(int(line.split()[0]))
    right.append(int(line.split()[1]))

left.sort()
right.sort()

sum: int = 0
for i in range(len(left)):
    sum += abs(left[i] - right[i])

print(sum)
