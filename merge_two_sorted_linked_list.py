# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeTwoLists(self, list1, list2):
    head = None
    temp1 = list1
    temp2 = list2
    curr = None


    class Obj:
        def __init__(self,val):
            self.val = val
            self.next = None
    if temp1 == None:
        return temp2
    elif temp2 == None:
        return temp1    
    if temp1.val <= temp2.val:
        head = Obj(temp1.val)
        temp1 = temp1.next
    else:
        head = Obj(temp2.val)
        temp2 = temp2.next
    curr = head  
    while(not ((temp1 == None)|(temp2 == None))):
        if temp1.val <= temp2.val:
            curr.next = Obj(temp1.val)
            temp1 = temp1.next
        else:
            curr.next = Obj(temp2.val)
            temp2 = temp2.next
        curr = curr.next
    while(temp1 != None):
        curr.next = Obj(temp1.val)
        #print(f'after t1 {curr.val}')
        curr = curr.next
        temp1 = temp1.next
    while(temp2 != None):  
        curr.next = Obj(temp2.val)
        #print(f'after t2 {curr.val}')
        curr = curr.next
        temp2 = temp2.next
    return head