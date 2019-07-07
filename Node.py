class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None
        self.previousval = None

class TreeNode:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.rightchild = None
        self.leftchild = None
        self.duplicates = 0