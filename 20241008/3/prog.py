def format_line(line, fraction_str):
    spaces = total_output_width - len(line) - len(fraction_str)
    return f"{line}{' ' * spaces}{fraction_str}"


lines = []
while s := input():
    lines.append(s)
rows = len(lines)
cols = len(lines[0])
grid = [list(line) for line in lines]
rotated_cols = rows
rotated_rows = cols
rotated_grid = [[' ' for _ in range(rotated_cols)] for _ in range(rotated_rows)]
for i in range(rows):
    for j in range(cols):
        rotated_grid[j][rows - i - 1] = grid[i][j]
container = []
for i in range(1, rotated_rows - 1):
    container_row = []
    for j in range(1, rotated_cols - 1):
        container_row.append(rotated_grid[i][j])
    container.append(container_row)
total_cells = (rotated_rows - 2) * (rotated_cols - 2)
gas_cells = sum(row.count('.') for row in container)
liquid_cells = sum(row.count('~') for row in container)
container_height = len(container)
container_width = len(container[0])

liquid_rows = liquid_cells // container_width

if liquid_cells % container_width != 0:
    liquid_rows += 1
    liquid_cells = liquid_rows * container_width

for i in range(container_height):
    if i >= container_height - liquid_rows:
        container[i] = ['~'] * container_width
    else:
        container[i] = ['.'] * container_width

for i in range(1, rotated_rows - 1):
    for j in range(1, rotated_cols - 1):
        rotated_grid[i][j] = container[i - 1][j - 1]

for row in rotated_grid:
    print(''.join(row))

gas_fraction = gas_cells / total_cells
liquid_fraction = liquid_cells / total_cells

max_width = 20
max_fraction = max(gas_fraction, liquid_fraction)

gas_line_length = round((gas_fraction / max_fraction) * max_width)
liquid_line_length = round((liquid_fraction / max_fraction) * max_width)

gas_line_length = min(gas_line_length, max_width)
liquid_line_length = min(liquid_line_length, max_width)

gas_line = '.' * gas_line_length
liquid_line = '~' * liquid_line_length

gas_fraction_str = f"{gas_cells}/{total_cells}"
liquid_fraction_str = f"{liquid_cells}/{total_cells}"
max_fraction_length = max(len(gas_fraction_str), len(liquid_fraction_str))

total_output_width = max_width + 1 + max_fraction_length

print(format_line(gas_line, gas_fraction_str))
print(format_line(liquid_line, liquid_fraction_str))
