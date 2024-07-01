from typing import Optional

# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head: Optional[Node]) -> Optional[Node]:
        previous, current = None, head

        while current:
            print("current ref: ", current)
            print(f"Current Node: val={current.val}, next={current.next.val if current.next else None}")
            if current.next:
                print(f"Next Node Value: {current.next.val}")
            else:
                print("Next Node: None")
            temp = current.next    # next node of `current` is stored in the `temp` reference
            print("temp ref: ", temp)
            print('reverse the pointer of `current` to point to `previous` node')
            current.next = previous     # reverse the pointer of `current` to point to `previous` node
            if current.next:
                print(f"Next Node Value: {current.next.val}")
            else:
                print("Next Node: None")
            print("previous ref: ", previous)
            print("update `previous` reference to point to the `current` node")
            previous = current          # update `previous` reference to point to the `current` node
            print("previous ref: ", previous)
            print("update `current` reference forward to the next node `temp`")
            current = temp        # update `current` reference forward to the next node `temp`
            print("_________________")

        return previous


if __name__ == "__main__":
    s = Solution()
    node2 = Node(20, None)
    node1 = Node(1, node2)

    # Reverse the linked list starting from node1
    reversed_head = s.reverse(node1)
    

    # Print the reversed linked list
    while reversed_head:
        print(reversed_head.val, end=" ")
        reversed_head = reversed_head.next
