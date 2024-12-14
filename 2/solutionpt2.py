from typing import List


def is_increasing(list: List[int]) -> bool:
    return all(list[i] < list[i + 1] for i in range(len(list) - 1))


def is_decreasing(list: List[int]) -> bool:
    return all(list[i] > list[i + 1] for i in range(len(list) - 1))


def check_diff(list: List[int]) -> bool:
    return all(abs(list[i+1] - list[i]) in (1, 2, 3) for i in range(len(list) - 1))


with open('2/input.txt', "r") as file:
    reports = list(map(lambda x: x.split(), file.readlines()))
    reports = list(map(lambda x: list(map(int, x)), reports))
    safe = 0
    for report in reports:
        if (is_increasing(report) or is_decreasing(report)) and check_diff(report):
            print(f'{report} is safe')
            safe += 1
        else:
            for i in range(len(report)):
                if i == 0:
                    new_report = report[i + 1:]
                elif i == len(report) - 1:
                    new_report = report[:i]
                else:
                    new_report = report[:i] + report[i+1:]
                if (is_increasing(new_report) or is_decreasing(new_report)) and check_diff(new_report):
                    print(f'{report} is safe after removing {report[i]}')
                    safe += 1
                    break
            else:
                print(f'{report} is not safe')

    print(safe)
