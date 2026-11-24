"""
Binary Tree
Name: RALF JANGAD

Builds a binary tree from the letters of the first and last name
(level by level, left to right) and displays it.
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


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def print_levels(root):
    """Prints the tree one level per line."""
    level = [root]
    depth = 0
    while level and any(level):
        letters = [n.letter for n in level if n]
        print(f"Level {depth}: {' '.join(letters)}")
        next_level = []
        for n in level:
            if n:
                next_level.append(n.left)
                next_level.append(n.right)
        level = next_level
        depth += 1


def print_tree(node, prefix="", is_left=True, is_root=True):
    """Prints a sideways picture of the tree (root at the left, right child on top)."""
    if node is None:
        return
    if node.right:
        print_tree(node.right, prefix + ("    " if is_root or not is_left else "|   "), False, False)
    connector = "" if is_root else ("\\-- " if is_left else "/-- ")
    print(prefix + connector + node.letter)
    if node.left:
        print_tree(node.left, prefix + ("    " if is_root or is_left else "|   "), True, False)


if __name__ == "__main__":
    root = build_tree(NAME)

    print("Name: RALF JANGAD")
    print("Letters:", " ".join(NAME))
    print()
    print_levels(root)
    print()
    print("Sideways view:")
    print_tree(root)
    print()
    print("Total nodes:", count_nodes(root))
    print("Height     :", height(root))
