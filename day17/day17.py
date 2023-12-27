
import heapq


def get_shortest_path(grid: list[list[int]], start: tuple[int], goal: tuple[int], max_straight: int, pre_turn: int):
    """ Determine the path with lowest cost from start to goal

    Args:
        grid (list[list[int]]): A 2D grid containing int values
        start (Point): Starting point
        goal (Point): Final point
        max_straight (int): Max moves we can make in a straight line before turning
        pre_turn (int): Max moves we must make before turning or stopping

    Raises:
        ValueError: If no solution

    Returns:
        int: best cost for path
    """
    queue = []  # priority queue to store current state

    cost: int = 0  # cumulative cost of all moves, based on value of each entered location
    current_position: tuple[int] = start
    direction = None  # Current direction. (None when we start.)
    straight_steps: int = 0  # number of steps taken in one direction without turning
    # cost must come first for our priority queue
    heapq.heappush(queue, (cost, current_position, direction, straight_steps))

    seen = set()

    while queue:
        cost, current_position, direction, straight_steps = heapq.heappop(
            queue)

        if current_position == goal and straight_steps >= pre_turn:
            return cost

        if (current_position, direction, straight_steps) in seen:
            continue
        seen.add((current_position, direction, straight_steps))

        next_states = []
        if direction is None:  # we're at the start, so we can go in any direction
            for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                neighbour = (
                    current_position[0] + d[0], current_position[1] + d[1])
                next_states.append((neighbour, d, 1))
        else:
            if straight_steps >= pre_turn:
                # turn 90 degrees CCW (left)
                next_states.append(
                    ((current_position[0] - direction[1], current_position[1] + direction[0]), (-direction[1], direction[0]), 1))
                # turn 90 degrees CW (right)
                next_states.append(
                    ((current_position[0] + direction[1], current_position[1] - direction[0]), (direction[1], -direction[0]), 1))
            if straight_steps < max_straight:  # we can move straight ahead.
                next_states.append(
                    ((current_position[0] + direction[0], current_position[1] + direction[1]), direction, straight_steps+1))
        for neighbour, direction, new_steps in next_states:
            if (0 <= neighbour[1] < len(grid[0]) and 0 <= neighbour[0] < len(grid)):
                new_cost = cost + grid[neighbour[0]][neighbour[1]]
                heapq.heappush(queue, (new_cost,
                                       neighbour,
                                       direction,
                                       new_steps))

    raise ValueError("No solution found")


def part1(field):  # works also for part 2
    start = (0, 0)
    goal = (len(field) - 1, len(field[0]) - 1)
    cost = get_shortest_path(field, start, goal, max_straight=10, pre_turn=4)
    return cost


if __name__ == "__main__":
    with open("day17_input.txt", "r") as f:
        lines = f.readlines()

    field = []
    for line in lines:
        line = line.strip()
        row = []
        for letter in line:
            row.append(int(letter))
        field.append(row)

    solution_part1 = part1(field)
    print("Solution Part 1: ", solution_part1)
