class Node:
    def __init__(self, data):
        self.left = None
        self.right = None

def calculateMaxDepth(n):
    if n is None:
        return 0
    left_depth = calculateMaxDepth(n.left)
    right_depth = calculateMaxDepth(n.right)
    print(left_depth, right_depth)
    return max(left_depth, right_depth) + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(4)


"""
max(calculateMaxDepth(n.left), calculateMaxDepth(n.right)) + 1
=> max (max(0, 0) + 1, max(calculateMaxDepth(n.left) , calculateMaxDepth(n.right))+ 1) + 1
=> max (1, max(0, max(0, 0 ) + 1 )+ 1 ) + 1
=> max (1, max(0, 1) + 1) + 1
=> max (1, 2)  + 1
=> 2 + 1 = 3


"""


# Calculate the depth of the binary tree
depth = calculateMaxDepth(root)
print("Depth of the binary tree:", depth)

