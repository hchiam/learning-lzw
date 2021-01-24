import sys
from sys import argv
from struct import *


def is_dictionary_full(dictionary, maximum_table_size):
    return len(dictionary) > maximum_table_size


def compress():
    dictionary_size = 256  # ASCII codes starting point
    dictionary = {chr(i): i for i in range(dictionary_size)}

    phrase = ""

    output = []

    input_file = open(input_file_name)
    input = input_file.read()

    for character in input:

        word = phrase + character

        if word in dictionary:
            phrase = word
        else:
            output.append(dictionary[phrase])

            if not is_dictionary_full(dictionary, maximum_table_size):
                dictionary[word] = dictionary_size
                dictionary_size += 1

            phrase = character

    if phrase in dictionary:
        output.append(dictionary[phrase])

    # save compressed string to .lzw file:
    output_file_name = input_file_name.split(".")[0]
    output_file = open(output_file_name + ".lzw", "wb")

    for input in output:
        # save as unsigned short:
        output_file.write(pack('>H', int(input)))

    output_file.close()
    input_file.close()


input_file_name = "example_text.txt"

code_width = 12  # must match the encoding width of the decoder!

maximum_table_size = pow(2, int(code_width))

compress()
