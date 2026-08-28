from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class PlainBST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if node is None:
            return Node(value)
        elif value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        return node
    
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                successor = self._find_min(node.right)
                node.value = successor.value
                node.right = self._delete_recursive(node.right, successor.value)
        return node
                
    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def search(self, value):
        return self._search_recursive(self.root, value)
            
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def print_tree(self):
        if self.root is None:
            print("(empty tree)")
            return
        
        queue = deque([self.root])
        while queue:
            level_size = len(queue)
            level_values = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(str(node.value))
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            print(" ".join(level_values))
            
if __name__ == "__main__":
    tree = PlainBST()
    for val in [1, 2, 3, 4, 5, 6, 7]:
        tree.insert(val)
    tree.print_tree()