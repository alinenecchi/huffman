class Node:
    def __init__(self, number, letter="", left=None, right=None):
        self.number = number
        self.letter = letter
        self.parent = None
        self.code = ""
        self.right = right
        self.left = left


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
    global startingnodes
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
    global startingnodes
    print("letras- frequencia - code bin")
    for i in startingnodes:
        tmp = i
        while tmp.parent is not None:
            i.code += tmp.parent.code
            tmp = tmp.parent
    for i in startingnodes:
       
        print("   "+ i.letter + "        " + str(i.number) + "         " + i.code[::-1])


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


startingnodes = []
create_tree("string.txt")
give_codes(find_top())
print_results()