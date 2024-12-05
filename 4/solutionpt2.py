from typing import List

with open('4/input.txt', 'r') as file:
    data: List[str] = file.readlines()
    data = [line.strip() for line in data]

    n = len(data)
    m = len(data[0])

    total = 0
    for i in range(1, n - 1):
        for j in range(1, m-1):
            if data[i][j] == 'A':
                if (data[i-1][j-1] == 'M' and data[i+1][j+1] == 'S' and data[i-1][j+1] == 'M' and data[i+1][j-1] == 'S') or \
                   (data[i-1][j-1] == 'S' and data[i+1][j+1] == 'M' and data[i-1][j+1] == 'S' and data[i+1][j-1] == 'M') or \
                   (data[i-1][j-1] == 'M' and data[i+1][j+1] == 'S' and data[i-1][j+1] == 'S' and data[i+1][j-1] == 'M') or \
                   (data[i-1][j-1] == 'S' and data[i+1][j+1] == 'M' and data[i-1][j+1] == 'M' and data[i+1][j-1] == 'S'):
                    total += 1

    print(total)


