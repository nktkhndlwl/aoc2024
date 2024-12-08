def check(answer: int, numbers: list[int]) -> bool:
    def calculate_possibilities(current_value: int, index: int) -> bool:
        if index >= len(numbers):
            return current_value == answer

        if calculate_possibilities(current_value + numbers[index], index + 1):
            return True

        if calculate_possibilities(current_value * numbers[index], index + 1):
            return True

        return False

    if not numbers:
        return False

    return calculate_possibilities(numbers[0], 1)


with open('7/input.txt') as f:
    lines = [line.strip().split(': ') for line in f.readlines()]
    lines = [(int(line[0]), [int(n) for n in line[1].split(' ')]) for line in lines]

total = 0
for line in lines:
    if check(line[0], line[1]):
        total += line[0]

print(total)
