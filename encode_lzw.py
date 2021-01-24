import sys
from sys import argv
from struct import *


def compress():
    # Building and initializing the dictionary.
    dictionary_size = 256
    dictionary = {chr(i): i for i in range(dictionary_size)}

    # We'll start off our phrase as empty and add characters to it as we encounter them
    phrase = ""

    # This will store the sequence of codes we'll eventually write to disk
    compressed_data = []

    # Load the text
    input_file = open(input_file_name)
    data = input_file.read()

    # Iterating through the input text character by character
    for symbol in data:

        # Get input symbol.
        string_plus_symbol = phrase + symbol

        # If we have a match, we'll skip over it
        # This is how we build up to support larger phrases
        if string_plus_symbol in dictionary:
            phrase = string_plus_symbol
        else:

            # We'll add the existing phrase (without the breaking character) to our output
            compressed_data.append(dictionary[phrase])

            # We'll create a new code (if space permits)
            if(len(dictionary) <= maximum_table_size):
                dictionary[string_plus_symbol] = dictionary_size
                dictionary_size += 1
            phrase = symbol

    if phrase in dictionary:
        compressed_data.append(dictionary[phrase])

    # Storing the compressed string into a file (byte-wise).
    out = input_file_name.split(".")[0]
    output_file = open(out + ".lzw", "wb")

    for data in compressed_data:
        # Saves the code as an unsigned short
        output_file.write(pack('>H', int(data)))

    output_file.close()
    input_file.close()


# Usage
input_file_name = "example_text.txt"

# Defining the maximum table size
# It's important that the encoder and decoder agree on the code_width
code_width = 12
maximum_table_size = pow(2, int(code_width))

compress()
