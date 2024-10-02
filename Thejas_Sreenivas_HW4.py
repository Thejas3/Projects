class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def last_remaining(n, k):
    # Create circular linked list
    head = ListNode(0)  # Create the head of the linked list
    current = head
    for i in range(1, n):
        current.next = ListNode(i)
        current = current.next
    current.next = head  # Make it circular by linking the last node to head

    # Simulate the game
    while current.next != current:
        # Move k-1 steps
        for _ in range(k - 1):
            current = current.next
        # Remove the next node
        current.next = current.next.next

    return current.value    #Return the value of the last remaining node

def tree_info(node):
    # Helper function to calculate tree height
    def calculate_height(node):
        if node is None:
            return 0
        else:
            return 1 + max(calculate_height(node.left), calculate_height(node.right))

    # Helper function to count leaf nodes
    def count_leaves(node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        else:
            return count_leaves(node.left) + count_leaves(node.right)

    # Helper function to check if the tree is full
    def is_full(node):
        if node is None:
            return True
        elif node.left is None and node.right is None:
            return True
        elif node.left is not None and node.right is not None:
            return is_full(node.left) and is_full(node.right)
        else:
            return False

    # Helper function to check if the tree is balanced
    def is_balanced(node):
        if node is None:
            return True
        lh = calculate_height(node.left)
        rh = calculate_height(node.right)
        if abs(lh - rh) <= 1 and is_balanced(node.left) and is_balanced(node.right):
            return True
        return False

    height = calculate_height(node)
    leaf_count = count_leaves(node)
    is_full_tree = "Yes" if is_full(node) else "No"
    is_balanced_tree = "Yes" if is_balanced(node) else "No"

    print("Height of the tree:", height)
    print("Number of leaf nodes:", leaf_count)
    print("Is Full:", is_full_tree)
    print("Is Balanced:", is_balanced_tree)

# Example usage:

# Task 1
n = 11  # Number of people in the group
k = 2   # Steps in one iteration of the rhyme
result = last_remaining(n, k)
print("Last remaining member:", result)

# Task 2
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Constructing the binary tree
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))

tree_info(root)
