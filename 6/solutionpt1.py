with open('6/input.txt', 'r') as file:
    lines = file.readlines()


start = None
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '^':
            start = (i, j)
            break
    if start:
        break

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_counter = 0

cells = 0
current = start

changed_lines = [[c for c in line] for line in lines]

seen = set()
while current[0] >= 0 and current[0] < len(lines) and current[1] >= 0 and current[1] < len(lines[0]):
    next_cell = (current[0] + direction[direction_counter][0], current[1] + direction[direction_counter][1])
    # print(f'{current=}')
    if current not in seen:
        seen.add(current)
        cells += 1
        changed_lines[current[0]][current[1]] = 'X'

    if next_cell[0] < 0 or next_cell[0] >= len(lines) or next_cell[1] < 0 or next_cell[1] >= len(lines[0]):
        break

    if lines[next_cell[0]][next_cell[1]] == '#':
        direction_counter = (direction_counter + 1) % 4
        next_cell = (current[0] + direction[direction_counter][0], current[1] + direction[direction_counter][1])
        # print(f'turning right at {current}')

    current = next_cell

print(cells)
# print('\n'.join([''.join(line) for line in changed_lines]).strip())
