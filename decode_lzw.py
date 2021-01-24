import sys
from sys import argv
import struct
from struct import *


def decompress():
    # Default values in order to read the compressed file
    compressed_data = []
    next_code = 256
    decompressed_data = ""
    phrase = ""

    # Reading the compressed file.
    while True:
        rec = file.read(2)
        if len(rec) != 2:
            break
        (data, ) = unpack('>H', rec)
        compressed_data.append(data)

    # Building and initializing the dictionary.
    dictionary_size = 256
    dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])

    # Iterating through the codes.
    # LZW Decompression algorithm
    for code in compressed_data:

        # If we find a new
        if not (code in dictionary):
            dictionary[code] = phrase + (phrase[0])

        decompressed_data += dictionary[code]

        if not(len(phrase) == 0):
            # Ensures we don't exceed the bounds of the table
            if(len(dictionary) <= maximum_table_size):
                dictionary[next_code] = phrase + (dictionary[code][0])
                next_code += 1
        phrase = dictionary[code]

    # storing the decompressed string into a file.
    out = input_file_name.split(".")[0]
    output_file = open(out + "_decoded.txt", "w")
    for data in decompressed_data:
        output_file.write(data)

    output_file.close()
    file.close()


# Usage
code_width = 12
maximum_table_size = pow(2, int(code_width))

input_file_name = "example_text.lzw"
file = open(input_file_name, "rb")

decompress()
