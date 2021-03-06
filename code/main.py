from no import Node
import os
import timeit

startingnodes = ""
start_time = timeit.default_timer()
def read_file(filename):
    letters_frequency = {}
    file = open(filename, "r")
    while True:
        char = file.read(1)
        if not char:
            break
        if char in letters_frequency:
            letters_frequency[char] += 1
        else:
            letters_frequency[char] = 1
    return letters_frequency


def create_tree(x):
    print("Arquivo que está sendo comprimido: " + x)
    start_time = timeit.default_timer()
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
    final_time = timeit.default_timer() - start_time
    print("\nTempo de execução de criação da arvore: ",final_time)


def print_results():
    #global startingnodes
    list_code_str = ""
    #print("letras- frequencia - code bin")
    for i in startingnodes:
        tmp = i
        while tmp.parent is not None:
            i.code += tmp.parent.code
            tmp = tmp.parent
    for i in startingnodes:
        #print("   " + i.letter + "        " + str(i.number) + "         " + i.code[::-1])
        list_code_str += i.code
    creatFile("encode.bin", list_code_str)


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
    


def creatFile(file_name, text):  # escreve um arquivo com o texto em binário
    try:
        file = open(file_name, 'w')
        file.write(text)
        file.close()
    except IOError:
        raise print("Erro ao criar o arquivo")


startingnodes = []
#create_tree("sample.txt")
create_tree("input.in")
give_codes(find_top())
print_results()

path_input = os.path.abspath("input.in")
input_size = os.path.getsize(path_input)

#path_sample = os.path.abspath("sample.txt")
#ascii_size = os.path.getsize(path_sample)

path_encode = os.path.abspath("encode.bin")
huff_size = os.path.getsize(path_encode)

#print('ASCII File Size:', ascii_size, 'bytes')
print('Input File Size:', input_size, 'bytes')
print('Huffman File Size:', huff_size, 'bytes')

#print('Redução de sample.txt: {:.2f}%'.format((100-(huff_size*100/ascii_size))))
print('Redução de input.in: {:.2f}%'.format((100-(huff_size*100/input_size))))

final_time = timeit.default_timer() - start_time
print("\nTempo de execução do processo: ",final_time)
