import string
from typing import List
from math import inf


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_max_depth(node: Node) -> int:
    # If the node is none then just return 0
    if node is None:
        return 0

    return max(tree_max_depth(node.left), tree_max_depth(node.right)) + 1


def visible_tree_node(node: Node, max_so_far: int) -> int:
    if node is None:
        return 0

    total = 0
    if node.val >= max_so_far:
        total += 1

    total += visible_tree_node(node.left, max(max_so_far, node.val))
    total += visible_tree_node(node.right, max(max_so_far, node.val))
    return total


# Draw this out on Ipad
def is_balanced(node: Node) -> int:
    if node is None:
        return 0
    # Post Order traversal - Start deep far left
    # Post Order lets this problem be O(N)
    left_tree_height = is_balanced(node.left)
    right_tree_height = is_balanced(node.right)
    # If either of our children have violated our height requirement we already lost
    if left_tree_height == -1 or right_tree_height == -1:
        return -1
    # Check if there is a violation
    if abs(left_tree_height - right_tree_height) > 1:
        return -1
    # Return the height
    return max(left_tree_height, right_tree_height) + 1


def is_balanced_helper(node: Node) -> bool:
    return is_balanced(node) != -1


def serialize(root: Node):
    arr_to_stringify = []

    def dfs(node: Node):
        # Current node first operations
        if node is None:
            arr_to_stringify.append('N')
            return
        arr_to_stringify.append(str(node.val))
        # Current node first operations
        # Deep left
        dfs(node.left)
        # then right
        dfs(node.right)

    dfs(root)
    return ' '.join(arr_to_stringify)


# Other person in the comments uses a stack, which makes more sense to me as I don't know the context of iterator
def deserialize(s: string):
    def dfs(token_iterator: List):
        # Pop removes the index passed in , we remove the top element on the stack
        current_token = token_iterator.pop(0)
        # If we reached a leaf then return a null pointer, this is what splits our tree as well

        if current_token == "N":
            return None
        # Set our parent nodes value -> preorder
        new_node = Node(int(current_token))
        # Deep left tree
        new_node.left = dfs(token_iterator)
        # Deep right tree
        new_node.right = dfs(token_iterator)
        return new_node

    # Passing in an interator that we will recursively consume
    char_arr = s.split()
    return dfs(char_arr)


def print_preorder(curr_node: Node):
    if curr_node is None:
        print("Null")
        return

    print(curr_node.val)
    print_preorder(curr_node.left)
    print_preorder(curr_node.right)
    return


def lca(root, node1, node2):
    def dfs(curr_node, n1, n2):
        # Leaf
        if curr_node is None:
            return None
        # Bubble up that we found one of then nodes
        if curr_node is n1 or curr_node is n2:
            return curr_node
        # DFS
        left_side_ancestor = dfs(curr_node.left, n1, n2)
        right_side_ancestor = dfs(curr_node.right, n1, n2)
        # If we found both of our children in the current node we found the LCA
        if left_side_ancestor and right_side_ancestor:
            return curr_node
        # Bubble up that we found the left child in this current DFS
        if left_side_ancestor:
            return left_side_ancestor
        # Bubble up that we found the right child in this current DFS
        if right_side_ancestor:
            return right_side_ancestor
        # Bubble up that we found neither, means both are in the other half
        return None

    dfs(root, node1, node2)


def valid_bst(root: Node) -> bool:
    def dfs(curr_node, min_val, max_val):
        if curr_node is None:
            return True

        if not min_val <= curr_node.val <= max_val:
            return False
        # Less than parent
        left_side = dfs(curr_node.left, min_val, curr_node.val)
        # Greater than parent
        right_side = dfs(curr_node.right, curr_node.val, max_val)

        return left_side and right_side

    return dfs(root, -inf, inf)


def insert_bst(tree: Node, val: int):
    def dfs(curr_node, to_insert):
        if curr_node is None:
            curr_node = Node(to_insert)
            return curr_node

        if val < curr_node.val:
            dfs(curr_node.left, val)
        elif val > curr_node.val:
            dfs(curr_node.right, val)
        # Same value
        return curr_node

    return dfs(tree, val)


def invert_bt(tree: Node):
    def dfs(parent):
        if parent is None:
            return None

        parent.left, parent.right = parent.right, parent.left

        dfs(parent.left)
        dfs(parent.right)
        return parent

    dfs(tree)


if __name__ == '__main__':
    bst = Node(8)
    bst.left = Node(4)
    bst.left.left = Node(2)
    bst.left.right = Node(7)
    bst.right = Node(12)
    bst.right.right = Node(13)
    bst.right.left = Node(11)
    print(valid_bst(bst))
    insert_bst(bst, 23)
    print(valid_bst(bst))
