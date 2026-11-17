
from collections import deque

NAME = "JANGAD"

class Node:
    def __init__(self, letter):
        self.letter = letter
        self.left = None
        self.right = None


def build_binary_tree(name):

    nodes = [Node(ch) for ch in name]
    for i, node in enumerate(nodes):
        left, right = 2 * i + 1, 2 * i + 2
        if left < len(nodes):
            node.left = nodes[left]
        if right < len(nodes):
            node.right = nodes[right]
    return nodes[0] if nodes else None


def tree_bfs(root):

    result = []
    if root is None:
        return result
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.letter)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def preorder(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.letter)
        preorder(node.left, result)
        preorder(node.right, result)
    return result


def inorder(node, result=None):
    if result is None:
        result = []
    if node:
        inorder(node.left, result)
        result.append(node.letter)
        inorder(node.right, result)
    return result


def postorder(node, result=None):
    if result is None:
        result = []
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.letter)
    return result


def print_tree(node, prefix="", is_left=True, is_root=True):
    if node is None:
        return
    if node.right:
        print_tree(node.right, prefix + ("    " if is_root or not is_left else "│   "), False, False)
    connector = "" if is_root else ("└── " if is_left else "┌── ")
    print(prefix + connector + node.letter)
    if node.left:
        print_tree(node.left, prefix + ("    " if is_root or is_left else "│   "), True, False)



def build_graph():

    vertices = ["J", "A1", "N", "G", "A2", "D"]
    edges = [("J", "A1"), ("J", "N"), ("A1", "G"), ("A1", "A2"), ("N", "D")]

    graph = {v: [] for v in vertices}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def graph_bfs(graph, start):

    visited = {start}
    queue = deque([start])
    result = []
    while queue:
        v = queue.popleft()
        result.append(v)
        for w in graph[v]:
            if w not in visited:
                visited.add(w)
                queue.append(w)
    return result


def graph_dfs(graph, start):
    visited = set()
    stack = [start]
    result = []
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            result.append(v)
            # push in reverse so the first neighbor is visited first
            for w in reversed(graph[v]):
                if w not in visited:
                    stack.append(w)
    return result


def fmt(items):
    return " -> ".join(items)
if __name__ == "__main__":
    print(f"Name: {NAME}\n")

    print("=== Diagram 1: Binary tree ===")
    root = build_binary_tree(NAME)
    print_tree(root)
    print()
    print("BFS       :", fmt(tree_bfs(root)))
    print("Preorder  :", fmt(preorder(root)))
    print("Inorder   :", fmt(inorder(root)))
    print("Postorder :", fmt(postorder(root)))

    print("\n=== Diagram 2: Graph ===")
    graph = build_graph()
    for vertex, neighbors in graph.items():
        print(f"{vertex:>2} : {neighbors}")
    print()
    print("BFS :", fmt(graph_bfs(graph, "J")))
    print("DFS :", fmt(graph_dfs(graph, "J")))