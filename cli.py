from core import BST, Node

def run_cli():
    tree = BST()
    print("""Binary Search Tree Interface Active:
Type 'help' for more information
Type "quit" to exit interface.""")
    while True:
        user_input = input("> ").strip()
        if user_input == "quit":
            break
        if user_input == "print":
            tree.print_tree()
            continue
        if user_input == "help":
            print("""insert  : insert an item into the tree.
delete args : Remove an item from the tree
print  args : Print the tree out.
search args : find an item in the tree.""")
            continue
        if len(user_input.split()) != 2:
            print("Invalid Input, missing valid arguments.")
            continue
        user_input= user_input.split()
        command = user_input[0]
        arg = user_input[1]
        try:
            arg = int(arg)
        except:
            print("Invalid argument.Type 'help' for command info")
            continue
        if command == "insert":
            tree.insert(arg)
            print("Insertion succesful")
        elif command == "search":
            search = tree.search(arg)
            if search is None:
                print("Not found")
                continue
            else:
                print(f"({search.value}) found with left child ({search.left.value if search.left is not None else search.left}) and right child ({search.right.value if search.right is not None else search.right})")
        elif command == "delete":
            tree.delete(arg)
            print("Deletion successful")
        else:
            print("Invalid command\nType 'help' to see command info.")
        
run_cli()
        