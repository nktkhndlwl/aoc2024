import re


with open('3/input.txt', 'r') as f:
    data = f.read()
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.finditer(pattern, data)

    total = 0
    for match in matches:
        x, y = map(int, match.groups())
        total += x * y

    print(total)
