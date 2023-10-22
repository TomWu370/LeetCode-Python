# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2):
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
        list1 = None
        for i in range(len(lists)):
            if i == 0:
                list1 = lists[i]
                continue
            list1 = mergeTwoLists(list1, lists[i])

        return list1


# similar to merging 2 sorted linked list
# however for each list, sort ith and i+1th list, then make ith list value into the resulting merged list
# continue until you merged each list individually, then return the ith list
# however for this particular question, the non intended but quicker way to solve is to
# push all the values in the lists into a priority queue, sorted then reassemble back into a linked list