Referencias 
-> Written By Jonathan Richard
-> https://www.section.io/engineering-education/huffman-coding-python/
-> https://www.techrepublic.com/article/huffman-coding-in-python/
-> https://bhrigu.me/post/huffman-coding-python-implementation/
-> https://github.com/Vnicius/python-arvore-de-huffman

Department of Electrical Engineering Universitas Indonesia
# huffmancoding-Python
This repository contains one encode script and one decode script. The encode script will generate the huffman table and export it to table.txt, and encode the following string  and then export it to compressed.bin .The decode function generates the huffman tree from the available huffman table in table.txt, and then proceeds to decode the byte file to the original string. Compatible with C# Huffman Coding code in my repositiory (the encoded file here can be decoded with the C# code, and vice versa.)

# Source code contents
## BitArray Version
This version is much faster but requires the BitArray package acquirable in Pip. Compatible only with Python 3. 
## Standard Version
Slower version, this version could be easily ported into MicroPython (and has been tested before) because it only used standard libraries of python. 

# Usage
### Put your string into sample.txt 
### Run main.py
### New files are created: encode.bin is the encoded string and sample.txt contains the huffman code. 


