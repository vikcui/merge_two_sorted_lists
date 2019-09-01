# author: YANG CUI
"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first
two lists.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    '''
    :time complexity: O(T) T being total number of nodes
    '''
    result = ListNode(0)
    listHeadResult = result
    if l1 == None:
        return l2
    elif l2 == None:
        return l1
    elif l1 == None and l2 == None:
        return None
    else:
        currentHeadl1 = l1
        currentHeadl2 = l2
        while currentHeadl1 != None or currentHeadl2 != None:
            if currentHeadl1 != None and currentHeadl2 != None:
                if currentHeadl1.val <= currentHeadl2.val:
                    result.next = ListNode(currentHeadl1.val)
                    currentHeadl1 = currentHeadl1.next
                elif currentHeadl1.val > currentHeadl2.val:
                    result.next = ListNode(currentHeadl2.val)
                    currentHeadl2 = currentHeadl2.next
            elif currentHeadl1 != None and currentHeadl2 == None:
                result.next= currentHeadl1
                return listHeadResult.next
            elif currentHeadl1 == None and currentHeadl2 != None:
                result.next = currentHeadl2
                return listHeadResult.next
            result = result.next
    return listHeadResult.next

# l1 = ListNode(-9)
# l1.next = ListNode(3)
# # l1.next.next = ListNode(4)
#
# l2 = ListNode(5)
# l2.next = ListNode(7)
# # l2.next.next = ListNode(3)
#
# mergeTwoLists(l1, l2)

