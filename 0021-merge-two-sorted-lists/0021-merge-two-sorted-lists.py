class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to start the merged list
        dummy = ListNode()
        tail = dummy  # Tail will point to the end of the merged list

        # Loop while both lists have nodes
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1  # Attach list1's node
                list1 = list1.next  # Move list1 pointer forward
            else:
                tail.next = list2  # Attach list2's node
                list2 = list2.next  # Move list2 pointer forward
            tail = tail.next  # Move the tail pointer forward

        # Attach remaining nodes from either list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # Return the head of the merged list (after the dummy node)
        return dummy.next
