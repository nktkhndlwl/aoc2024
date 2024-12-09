import pdb

with open('9/input.txt', 'r') as file:
    line: str = file.read()

expanded_string = []
for i, c in enumerate(line):
    to_append = i//2 if i % 2 == 0 else '.'
    for _ in range(int(c)):
        expanded_string.append(to_append)

left_pointer = 0
right_pointer = len(expanded_string) - 1
while left_pointer < right_pointer:
    while expanded_string[right_pointer] == '.':
        right_pointer -= 1

    while expanded_string[left_pointer] != '.':
        left_pointer += 1

    if left_pointer >= right_pointer:
        break

    expanded_string[left_pointer], expanded_string[right_pointer] = expanded_string[right_pointer], expanded_string[left_pointer]
    left_pointer += 1
    right_pointer -= 1
    # print((ans := ''.join([str(x) for x in expanded_string])), len(ans))
    # pdb.set_trace()

ans = 0
for i in range(len(expanded_string)):
    if expanded_string[i] != '.':
        ans += i * expanded_string[i]
print(ans)
