from collections import deque
from typing import List


# def bfs_by_queue(root):
#     queue = deque([root]) # at least one element in the queue to kick start bfs
#     while len(queue) > 0: # as long as there is an element in the queue
#         node = queue.popleft() # dequeue
#         for child in node.children: # enqueue children
#             if OK(child): # early return if problem condition met
#                 return FOUND(child)
#             queue.append(child)
#     return NOT_FOUND


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root: Node) -> List[List[int]]:
    ans = []
    # Create a double ended queue with ourroot
    queue = deque([root])
    while len(queue) > 0:
        current_level = []
        no_of_nodes = len(queue)

        for _ in range(no_of_nodes):
            curr_node = queue.popleft()
            current_level.append(curr_node.val)
            for child in [curr_node.left, curr_node.right]:
                if child is not None:
                    queue.append(child)
        ans.append(current_level)
    return ans


def zig_zag_traversal(root: Node) -> List[List[int]]:
    ans = []
    queue = deque([root])

    while len(queue) > 0:
        curr_level = []
        no_of_nodes = len(queue)

        for _ in range(no_of_nodes):
            node = queue.popleft()
            for child_node in [node.left, node.right]:
                if child_node is not None:
                    queue.append(child_node)
            curr_level.append(node.val)
        ans.append(curr_level[::-1]) if no_of_nodes % 2 == 0 else ans.append(curr_level)
    return []


def binary_tree_right_side_view(root: Node) -> List[int]:
    queue = deque([root])
    ans = []
    while len(queue) > 0:
        no_of_nodes = len(queue)
        for i in range(no_of_nodes):
            curr_node = queue.popleft()
            if i == no_of_nodes - 1:
                ans.append(curr_node.val)
            for child in [curr_node.left, curr_node.right]:
                if child is not None:
                    queue.append(child)
    return ans


def binary_tree_min_depth(root: Node) -> int:
    queue = deque([root])
    depth = 0
    while len(queue) > 0:
        no_of_nodes = len(queue)

        for _ in range(no_of_nodes):
            curr_node = queue.popleft()
            if curr_node.left is None and curr_node.right is None:
                return depth
            for child in [curr_node.left, curr_node.right]:
                if child is not None:
                    queue.append(child)
        depth += 1


if __name__ == "__main__":
    print("bfs")
