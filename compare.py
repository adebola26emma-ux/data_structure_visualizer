from core import BST
from plain_bst import PlainBST

def compare(values):
    avl = BST()
    plain = PlainBST()
    for v in values:
        try:
            v = int(v)
        except:
            print("Non integer input")
            return None
        avl.insert(v)
        plain.insert(v)
    print("AVL Tree:")
    avl.print_tree()
    print('\nPlain BST:')
    plain.print_tree()
    
if __name__ == "__main__":
    compare([1, 2, 3, 4, 5, 6, 7])
    