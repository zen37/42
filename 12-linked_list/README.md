```python
def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head

    while curr:
        temp = curr.next  # Temporarily store the next node of `curr`
        curr.next = prev  # Reverse the pointer of `curr` to point to `prev`
        prev = curr       # Update `prev` to point to the current node (`curr`)
        curr = temp       # Move `curr` to the next node (`temp`), advancing in the original list

    return prev  # Return the new head of the reversed linked list
```

### Explanation:

1. **Initialization**:
   - `prev, curr = None, head`: Initialize `prev` as `None` (initially the last node of the reversed list) and `curr` as `head` (the first node of the original list).

2. **While Loop**:
   - `while curr:`: Continue iterating as long as `curr` is not `None`, meaning there are nodes left in the original list to process.

3. **Pointer Reversal**:
   - `temp = curr.next`: Temporarily store the next node (`curr.next`) in `temp` to preserve the remaining original list.
   - `curr.next = prev`: Reverse the pointer of `curr` to point backwards to `prev`, integrating `curr` into the reversed list.
   - `prev = curr`: Update `prev` to point to the current node (`curr`). Now `prev` is a pointer to `curr`, which is the next node in the reversed list.
   - `curr = temp`: Move `curr` forward to `temp`, which is the next node in the original list. This advances the iteration through the original list.

4. **Return Statement**:
   - `return prev`: Once the loop completes (`curr` becomes `None`), `prev` points to the head of the reversed list. Return `prev`, which is now the head of the reversed linked list.

### Clarified Example:

Suppose you have a linked list `1 -> 2 -> 3 -> None`. Here’s how the `reverse` method progresses:

- Initial state: `prev = None`, `curr = ListNode(1)`
- First iteration:
  - `temp = curr.next` (stores `ListNode(2)`)
  - `curr.next = prev` (ListNode(1).next points to `None`)
  - `prev = curr` (prev becomes a pointer to `ListNode(1)`)
  - `curr = temp` (curr moves to `ListNode(2)`)
- Second iteration:
  - `temp = curr.next` (stores `ListNode(3)`)
  - `curr.next = prev` (ListNode(2).next points to `ListNode(1)`)
  - `prev = curr` (prev becomes a pointer to `ListNode(2)`)
  - `curr = temp` (curr moves to `ListNode(3)`)
- Third iteration:
  - `temp = curr.next` (stores `None`)
  - `curr.next = prev` (ListNode(3).next points to `ListNode(2)`)
  - `prev = curr` (prev becomes a pointer to `ListNode(3)`)
  - `curr = temp` (curr becomes `None`, exiting the loop)
- Return `prev`, which is now a pointer to `ListNode(3)`, the head of the reversed list (`3 -> 2 -> 1 -> None`).

### Conclusion:

In the `reverse` method:
- `prev` starts as `None` and eventually becomes a pointer to the last node in the reversed list.
- `curr` starts as `head` and moves through the original list.
- After reversing the pointer of `curr` to point to `prev`, `prev` is updated to point to `curr`. This effectively makes `prev` a pointer to the next node in the reversed list as we progress through the loop.
  
This process effectively builds the reversed linked list in-place, and `prev` correctly represents the head of the reversed list after the loop completes.