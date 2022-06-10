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


if __name__ == '__main__':
    test_root = Node(1)
    test_root.left = Node(2)
    test_root.left.left = Node(4)
    test_root.left.left.right = Node(7)

    test_root.left.right = Node(5)
    test_root.right = Node(3)
    test_root.right.right = Node(6)
    test_root.right.right.left = Node(8)
    print(is_balanced_helper(test_root))
