# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # visited = set()
        # current = head
        # while current:
        #     if current in visited:
        #         return True
        #     visited.add(current)
        #     current = current.next
        # return False

        #Floyd's tortoise hare algorithm - slow and fast pointers

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next # moves one step at a go
            fast = fast.next.next # moves two steps at a go
            if slow == fast:
                return True

        return False









        