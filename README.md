# Learning LZW compression algorithm

Just one of the things I'm learning. <https://github.com/hchiam/learning>

## Tutorial

<https://hackernoon.com/unixs-lzw-compression-algorithm-how-does-it-work-cp65347h> which in turn adapts a version of the code here: <https://github.com/adityagupta3006/LZW-Compressor-in-Python?ref=hackernoon.com>

## Notes

"[Unlike Huffman Encoding, LZW doesn’t require this dictionary to be included in the compressed data. One of the unique characteristics of this algorithm is that this dictionary can be rebuilt while uncompressing the data](https://hackernoon.com/unixs-lzw-compression-algorithm-how-does-it-work-cp65347h#NyWBLTdXEqWi5eDwzGGi:~:text=Unlike%20Huffman%20Encoding%2C%20LZW%20doesn%E2%80%99t%20require,be%20rebuilt%20while%20uncompressing%20the%20data.), ... [with the 256 ASCII codes as a preliminary step](https://hackernoon.com/unixs-lzw-compression-algorithm-how-does-it-work-cp65347h#NyWBLTdXEqWi5eDwzGGi:~:text=with%20the%20256%20ASCII%20codes%20as%20a%20preliminary%20step)." LZW can be implemented with variable-width encoding. A maximum width would then be used to put a cap on memory consumption, so once the dictionary is "filled", no more words can be added. LZW works better on data that has redundancy.

## Pseudocode

```python
def lzw(input: array):
    output = compressed_data
    dictionary.pre_filled_with(basic_ascii_chars)
    for word in input:
        if word in dictionary:
            output.add(dictionary[word])
        elif dictionary.is_full():
            output.add(word)
        else: # not in dictionary and dictionary has space
            dictionary.add(word)
            output.add(dictionary[word])
    return output
```

## Running the code in this repo

```bash
python encode_lzw.py # example_text.txt -> example_text.lzw
python decode_lzw.py # example_text.lzw -> example_text_decoded.txt
```
