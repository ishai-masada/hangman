def load_file(filename):
    with open(filename, "r") as f:
        raw_file = f.read()

    return [line.strip() for line in raw_file.splitlines() if line.strip()]


SAMPLE = load_file('sample.txt')

PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

AUTO_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def check_syntax(line):
    stack = []
    for char in line:
        # Opening brackets
        if char in PAIRS:
            stack.append(char)
        # Closing brackets
        else:
            if char == PAIRS[stack[-1]]:
                stack.pop()
            else:
                return POINTS[char]

def autocomplete(line):
    stack = []
    for char in line:
        # Opening brackets
        if char in PAIRS:
            stack.append(char)
        # Closing brackets
        else:
            if char == PAIRS[stack[-1]]:
                stack.pop()

    score = 0
    while stack:
        score *= 5
        opener = stack.pop()
        closer = PAIRS[opener]
        score += AUTO_POINTS[closer]
        line += closer
    return score


def part_one(lines):
    errors = [check_syntax(line) for line in lines]
    return sum([n for n in errors if n])


def part_two(lines):
    autocompleted = [autocomplete(line) for line in lines if not check_syntax(line)]
    return sorted(autocompleted)[len(autocompleted) // 2]


if __name__ == '__main__':
    assert part_one(SAMPLE) == 26397
    assert part_two(SAMPLE) == 288957

    INPUT = load_file('input.txt')
    print(part_one(INPUT))
    print(part_two(INPUT))

