from Node import TreeNode

class BSTree:
    def __init__(self):
        self.root = None
        self.depth = 0

def insert(tree, dataval):
    if tree.root is None:
        tree.root = TreeNode(dataval)
    else:
        pointer1 = tree.root

        while pointer1 is not None:
            if pointer1.dataval > dataval:
                if pointer1.leftchild is None:
                    pointer1.leftchild = TreeNode(dataval)
                    return
                else:
                    pointer1 = pointer1.leftchild
            elif pointer1.dataval < dataval:
                if pointer1.rightchild is None:
                    pointer1.rightchild = TreeNode(dataval)
                    return
                else:
                    pointer1 = pointer1.rightchild
            else:
                pointer1.duplicates += 1
                return
    
def print_preorder(root):
    
    if root:
        print(root.dataval)

        print_preorder(root.leftchild)

        print_preorder(root.rightchild)

def print_postorder(root):

    if root:
        print_preorder(root.leftchild)

        print_preorder(root.rightchild)

        print(root.dataval)

def print_inorder(root):
    
    if root:
        print_preorder(root.leftchild)

        print(root.dataval)

        print_preorder(root.rightchild)

def search_n(root, dataval):
    
    
if __name__ == '__main__':
    tree = BSTree()

    insert(tree, 25)
    insert(tree, 15)
    insert(tree, 50)
    insert(tree, 10)
    insert(tree, 22)
    insert(tree, 4)
    insert(tree, 12)
    insert(tree, 18)
    insert(tree, 24)
    insert(tree, 35)
    insert(tree, 70)
    insert(tree, 31)
    insert(tree, 44)
    insert(tree, 66)
    insert(tree, 90)

    print_preorder(tree.root)

