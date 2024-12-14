import re


with open('3/input.txt', 'r') as f:
    data = f.read()
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))'
    matches = re.finditer(pattern, data)

    total = 0
    do = True
    for match in matches:
        groups = match.groups()
        print(groups)
        if groups[2] == 'do()':
            do = True
            continue
        elif groups[3] == "don't()":
            do = False
            continue

        if do:
            x, y = int(groups[0]), int(groups[1])
            total += x * y

    print(total)
