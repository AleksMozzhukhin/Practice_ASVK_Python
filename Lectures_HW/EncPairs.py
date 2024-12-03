import sys

encodings = ['koi8-r', 'cp1251', 'mac_cyrillic', 'cp866', 'iso8859_5','cp855']

data = sys.stdin.buffer.read()

for initial_encoding in encodings:
    for source_encoding in encodings:
        for target_encoding in encodings:
            try:
                text = data.decode(target_encoding).encode(source_encoding).decode(initial_encoding)
                if 'Зимбабве' in text:
                    print(text, end="")
                    sys.exit(0)
            except (UnicodeDecodeError, UnicodeEncodeError):
                continue