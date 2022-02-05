# Day 7
# Crab Submarines
# Ishai Masada

with open('input.txt', 'r') as f:
    x_positions = [int(num) for num in f.read().split(',')]

def part_two(crab_positions):
    MIN_POSITION = min(crab_positions)
    MAX_POSITION = max(crab_positions) + 1
    fuel_costs = {}

    def sum_of_integers(number):
        return int((number * (number + 1)) / 2)

    for target_position in range(MIN_POSITION, MAX_POSITION):
        fuel_cost = 0
        for current_position in x_positions:
            fuel_cost += sum_of_integers(abs(current_position - target_position))
        fuel_costs[fuel_cost] = target_position


    cheapest_position, minimum_fuel_cost = fuel_costs[min(fuel_costs)], min(fuel_costs)
    print(f'minimum fuel cost: {minimum_fuel_cost}')

part_two(x_positions)
