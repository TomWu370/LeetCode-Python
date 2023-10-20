# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n > 0:
            return head.next
        size = 1
        temp = head
        while temp.next:
            temp = temp.next
            size += 1
        temp = head

        if size-n == 0:
            return head.next

        for i in range(abs((size-n)+1)):

            if i == abs(size-n-1):
                if temp.next:
                    temp.next = temp.next.next
                else:
                    head.next = None
                return head

            if temp.next:
                temp = temp.next
             

# traverse through linked list
# remove from the back
# therefore there is a need to traverse through the list to get list length
# the key is how to remove a node
# delink the node by replacing current link with the next link
# since linked list are simply linked, you could declare a copy, then modify certain aspect of the list
# and it will affect the main list, for example traversing then redefining the next
# when n is larger than size then wrap it around using modulus
# handle edge case where the wrap around results in 0