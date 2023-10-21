# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        temp = newList
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                temp = temp.next
                list1 = list1.next
            else:
                temp.next = list2
                temp = temp.next
                list2 = list2.next
        if list1 or list2:
            temp.next = list1 if list1 else list2
        
        return newList.next
        

# traverse through both list at the same time, create a new list then record item in order

# to initialise ListNode, just do it with ListNode(), however there will be an initialised value as 0th item,
# therefore just return the next item to remove it
# by converting individual node value into a ListNode will cause the while loop to not consider the last item from each list
# therefore it's necessary to set the next of temp to the whole list, then move the list forward along with temp
# however in this case it will still lose 1 of the list, because without the last if statement
# both of the last item will be lost to the 2 lists, therefore the while condition should be while list1 - list 2
# the comparitor should be and, because this ensures that both list have a current value
# this will ensure the traversal will proceed to the very last item, then stop if there are no next item
# this way the list will always have the tail of the list no matter where you end the while loop