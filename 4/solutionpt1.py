from typing import List, Tuple


WORD = 'XMAS'


def word_search(data: List[str], i: int, j: int, direction: Tuple[int, int]) -> int:
    n = len(data)
    m = len(data[0])
    for k in range(len(WORD)):
        if i + k * direction[0] < 0 or i + k * direction[0] >= n or j + k * direction[1] < 0 or j + k * direction[1] >= m:
            return 0
        if data[i + k * direction[0]][j + k * direction[1]] != WORD[k]:
            return 0
    return 1


with open('4/input.txt', 'r') as file:
    data: List[str] = file.readlines()
    data = [line.strip() for line in data]

    n = len(data)
    m = len(data[0])

    total = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for i in range(n):
        for j in range(m):
            if data[i][j] == 'X':
                for direction in directions:
                    total += word_search(data, i, j, direction)

    print(total)
