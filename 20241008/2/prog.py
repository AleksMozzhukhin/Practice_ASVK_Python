import math

# Read input
W, H, A, B, func_str = input().split(None, 4)
W = int(W)
H = int(H)
A = float(A)
B = float(B)
func_str = func_str.strip()

# Prepare the safe evaluation environment
allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
def f(x):
    try:
        allowed_names['x'] = x
        return eval(func_str, {"__builtins__": {}}, allowed_names)
    except Exception:
        return None

# Sample the function to find y_min and y_max
N_sample = max(W * 10, 1000)
xs_sample = [A + (B - A) * i / (N_sample - 1) for i in range(N_sample)]
ys_sample = [f(x) for x in xs_sample if f(x) is not None]
y_min = min(ys_sample)
y_max = max(ys_sample)

# Prepare for plotting
N_plot = W * 10
xs_plot = [A + (B - A) * i / (N_plot - 1) for i in range(N_plot)]
ys_plot = [f(x) for x in xs_plot]

# Map x and y to columns and rows
def x_to_c(x):
    return int((x - A) / (B - A) * (W - 1))

def y_to_r(y):
    return int((y_max - y) / (y_max - y_min) * (H - 1))

points = []
for x, y in zip(xs_plot, ys_plot):
    if y is None:
        continue
    c = x_to_c(x)
    r = y_to_r(y)
    points.append((c, r))

# Initialize the grid
grid = [[' '] * W for _ in range(H)]

# Line drawing function (Bresenham's algorithm)
def plot_line(grid, c0, r0, c1, r1):
    delta_c = c1 - c0
    delta_r = r1 - r0
    c_sign = 1 if delta_c >= 0 else -1
    r_sign = 1 if delta_r >= 0 else -1
    delta_c = abs(delta_c)
    delta_r = abs(delta_r)

    if delta_c > delta_r:
        err = delta_c / 2.0
        r = r0
        for c in range(c0, c1 + c_sign, c_sign):
            if 0 <= r < H and 0 <= c < W:
                grid[r][c] = '*'
            err -= delta_r
            if err < 0:
                r += r_sign
                err += delta_c
    else:
        err = delta_r / 2.0
        c = c0
        for r in range(r0, r1 + r_sign, r_sign):
            if 0 <= r < H and 0 <= c < W:
                grid[r][c] = '*'
            err -= delta_c
            if err < 0:
                c += c_sign
                err += delta_r

for i in range(len(points) - 1):
    c0, r0 = points[i]
    c1, r1 = points[i + 1]
    plot_line(grid, c0, r0, c1, r1)

for row in grid:
    print(''.join(row))
