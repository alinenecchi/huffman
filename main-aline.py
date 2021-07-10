import os

class Node:
    def __init__(self, number, letter="", left=None, right=None):
        self.number = number
        self.letter = letter
        self.parent = None
        self.code = ""
        self.right = right
        self.left = left

startingnodes = ""
def read_file(x):
    letters_frequency = {}
    f = open(x, "r")
    while True:
        char = f.read(1)
        if not char:
            break
        if char in letters_frequency:
            letters_frequency[char] += 1
        else:
            letters_frequency[char] = 1
    f.close()
    return letters_frequency


def create_tree(x):
    print ("Arquivo que está sendo comprimido: "+ x)
    #global startingnodes
    letters_frequency = read_file(x)
    for i, j in letters_frequency.items():
        startingnodes.append(Node(j, i))
    nodes = startingnodes.copy()
    while len(nodes) > 1:
        nodes.sort(key=lambda o: o.number)
        n = Node(nodes[0].number + nodes[1].number, "", nodes[0], nodes[1])
        nodes[0].parent = n
        nodes[1].parent = n
        del nodes[0]
        del nodes[0]
        nodes.append(n)


def print_results():
    #global startingnodes
    list_code_str = ""
    print("letras- frequencia - code bin")
    for i in startingnodes:
        tmp = i
        while tmp.parent is not None:
            i.code += tmp.parent.code
            tmp = tmp.parent
    for i in startingnodes:
        print("   " + i.letter + "        " + str(i.number) + "         " + i.code[::-1])
        print("   " + i.letter + "        " + str(i.number) + "         " + i.code[::-1])
        list_code_str += i.code
    creatFile("result.bin", list_code_str)
    print("Codigo gerado: " + list_code_str)

def find_top():
    top = startingnodes[0]
    while top.parent is not None:
        top = top.parent
    return top


def give_codes(current):
    if current.left is not None:
        current.left.code = "1"
        give_codes(current.left)
    if current.right is not None:
        current.right.code = "0"
        give_codes(current.right)

def readb(filename):
    f = open(filename, "r")
    txt = str(f)
    print(txt.encode(encoding="ascii", errors="ignore"))

def creatFile(file_name, text):
 try:
     file = open(file_name, 'w')	
     file.write(text)
     file.close()
 except IOError:
     raise print("Erro ao criar o arquivo")

startingnodes = []
create_tree("sample.txt")

give_codes(find_top())
print_results()
file_size = os.path.getsize(r'C:\Users\aline\huffman\sample.txt')
print('sample.txt:', file_size, 'bytes')
file_size_end = os.path.getsize(r'C:\Users\aline\huffman\result.bin')
print('Result.bin:', file_size_end, 'bytes')