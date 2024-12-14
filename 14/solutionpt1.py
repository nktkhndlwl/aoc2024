with open('14/input.txt', 'r') as file:
    lines = file.readlines()

T = 100
x_max = 101
y_max = 103
lines = [line.strip() for line in lines]

pos = []
for i in range(len(lines)):
    line = lines[i]
    p = line.split(' ')[0].split('=')[1]
    v = line.split(' ')[1].split('=')[1]
    px = int(p.split(',')[0])
    py = int(p.split(',')[1])
    vx = int(v.split(',')[0])
    vy = int(v.split(',')[1])
    x_final = (px + vx * T) % x_max
    y_final = (py + vy * T) % y_max
    pos.append((x_final, y_final))

x_mid = x_max // 2  # 50
y_mid = y_max // 2  # 51

q1 = 0
q2 = 0
q3 = 0
q4 = 0

for x, y in pos:
    if x < x_mid and y < y_mid:
        q1 += 1
    elif x < x_mid and y > y_mid:
        q2 += 1
    elif x > x_mid and y < y_mid:
        q3 += 1
    elif x > x_mid and y > y_mid:
        q4 += 1

print(q1 * q2 * q3 * q4)
