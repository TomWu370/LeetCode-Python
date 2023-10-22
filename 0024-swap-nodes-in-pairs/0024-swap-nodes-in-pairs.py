# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recurse(head):
            second = None
            if head and head.next:
                second = ListNode(head.next.val)
                current = ListNode(head.val)
      
                current.next = recurse(head.next.next) if head.next else head.next
                second.next = current
                return second
            else:
                return head

        return recurse(head)
        

# recursively go through list
# check if has next item
# if True, then create temp Node with next item as value, set the next as the current node value
# then finally set the next of that to the current list's next next value
# check if exist, with if not list.next and list.next.next
# otherwise set to None
# then set current.next as recursion of the current operation