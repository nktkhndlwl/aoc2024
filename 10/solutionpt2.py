from collections import deque

with open('10/input.txt', 'r') as file:
    lines = file.readlines()

grid = [[int(c) for c in line.strip()] for line in lines]
n, m = len(grid), len(grid[0])

total = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            nines = {}
            q = deque()
            q.append((i, j))
            while len(q) > 0:
                x, y = q.popleft()
                if grid[x][y] == 9:
                    if (x, y) not in nines:
                        nines[(x, y)] = 0
                    nines[(x, y)] += 1
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] - grid[x][y]== 1:
                        q.append((nx, ny))
            score = 0
            for k, v in nines.items():
                score += v
            total += score
print(total)
