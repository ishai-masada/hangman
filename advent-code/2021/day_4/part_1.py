# Day 4
# Bingo
# Ishai Masada


class Board:
    def __init__(self, rows):
        self.rows = rows

    def row(self, row_index):
        return self.rows[row_index]

    def column(self, col_index):
        return [row[col_index] for row in self.rows]

    def is_finished(self):
        rows = self.rows
        columns = [self.column(i) for i in range(len(rows))]
        for line in rows + columns:
            if all([isinstance(elem, bool) for elem in line]):
                return True
        return False

    def cross(self, mark):
        for y, row in enumerate(self.rows):
            for x, elem in enumerate(row):
                if elem == mark:
                    self.rows[y][x] = True
        return self.is_finished()

def load_file(filename):
    with open(filename, 'r') as f:
        groups = f.read().split('\n\n')
        order, boards = list(map(int, groups[0].split(','))), groups[1:]
        boards = [
            Board(
                [list(map(int, row.split())) for row in board.splitlines()]
            )
            for board in boards
        ]
        return order, boards

def part_one(boards, order):
    for mark in order:
        for board in boards:

            # Check if the board is finished
            if board.cross(mark):

                # Remove all of the Trues in the board
                for row_index, row in enumerate(board.rows):
                    board.rows[row_index] = [elem for elem in row if elem is not True]

                # Find the sum of all of the unmarked numbers in the board
                board_sum = 0
                for row in board.rows:
                    board_sum += sum(row)

                # Multiply the sum of the unmarked numbers by the number that finished the board
                score = board_sum * mark
                return score

if __name__ == '__main__':
    order, boards = load_file('sample.txt')
    print(part_one(boards, order))
