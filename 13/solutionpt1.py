from typing import Tuple


class Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Button(x={self.x}, y={self.y})"


class Case:
    def __init__(self, button_a: Button, button_b: Button, prize: Tuple[int, int]):
        self.button_a = button_a
        self.button_b = button_b
        self.prize = prize

    def __repr__(self):
        return f"Case(button_a={self.button_a}, button_b={self.button_b}, prize={self.prize})"


cases = []
button_a = None
button_b = None
prize = None
with open('13/input.txt', 'r') as file:
    i = 0
    while (line := file.readline()):
        if i % 4 == 3:
            i += 1
            continue

        x_y = line.split(':')[1].strip().split(', ')
        if i % 4 == 0:
            x = int(x_y[0].split('+')[1])
            y = int(x_y[1].split('+')[1])
            button_a = Button(x, y)
        elif i % 4 == 1:
            x = int(x_y[0].split('+')[1])
            y = int(x_y[1].split('+')[1])
            button_b = Button(x, y)
        elif i % 4 == 2:
            x = int(x_y[0].split('=')[1])
            y = int(x_y[1].split('=')[1])
            prize = (x, y)
            cases.append(Case(button_a, button_b, prize))
        i += 1


def solve(case: Case):
    button_a = case.button_a
    button_b = case.button_b
    prize = case.prize

    button_a_presses = button_b.y * prize[0] - button_b.x * prize[1]
    button_b_presses = button_a.x * prize[1] - button_a.y * prize[0]
    det = button_a.x * button_b.y - button_a.y * button_b.x

    if button_a_presses % det == 0 and button_b_presses % det == 0:
        return button_a_presses // det, button_b_presses // det
    else:
        return None


ans = 0
for case in cases:
    solution = solve(case)
    if solution:
        ans += 3*solution[0] + solution[1]

print(ans)