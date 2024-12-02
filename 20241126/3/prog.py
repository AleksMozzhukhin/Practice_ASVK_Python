import sys
import struct

def parse_wav_header(file_path):
    try:
        with open(file_path, 'rb') as f:
            header = f.read(44)
            if len(header) < 44:
                return "NO"
            riff, file_size, wave, fmt, fmt_size = struct.unpack('<4sI4s4sI', header[:20])
            if riff != b'RIFF' or wave != b'WAVE' or fmt != b'fmt ' or fmt_size != 16:
                return "NO"
            audio_format, num_channels, sample_rate, byte_rate, block_align, bits_per_sample = struct.unpack('<HHIIHH', header[20:36])

            if audio_format != 1:
                return "NO"

            data_marker = header[36:40]
            if data_marker != b'data':
                return "NO"

            data_size = struct.unpack('<I', header[40:44])[0]

            return f"Size={file_size}, Type={audio_format}, Channels={num_channels}, Rate={sample_rate}, Bits={bits_per_sample}, Data size={data_size}"

    except Exception as e:
        return "NO"

file_path = sys.stdin.read().strip()
result = parse_wav_header(file_path)
print(result)

