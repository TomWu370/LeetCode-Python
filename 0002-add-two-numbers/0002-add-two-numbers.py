# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        y = 0
        carry = 0
        answer = ListNode(0)
        next = answer
        while True:
            if l1:
                x = l1.val
                l1 = l1.next
            else:
                x = 0

            if l2:
                y = l2.val
                l2 = l2.next
            else:
                y = 0

            sum = x + y + carry
            if sum > 9:
                carry = 1
                sum -= 10
            else:
                carry = 0

            if not answer:
                answer = ListNode(sum)
            else:
                temp = ListNode(sum)
                next.next = temp
                next = temp
                
            if not (l1 or l2):
                if carry != 0:
                    temp = ListNode(carry)
                    next.next = temp
                    next = temp
                break
        return answer.next
# do until loop structure with while True, and if condition to break
# loop through l1 and l2
# to use linked list, you need to link the next with the head
# when you change the 'next' the head's next will follow the changes
# to append to next, make the next of the next into a new linked node, then make the current node into the new node
# the reason moving onto next node by using current = next node works is because this is not assignment
# but rather the lists are actually linked
