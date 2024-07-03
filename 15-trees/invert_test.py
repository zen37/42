# test_solution.py
import pytest
from invert import TreeNode, Solution

# Helper function to build a binary tree from a list of values
def build_tree(nodes):
    if not nodes:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in nodes]
    root = nodes[0]
    idx = 0
    for node in nodes:
        if node:
            if idx + 1 < len(nodes):
                node.left = nodes[idx + 1]
            if idx + 2 < len(nodes):
                node.right = nodes[idx + 2]
            idx += 2
    return root

# Helper function to convert a binary tree to a list
def tree_to_list(root):
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    return result

# Test cases using pytest
class TestSolution:

    @pytest.mark.parametrize("input_tree, expected_output", [
        ([2, 1, 3], [2, 3, 1]),
        ([1, None, 2], [1, 2, None]),
        ([], [])
    ])
    def test_invertTree(self, input_tree, expected_output):
        sol = Solution()
        root = build_tree(input_tree)
        inverted_root = sol.invertTree(root)
        inverted_list = tree_to_list(inverted_root)
        assert inverted_list == expected_output

if __name__ == "__main__":
    pytest.main()
