# This is for practice with Binary Trees
# A Tree is a form of a Graph that is connected, directed and acyclic
# A Binary Tree is a tree that has at the MOST 2 Children(0 or 1 or 2)
# exactly one root Node
# exactly one path between root and any other node
# Depth First Search(DFS) traverses through the Node starting from Root then goes to the Roots leftmost leafs
# then goes to the right most leafs on the left side, then goes to the Roots right Node and does the same
# wit the example below DSF = a, b, d, e, c, f, g

# create a test graph
#      a
#    /   \
#   b      c
#  / \    / \
# d   e  f   g

#      4
#    /   \
#   2      6
#  / \    / \
# 1   3  5   7


class Node:
    def __init__(self, value):
        self.value = value
        self.right_node = None
        self.left_node = None


def depth_first_search(root_node):
    stack = [root_node]

    while len(stack) > 0:
        # pop current node from the stack and print its value
        current_node = stack.pop()
        print(current_node.value)

        # ------------check if the Current Node has any children--------------
        # append the right node first so that it is on the bottom of the stack
        if current_node.right_node:
            stack.append(current_node.right_node)
        # append the left node second so that it is on the top of the stack
        if current_node.left_node:
            stack.append(current_node.left_node)

    print("Congrats, you just performed a Depth First Search on some Nodes")
    return "Congrats, you just performed a Depth First Search on some Nodes"


a = Node(4)
b = Node(2)
c = Node(6)
d = Node(1)
e = Node(3)
f = Node(5)
g = Node(7)

a.left_node = b
a.right_node = c
b.left_node = d
b.right_node = e
c.left_node = f
c.right_node = g

dfs = depth_first_search(a)





