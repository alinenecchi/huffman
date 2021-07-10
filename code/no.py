class Node:
    def __init__(self, number, letter="", left=None, right=None):
        self.number = number
        self.letter = letter
        self.parent = None
        self.code = ""
        self.right = right
        self.left = left