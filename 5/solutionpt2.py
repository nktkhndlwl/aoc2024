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
        wrong_order: bool = False
        i = 0
        while i < len(orders):
            order: List[int] = orders[i]
            left_element: int = order[0]
            right_element: int = order[1]
            if left_element not in update or right_element not in update:
                i += 1
                continue

            left_index: int = update.index(left_element)
            right_index: int = update.index(right_element)
            if left_index >= right_index:
                wrong_order = True
                temp: int = update[left_index]
                update[left_index] = update[right_index]
                update[right_index] = temp
                i = 0
            else:
                i += 1

        if wrong_order:
            total += update[len(update) // 2]

    print(total)
