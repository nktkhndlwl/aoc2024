from os import getcwd, path
from typing import List


def is_increasing(list: List[int]) -> bool:
    return all(list[i] < list[i + 1] for i in range(len(list) - 1))


def is_decreasing(list: List[int]) -> bool:
    return all(list[i] > list[i + 1] for i in range(len(list) - 1))


def check_diff(list: List[int]) -> bool:
    return all(abs(list[i+1] - list[i]) in (1, 2, 3) for i in range(len(list) - 1))


with open(path.join(getcwd(), '2', 'input.txt'), "r") as file:
    reports = list(map(lambda x: x.split(), file.readlines()))
    reports = list(map(lambda x: list(map(int, x)), reports))
    safe = 0
    for report in reports:
        if (is_increasing(report) or is_decreasing(report)) and check_diff(report):
            safe += 1

    print(safe)
