import sys
import binascii
import tarfile
import io


hex_data = sys.stdin.read()
hex_data = hex_data.replace(" ", "").replace("\n", "")
binary_data = binascii.unhexlify(hex_data)
with tarfile.open(fileobj=io.BytesIO(binary_data), mode="r:*") as tar:
    total_files = 0
    total_size = 0
    for member in tar.getmembers():
        if member.isfile():
            total_files += 1
            total_size += member.size

    print(total_size, total_files)

