
def build_grid():
    matrix = {}
    parts_locations = []
    with open("input", "r") as file:
        current_row = 0
        for line in file:
            current_column = 0
            while line[current_column] != '\n':
                if line[current_column] == '.':
                    current_column += 1
                    continue
                if line[current_column] != '.' and not line[current_column].isdigit():
                    parts_locations.append((current_row, current_column))
                    current_column += 1
                    continue
                num_str = ""
                locations = []
                while line[current_column].isdigit():
                    num_str += line[current_column]
                    locations.append((current_row, current_column))
                    current_column += 1
                if len(locations) > 0:
                    for r, c in locations:
                        matrix[r, c] = num_str
            current_row += 1
    return matrix, parts_locations


if __name__ == '__main__':
    grid, parts = build_grid()
    print(grid)
    print(parts)
    part_numbers = []
    for part in parts:
        r = part[0]
        c = part[1]
        adj_cells = [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                     (r, c - 1), (r, c + 1),
                     (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]
        nums = set()
        for cell in adj_cells:
            if cell in grid:
                nums.add(int(grid[cell]))
        if len(nums) > 0:
            part_numbers.extend(list(nums))
    print(sum(list(part_numbers)))
