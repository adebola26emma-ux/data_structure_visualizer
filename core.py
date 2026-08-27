from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.height = 1
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        """Public insert method the handles an empty tree
        and calls the private method otherwise."""
        self.root = self._insert_recursive(self.root, value)
            
    def _insert_recursive(self, node, value):
        """Main insert method that inputs new nodes into the tree."""
        if node is None:
            return Node(value)
        elif value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)
        
        if balance > 1:
            if self._get_balance(node.left) >= 0:
                node = self._rotate_right(node)
            else:
                node = self._rotate_left_right(node)
        elif balance < -1:
            if self._get_balance(node.right) <= 0:
                node = self._rotate_left(node)
            else:
                node = self._rotate_right_left(node)
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
                
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)
        
    def _delete_recursive(self, node, value):
        if node is None: 
            return node # Case of value not found
        #finding the node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Case 1: leaf node
            
            # Case 2a: only right child
            if node.left is None:
                node = node.right
            
            # Case 2b: only left child
            elif node.right is None:
                node = node.left
            
            # Case 3: two children
            else:
                # Find the successor (smallest value in right subtree)
                successor = self._find_min(node.right)
                
                # replace this node with the successor's value
                node.value = successor.value
                
                node.right = self._delete_recursive(node.right, successor.value)
        if node is None:
            return node
        node.height = 1 + max(self._get_height(node.right), self._get_height(node.left))
        balance = self._get_balance(node)
        if balance > 1:
            if self._get_balance(node.left) >= 0:
                node = self._rotate_right(node)
            else:
                node = self._rotate_left_right(node)
        elif balance < -1:
            if self._get_balance(node.right) <= 0:
                node = self._rotate_left(node)
            else:
                node = self._rotate_right_left(node)
        return node
    
    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    
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
    
    def _get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
        
    def _rotate_right(self, node):
        z = node
        y = z.left
        t = y.right
        
        y.right = z
        z.left = t
        
        #Height updates z comes first cus its lower in the new tree.
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y
    
    def _rotate_left(self, node):
        x = node
        y = x.right
        t = y.left
        
        y.left = x
        x.right = t
        
        #Height updates x comes first cus its lower in the new tree.
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y
    
    def _rotate_left_right(self, node):
        y = node.left
        node.left = self._rotate_left(y)
        return self._rotate_right(node)
    
    def _rotate_right_left(self, node):
        node.right = self._rotate_right(node.right)
        return self._rotate_left(node)
    
    def is_valid_bst(self, node=None, low=float('-inf'), high=float('inf')):
        if node is None:
            node = self.root
            if node is None:
                return True  # empty tree is trivially valid

        if not (low < node.value < high):
            return False
        left_ok = True
        right_ok = True
        if node.left is not None:
            left_ok = self.is_valid_bst(node.left, low, node.value)
        if node.right is not None:
            right_ok = self.is_valid_bst(node.right, node.value, high)
        return left_ok and right_ok
if __name__ == "__main__":
    tree = BST()
    for val in [9, 5, 10, 0, 6, 11, -1, 1, 2]:
        tree.insert(val)
    print("------------------------------")
    print(tree.is_valid_bst())   # True or False?

    tree.delete(10)
    tree.delete(11)
    tree.delete(9)
    print("------------------------------")

    print(tree.is_valid_bst())   # True or False?