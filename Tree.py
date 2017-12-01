import sys


# Python Program to find the size of binary tree


# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return "%s-%s-%s" % (self.data, self.left, self.right)


index = 0


# Computes the number of nodes in tree
def size(node):
    if node is None:
        return 0
    else:
        return size(node.left) + 1 + size(node.right)


def height(node):
    if node is None:
        return 0
    else:
        return 1 + (max(height(node.left), height(node.right)))


def checkBalanced(node):
    if node is None:
        return True

    tree_height = height(node.left) - height(node.right)
    # print(str(node) + " - " + str(tree_height))
    if abs(tree_height) > 1:
        return False
    else:
        return (checkBalanced(node.left) and checkBalanced(node.right))


def checkBalancedHeight(node):
    if node is None:
        return -1

    left_height = checkBalancedHeight(node.left);
    if left_height == sys.maxsize:
        return sys.maxsize

    right_height = checkBalancedHeight(node.right)
    if right_height == sys.maxsize:
        return sys.maxsize

    if abs(left_height - right_height) > 1:
        return sys.maxsize
    else:
        return 1 + max(left_height, right_height)


def isTreeBalanced(node):
    if checkBalancedHeight(node) == sys.maxsize:
        return False
    else:
        return True


def inOrder(node):
    if node is None:
        return None
    print(inOrder(node.left))
    print(node.data)
    print(inOrder(node.right))


def copyBST(node, array):
    global index
    if node is None:
        return
    copyBST(node.left, array)
    array[index] = node.data
    index = index + 1
    copyBST(node.right, array)


def checkBst(node, min_value, max_value):
    if node is None:
        return True

    if (min_value is not None and node.data <= min_value) or (max_value is not None and node.data > max_value):
        return False

    if checkBst(node.left, min_value, node.data) is False or checkBst(node.right, node.data, max_value) is False:
        return False

    return True


def printAllPaths2Leaf(node, path):
    if node.left is None and node.right is None:
        print(path + str(node.data))
        return;
    else:
        path = path + str(node.data)
        # print(node.data);
        if node.left is not None:
            printAllPaths2Leaf(node.left, path)
        if node.right is not None:
            printAllPaths2Leaf(node.right, path)


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(10)

root.right.right = Node(8)
root.right.right.right = Node(7)

print("Size of the tree is %d" % (size(root)))
print("height of the tree is %d" % (height(root)))
print("is tree Balances - %s" % checkBalanced(root))
print("is tree balanced - optimized - %s" % isTreeBalanced(root))
# print(inOrder(root))
print("IS BST %s" % (checkBst(root, None, None)))
print(printAllPaths2Leaf(root, ''))
