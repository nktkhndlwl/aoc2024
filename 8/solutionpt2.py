with open('8/input.txt') as file:
    lines = [[c for c in line.strip()] for line in file.readlines()]

coordinates_by_freq = {}
n = len(lines)
m = len(lines[0])
for i in range(n):
    for j in range(m):
        c = lines[i][j]
        if c == '.':
            continue

        if c not in coordinates_by_freq:
            coordinates_by_freq[c] = []
        coordinates_by_freq[c].append((i, j))

antinodes = set()
for freq, coordinates in coordinates_by_freq.items():
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            for x in range(n):
                for y in range(m):
                    x1, y1 = coordinates[i]
                    x2, y2 = coordinates[j]
                    if (x1 == x and y1 == y) or (x2 == x and y2 == y) or (x1 == x and x2 == x) or (y1 == y and y2 == y): # same point or same x or same y
                        antinodes.add((x, y))
                    else:
                        if x2 != x and y2 != y and (x1-x)/(x2-x) == (y1-y)/(y2-y): # same slope
                            antinodes.add((x, y))

print(len(antinodes))
