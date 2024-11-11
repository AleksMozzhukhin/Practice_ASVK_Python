from collections import deque


class Maze:
    def __init__(self, N):
        self.N = N
        self.connections = {(x, y): set() for x in range(N) for y in range(N)}

    def __setitem__(self, key, value):
        if not (isinstance(key, tuple) and len(key) == 3 and isinstance(key[1], slice)):
            raise TypeError("Key must be a tuple of the form (x0, slice(y0, x1, None), y1)")

        x0 = key[0]
        slice_obj = key[1]
        y1 = key[2]

        y0 = slice_obj.start
        x1 = slice_obj.stop

        if y0 == y1:
            step = 1 if x1 > x0 else -1
            for x in range(x0, x1, step):
                room1 = (x, y0)
                room2 = (x + step, y0)
                if value == "·":
                    self.connections[room1].add(room2)
                    self.connections[room2].add(room1)
                elif value == "█":
                    self.connections[room1].discard(room2)
                    self.connections[room2].discard(room1)
        elif x0 == x1:
            # Вертикальный проход от (x0, y0) до (x1, y1)
            step = 1 if y1 > y0 else -1
            for y in range(y0, y1, step):
                room1 = (x0, y)
                room2 = (x0, y + step)
                if value == "·":
                    self.connections[room1].add(room2)
                    self.connections[room2].add(room1)
                elif value == "█":
                    self.connections[room1].discard(room2)
                    self.connections[room2].discard(room1)

    def __getitem__(self, key):
        if not (isinstance(key, tuple) and len(key) == 3 and isinstance(key[1], slice)):
            raise TypeError("Key must be a tuple of the form (x0, slice(y0, x1, None), y1)")

        x0 = key[0]
        slice_obj = key[1]
        y1 = key[2]

        y0 = slice_obj.start
        x1 = slice_obj.stop

        start = (x0, y0)
        end = (x1, y1)

        if start == end:
            return True

        visited = set()
        queue = deque()
        queue.append(start)
        visited.add(start)

        while queue:
            current = queue.popleft()
            for neighbor in self.connections[current]:
                if neighbor == end:
                    return True
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False

    def __str__(self):
        size = 2 * self.N + 1
        grid = [['█' for _ in range(size)] for _ in range(size)]
        for x in range(self.N):
            for y in range(self.N):
                grid[2 * y + 1][2 * x + 1] = '·'
        for (x, y), neighbors in self.connections.items():
            for (nx, ny) in neighbors:
                dx = nx - x
                dy = ny - y
                if dx == 1 and dy == 0:
                    # Проход вправо
                    grid[2 * y + 1][2 * x + 2] = '·'
                elif dx == -1 and dy == 0:
                    # Проход влево
                    grid[2 * y + 1][2 * x] = '·'
                elif dx == 0 and dy == 1:
                    # Проход вниз
                    grid[2 * y + 2][2 * x + 1] = '·'
                elif dx == 0 and dy == -1:
                    # Проход вверх
                    grid[2 * y][2 * x + 1] = '·'
        maze_rows = [''.join(row) for row in grid]
        return '\n'.join(maze_rows)

while s:=input():
    exec(s)

