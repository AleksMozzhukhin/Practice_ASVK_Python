import sys

input_text = sys.stdin.read()

bytes_cp1251 = input_text.encode('latin1', errors='replace')

output_text = bytes_cp1251.decode('cp1251', errors='replace')

print(output_text, end='')
