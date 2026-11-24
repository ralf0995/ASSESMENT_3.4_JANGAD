"""
Assessment 3.6: DFS Method in Tree
Name: RALF JANGAD

Builds a binary tree from the letters of the first and last name
(level by level, left to right) and prints the three DFS traversals:
Preorder, Inorder and Postorder.
"""

NAME = "RALFJANGAD"


class Node:
    def __init__(self, letter):
        self.letter = letter
        self.left = None
        self.right = None


def build_tree(name):
    """Level-order insertion: children of index i are 2i+1 and 2i+2."""
    nodes = [Node(ch) for ch in name]
    for i, node in enumerate(nodes):
        left, right = 2 * i + 1, 2 * i + 2
        if left < len(nodes):
            node.left = nodes[left]
        if right < len(nodes):
            node.right = nodes[right]
    return nodes[0] if nodes else None


def preorder(node, result):
    """Root -> Left -> Right"""
    if node is None:
        return
    result.append(node.letter)
    preorder(node.left, result)
    preorder(node.right, result)


def inorder(node, result):
    """Left -> Root -> Right"""
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.letter)
    inorder(node.right, result)


def postorder(node, result):
    """Left -> Right -> Root"""
    if node is None:
        return
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.letter)


def run(traversal, root):
    result = []
    traversal(root, result)
    return " -> ".join(result)


if __name__ == "__main__":
    root = build_tree(NAME)

    print("Name: RALF JANGAD")
    print("Tree letters (level by level):", " ".join(NAME))
    print()
    print("Preorder  (Root, Left, Right):", run(preorder, root))
    print("Inorder   (Left, Root, Right):", run(inorder, root))
    print("Postorder (Left, Right, Root):", run(postorder, root))
