# https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        obj = {}
        Bool = True
        head = None
        #make a dict out of all the nodes
        while Bool:
            for i in range(len(lists)):
                if lists[i]:
                    try:
                        obj[lists[i].val].append(lists[i])
                    except:
                        obj[lists[i].val] = [lists[i]]
                    lists[i] = lists[i].next
                    Bool = False
            Bool = not Bool
        #use that dict in a sorted order to get each node
        arr = list(obj.keys())
        arr.sort()
        for i in arr:
            for j in obj[i]:
                if head:
                    temp.next = j
                    temp = temp.next
                else:
                    head = j
                    temp = head
        # print(head)
        return head