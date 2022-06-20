from typing import List


class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children


def ternary_tree_paths(root: Node) -> List[str]:
    ans = []

    def dfs(curr_node, curr_path):
        # The state is if all of our children are None (leaf)
        if all(children is None for children in curr_node.children):
            ans.append('->'.join(curr_path) + '->' + str(curr_node.val))
            return
        # DFS do work on our current node
        curr_path.append(str(curr_node.val))
        # For each child in our current node dfs and get their children onto our path
        for child in curr_node.children:
            dfs(child, curr_path)
        # If we reach this it means we have appended our path to our string, and we will recursively pop to the root
        curr_path.pop()

    if root: dfs(root, [])
    return ans


# Why cant we go down the list
# a b c
#
def permutations(letters: str) -> List[str]:
    ans = []

    def dfs(curr_path, letters_used):
        # if state is a solution
        if len(curr_path) == len(letters):
            ans.append(''.join(curr_path))
            return

        for i, letter, in enumerate(letters):
            if letters_used[i]:
                continue
            # DFS
            curr_path.append(letter)
            letters_used[i] = True

            dfs(curr_path, letters_used)
            # backtracking --> this happens after we appended one of our solutions
            curr_path.pop()
            letters_used[i] = False

    if letters:
        dfs([], [False] * len(letters))
    return ans


# 56


def letter_combinations_of_phone_number(digits: str) -> List[str]:
    ans = []
    letter_combo = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def dfs(curr_path):
        # State to check for completion
        if len(curr_path) == len(digits):
            ans.append("".join(curr_path))
            return
        # The length of our current path gives us the index for the next digit

        next_number = digits[len(curr_path)]
        for letter in letter_combo[next_number]:
            curr_path.append(letter)
            dfs(curr_path)
            # back_track
            curr_path.pop()

    if digits: dfs([])
    return ans


def word_break(s: str, words: List[str]) -> bool:
    memo = {}

    def dfs(index):
        if index == len(s):
            return True
        if index in memo:
            return memo[index]

        is_valid = False
        for word in words:
            if s[index:].startswith(word):
                if dfs(index + len(word)):
                    is_valid = True
        memo[index] = is_valid
        return is_valid

    return dfs(0)


def decode_ways(digits: str) -> int:
    prefixes = []
    for i in range(1, 27):
        prefixes.append(str(i))

    def dfs(index):
        # Report State Checl
        if index == len(digits):
            return 1

        # Find the recursive index somehow
        ways = 0
        remaining_digits = digits[index:]
        # Search for DFS
        for prefix in prefixes:
            if remaining_digits.startswith(prefix):
                ways += dfs(index + len(prefix))
        # Backtrack

        return ways

    return dfs(0)



def partition(s: str) -> List[List[str]]:
    ans = []

    def check_palindrome(word: str):
        return word == word[::-1]

    def dfs(start_index, curr_path):
        # State Check
        # @NOTE generally always length based
        # Reached the end of parsing our array
        if start_index == len(s):
            ans.append("".join(curr_path))
            return
        # start_index = 0
        # a a b
        # 0 1 2
        # i = start_index + 1 = 1
        # word_to_check = s[0 - 1]
        for i in range(start_index + 1, len(s) + 1):
            word_to_check = s[start_index: i]
            if check_palindrome(word_to_check):
                dfs(i, curr_path + [word_to_check])


    if s:
        dfs(0, [])
    return ans


if __name__ == "__main__":
    print(permutations("abc"))
