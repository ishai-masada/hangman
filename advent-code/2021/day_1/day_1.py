
with open('day_1.txt', 'r') as f:
    measurements = f.read()

# measurements = '''199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263'''

measurements = [int(line.strip()) for line in measurements.splitlines() if line.strip()]

def part_1():
    count = 0

    for idx, measurement in enumerate(measurements):
        if idx == 0:
            continue
        else:
            if measurement > measurements[idx-1]:
                count += 1

    print(count)

def part_2():
    count = 0

    for idx, measurement in enumerate(measurements):
        if idx == 0:
            continue
        else:
            try:
                current_window = sum(measurements[idx:idx+3])
                previous_window = sum(measurements[idx-1:idx+3-1])
                if current_window > previous_window:
                    count += 1
            except:
                break

    print(count)

part_2()
