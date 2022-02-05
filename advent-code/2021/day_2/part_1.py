# Day 2
# Horizontal Position and Depth
# Ishai Masada
import re

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

def depth(direction, value):
    global depth
    if direction == 'up':
        depth += value
    else:
        depth -= value

def add_horizontal(direction, value):
    global horizontal_position
    horizontal_position += value

groups = re.findall(r'(\w+) (\d)', directions)

commands = {'up': depth, 'forward': add_horizontal, 'down': depth}
depth = 0
horizontal_position = 0

for group in groups:
    direction, value = group[0], int(group[1])
    commands.get(direction)(direction, value)

product = abs(depth)*horizontal_position
print(product)
