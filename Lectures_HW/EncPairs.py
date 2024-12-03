import sys

encodings = {
    'KOI8-R': 'koi8-r',
    'CP1251': 'cp1251',
    'MACCYRILLIC': 'mac_cyrillic',
    'CP866': 'cp866',
    'ISO-8859-5': 'iso8859_5',
    'CP855': 'cp855',
}

encoding_list = list(encodings.values())

data = sys.stdin.buffer.read()

for initial_encoding in encoding_list:
    for source_encoding in encoding_list:
        for target_encoding in encoding_list:
            try:
                text1 = data.decode(target_encoding)
                bytes2 = text1.encode(source_encoding)
                text2 = bytes2.decode(initial_encoding)
                if 'Зимбабве' in text2:
                    print(text2)
                    sys.exit(0)
            except (UnicodeDecodeError, UnicodeEncodeError):
                continue
print("No encoding find")