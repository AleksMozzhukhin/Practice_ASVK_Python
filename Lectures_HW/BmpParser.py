import struct
import sys

file_data = sys.stdin.buffer.read()

if file_data[:2] != b'BM':
    print("Not a Windows BMP")
    exit()

bmp_size, = struct.unpack_from("<I", file_data, 2)
if bmp_size != len(file_data):
    print("Incorrect size")
    exit()

dib_header_size, = struct.unpack_from("<I", file_data, 14)
known_dib_sizes = [12, 40, 52, 56, 108, 124]
if dib_header_size not in known_dib_sizes:
    print("Incorrect header size")
    exit()
if dib_header_size == 12:
    width, height, planes, bpp = struct.unpack_from("<HHHH", file_data, 18)
else:
    width, height = struct.unpack_from("<ii", file_data, 18)
    planes, bpp = struct.unpack_from("<HH", file_data, 26)

abs_height = abs(height)
if dib_header_size >= 40:
    compression, = struct.unpack_from("<I", file_data, 30)
else:
    compression = 0
if dib_header_size >= 40:
    image_size, = struct.unpack_from("<I", file_data, 34)
else:
    image_size = 0

row_size = ((width * bpp + 31) // 32) * 4
calculated_image_size = row_size * abs_height

if image_size == 0:
    image_size = calculated_image_size
elif image_size not in (calculated_image_size, calculated_image_size + 2):
    print("Incorrect image size")
    exit()

filler_size = 0 if image_size == calculated_image_size else 2

print(width, abs_height, bpp, compression, filler_size)
