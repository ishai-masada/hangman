import re
# Day 2
# Horizontal Position and Depth
# Ishai Masada

with open('day_2.txt', 'r') as f:
    directions = f.read()

# directions = '''
# forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2
# '''

def depth():
    global direction
    global aim
    global value
    if direction == 'up':
        aim += value
    else:
        aim -= value

def add_horizontal():
    global horizontal_position
    global value
    global depth

    horizontal_position += value
    depth += (aim*value)

groups = re.findall(r'(\w+) (\d)', directions)

commands = {'up': depth, 'forward': add_horizontal, 'down': depth}
depth = 0
horizontal_position = 0
aim = 0

for group in groups:
    direction, value = group[0], int(group[1])
    commands.get(direction)()

product = abs(depth)*horizontal_position
print(product)
