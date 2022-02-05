# Day 25
# Sea Cucumbers
# Ishai Masada

# All of the east herds move simultaneously first and then the south herds afterwards

def load_file(file_name):
    with open(file_name, 'r') as f:
        initial_state = [list(line) for line in f.read().splitlines()]

    return initial_state

def part_one(board_state):
    HERDS = ['>','v']
    while True:
        number_of_moves = 0
        for row_idx, line in enumerate(board_state):
            for col_idx, elem in enumerate(line):

                if elem not in HERDS:
                    continue

                # If the east elem is at the end of the line and the first elem is open
                elif elem == HERDS[0] and col_idx == len(line) - 1 and line[0] not in HERDS:
                    board_state[row_idx][0] = elem
                    line[-1] = '.'

                # If the south elem is at the bottom and the same column space at the
                # top row is open
                elif elem == HERDS[1] and row_idx == len(board_state) - 1 and board_state[0][col_idx] not in HERDS:
                    board_state[0][col_idx] = elem
                    board_state[0][col_idx] = '.'

                # If the elem is an east herd and the next space is open
                elif elem == HERDS[0] and line[col_idx +1] not in HERDS:
                    line[col_idx + 1] = elem
                    line[col_idx + 1] = '.'

                # If the elem is a south herd and the space underneath it is open
                elif elem == HERDS[1] and board_state[row_idx +1][col_idx] not in HERDS:
                    board_state[row_idx +1][col_idx] = elem
                    line[col_idx] = '.'

                number_of_moves += 1

            if number_of_moves == 0:
                break

    end_state = board_state

    return end_state

if __name__ == '__main__':
    initial_state = load_file('sample.txt')
    print(part_one(initial_state))
