# Day 7
# Crab Submarines
# Ishai Masada

with open('input.txt', 'r') as f:
    x_positions = [int(num) for num in f.read().split(',')]

def part_one(crab_positions):
    MIN_POSITION = min(x_positions)
    MAX_POSITION = max(x_positions)
    fuel_costs = {}

    for target_position in range(MIN_POSITION, MAX_POSITION):
        fuel_cost = 0
        for current_position in x_positions:
            fuel_cost += abs(current_position - target_position)
        fuel_costs[fuel_cost] = target_position

    cheapest_position, minimum_fuel_cost = fuel_costs[min(fuel_costs)], min(fuel_costs)
    print(f'minimum fuel cost: {minimum_fuel_cost}')

