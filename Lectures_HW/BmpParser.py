import struct
import sys


def read_bmp(file_data):
    """
    Разбирает заголовки BMP-файла и проверяет их соответствие формату.
    """
    # Проверка сигнатуры "BM" (первые 2 байта)
    if file_data[:2] != b'BM':
        return "Not a Windows BMP"

    # Читаем размер BMP-файла (байты 2–6)
    bmp_size, = struct.unpack_from("<I", file_data, 2)
    if bmp_size != len(file_data):
        return "Incorrect size"

    # Читаем размер DIB header (байты 14–18)
    dib_header_size, = struct.unpack_from("<I", file_data, 14)
    known_dib_sizes = [12, 40, 52, 56, 108, 124]  # Возможные размеры DIB header
    if dib_header_size not in known_dib_sizes:
        return "Incorrect header size"

    # Читаем ширину, высоту и глубину цвета
    if dib_header_size == 12:  # BITMAPCOREHEADER
        width, height, planes, bpp = struct.unpack_from("<HHHH", file_data, 18)
    else:  # Все остальные форматы DIB
        width, height = struct.unpack_from("<ii", file_data, 18)
        planes, bpp = struct.unpack_from("<HH", file_data, 26)

    # Проверка, что высота может быть отрицательной (отражает направление)
    abs_height = abs(height)

    # Читаем метод упаковки (байты 30–34)
    if dib_header_size >= 40:
        compression, = struct.unpack_from("<I", file_data, 30)
    else:
        compression = 0  # Для старых заголовков метод упаковки не задаётся

    # Читаем размер изображения (байты 34–38)
    if dib_header_size >= 40:
        image_size, = struct.unpack_from("<I", file_data, 34)
    else:
        image_size = 0  # Размер не задан

    # Вычисляем размер строки в пикселях (с учётом выравнивания)
    row_size = ((width * bpp + 31) // 32) * 4  # Выравнивание на 4 байта
    calculated_image_size = row_size * abs_height

    # Проверка размера изображения
    if image_size == 0:
        image_size = calculated_image_size
    elif image_size not in (calculated_image_size, calculated_image_size + 2):
        return "Incorrect image size"

    # Вычисляем размер заполнителя
    filler_size = 0 if image_size == calculated_image_size else 2

    # Возвращаем информацию о файле
    return f"{width} {abs_height} {bpp} {compression} {filler_size}"


def main():
    # Чтение данных BMP из стандартного ввода
    file_data = sys.stdin.buffer.read()
    result = read_bmp(file_data)
    print(result)


if __name__ == "__main__":
    main()
