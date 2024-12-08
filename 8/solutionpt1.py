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
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[j]
            x0, y0 = 2 * x1 - x2, 2 * y1 - y2
            x00, y00 = 2 * x2 - x1, 2 * y2 - y1

            if 0 <= x0 < n and 0 <= y0 < m:
                antinodes.add((x0, y0))
            if 0 <= x00 < n and 0 <= y00 < m:
                antinodes.add((x00, y00))

print(len(antinodes))
