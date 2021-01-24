import sys
from sys import argv
import struct
from struct import *


def is_dictionary_full(dictionary, maximum_table_size):
    return len(dictionary) > maximum_table_size


def decompress(input_file_name):
    # initializing some values:
    compressed_data = []
    next_code = 256
    output = ""
    word = ""

    file = open(input_file_name, "rb")

    while True:
        file_contents = file.read(2)
        have_no_more_data_in_file_contents = len(file_contents) != 2
        if have_no_more_data_in_file_contents:
            break
        # get data from file contents:
        (data, ) = unpack('>H', file_contents)
        compressed_data.append(data)

    dictionary_size = 256
    dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])

    for code in compressed_data:
        if not (code in dictionary):
            dictionary[code] = word + (word[0])

        output += dictionary[code]

        if not(len(word) == 0):
            # Ensures we don't exceed the bounds of the table
            if not is_dictionary_full(dictionary, maximum_table_size):
                dictionary[next_code] = word + (dictionary[code][0])
                next_code += 1

        word = dictionary[code]

    # save decompressed string back to plaintext .txt file:
    output_file_name = input_file_name.split(".")[0]
    output_file = open(output_file_name + "_decoded.txt", "w")

    for character in output:
        output_file.write(character)

    output_file.close()
    file.close()


input_file_name = "example_text.lzw"

code_width = 12

maximum_table_size = pow(2, int(code_width))

decompress(input_file_name)
