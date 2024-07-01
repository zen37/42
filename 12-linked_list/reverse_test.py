from reverse import ListNode, Solution  # Assuming your main script is named reverse.py

# Helper function to create a linked list from a list of values
def create_linked_list_1(values):
    if not values:
        return None
    """
    Following statement creates a list called nodes where each element is a ListNode object initialized with values from the values list.
    For example, if values = [1, 2, 3], then nodes will be a list containing [ListNode(1), ListNode(2), ListNode(3)].
    """
    nodes = [ListNode(val) for val in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    return nodes[0]

def create_linked_list_2(values):
    if not values:
        return None
    
    # Create the first node
    head = ListNode(values[0])
    current = head
    
    # Iterate through the rest of the values to create and link nodes
    for val in values[1:]:
        new_node = ListNode(val)
        current.next = new_node
        current = new_node
    
    return head

test_cases = [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([2, 1], [1, 2]),
    ([], [])
]

# Test function
def test_reverse():
    s = Solution()
    for input_list, expected_output in test_cases:
        head = create_linked_list_1(input_list)
        reversed_head = s.reverse(head)
        result = []
        while reversed_head:
            result.append(reversed_head.val)
            reversed_head = reversed_head.next
        assert result == expected_output