from typing import List, Set, Tuple
from collections import deque

with open('12/input.txt', 'r') as file:
    lines = file.readlines()

grid: List[List[str]] = [[c for c in line.strip()] for line in lines]

visited: Set[Tuple[int, int]] = set()
n, m = len(grid), len(grid[0])

islands: List[List[Tuple[int, int]]] = []
for i in range(n):
    for j in range(m):
        if (i, j) in visited:
            continue

        q = deque()
        q.append((i, j))
        current_island = []
        while q:
            x, y = q.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            current_island.append((x, y))
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == grid[x][y] and (nx, ny) not in visited:
                    q.append((nx, ny))
        islands.append(current_island)


def calculate_area(island: List[Tuple[int, int]]) -> int:
    return len(island)


def calculate_perimeter(island: List[Tuple[int, int]], grid: List[List[str]]) -> int:
    perimeter = 0
    n, m = len(grid), len(grid[0])
    for x, y in island:
        current_perimeter = 4
        if 0 <= x-1 < n and grid[x - 1][y] == grid[x][y]:
            current_perimeter -= 1
        if 0 <= x+1 < n and grid[x + 1][y] == grid[x][y]:
            current_perimeter -= 1
        if 0 <= y-1 < m and grid[x][y - 1] == grid[x][y]:
            current_perimeter -= 1
        if 0 <= y+1 < m and grid[x][y + 1] == grid[x][y]:
            current_perimeter -= 1
        perimeter += current_perimeter
    return perimeter


ans = 0
for island in islands:
    ans += calculate_area(island) * calculate_perimeter(island, grid)
print(ans)
