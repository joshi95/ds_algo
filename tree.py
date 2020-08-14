class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

def preorder(root):
    if root is None:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def countLeaves(root):
    # Code here
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    leftans = countLeaves(root.left)
    rightans = countLeaves(root.right)
    return leftans + rightans

def printRootToLeafPaths(root, cur_path, all_paths):
    if root is None:
        return
    
    if root.left is None and root.right is None:
        cur_path.append(root.val)
        all_paths.append(cur_path[:])
        cur_path.pop()

    cur_path.append(root.val)
    printRootToLeafPaths(root.left, cur_path, all_paths)
    printRootToLeafPaths(root.right, cur_path, all_paths)
    cur_path.pop()


root = Node(1)
root.right = Node(8)
root.left = Node(5)
root.left.right = Node(7)
root.right.left = Node(9)
root.right.right = Node(10)

all_paths = []
printRootToLeafPaths(root, [], all_paths)
print(all_paths)