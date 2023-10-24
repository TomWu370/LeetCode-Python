# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        temp = head
        while temp:
            temp = temp.next
            size += 1
        groups = size//k
        previous = dummy = ListNode(0, head)
        while groups:
            current = previous.next # the head list
            nextNode = current.next # 2nd + elements from head
            for i in range(1,k):
                # reverse the list
                # 2nd Node = 3rd Node
                current.next = nextNode.next

                # 3rd node = head list
                nextNode.next = previous.next

                # head list linked with the swapped value
                previous.next = nextNode
                
                # update the nextNode value to be the rest of the list
                nextNode = current.next
            # update previous to be the new list that is not yet changed, to continue this operation
            previous = current
            
            groups -= 1
        return dummy.next
        

# first step would be to get the length of the list
# this will then allow us to calculate how many groups to reverse
# then create a new linked list but start from 0 then link to the head, this allows you to have a disposable node
# the idea is to iteratively move the next next up to K, back to the start of the subgroup
# e.g. if k=3 for the first test, then you'd move the 2 behind 1, then move 3 behind 2