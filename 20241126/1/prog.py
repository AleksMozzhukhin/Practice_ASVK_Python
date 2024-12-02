import sys

# Чтение всех данных из стандартного ввода в бинарном режиме
data = sys.stdin.buffer.read()

print(data)
# Первый байт — это идентификатор (N)
identifier = data[:1]
tail = data[1:]

# Получение численного значения первого байта
N = identifier[0]

# Размер хвоста
L = len(tail)

# Разделение хвоста на N частей
parts = []
for i in range(N):
    start = (i * L) // N
    end = ((i + 1) * L) // N
    parts.append(tail[start:end])

# Сортировка частей
sorted_parts = b"".join(sorted(parts))

# Формирование результата: идентификатор + отсортированные части
result = identifier + sorted_parts

# Вывод результата в стандартный вывод в бинарном режиме
sys.stdout.buffer.write(result)