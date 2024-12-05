from typing import List


with open('5/input.txt', 'r') as file:
    data: List[str] = file.readlines()
    data: List[str] = [line.strip() for line in data]

    empty_line: int = data.index('')
    orders: List[str] = data[:empty_line]
    updates: List[str] = data[empty_line+1:]

    orders: List[List[str]] = [line.split('|') for line in orders]
    updates: List[List[str]] = [line.split(',') for line in updates]

    orders: List[List[int]] = [[int(i) for i in order] for order in orders]
    updates: List[List[int]] = [[int(i) for i in update] for update in updates]

    total: int = 0
    for update in updates:
        for order in orders:
            if order[0] in update and order[1] in update and update.index(order[0]) >= update.index(order[1]):
                break
        else:
            total += update[len(update) // 2]

    print(total)
