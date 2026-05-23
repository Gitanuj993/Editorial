
# Leetcode Question 21 , Merge two sorted linked lists : approach_2

## Question :
 Task is to merge two sorted Linked list , for illustration  <br>
say `` list1 is 1 -> 3 -> 4 -> None `` and `` list2 is : 1 -> 2 -> 4 -> None `` <br>
then Merged linked list would be : `` 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None ``


## Central Idea 
We will traverse and compare each linked list and compare the elements of both the  lists,
smaller element wil be added first in the merged_list. 


## Approach_2 
Instead of creating New node each time , we reused reference of the previous node into the 'temp.next' instead of value.

### key changes.
1. renamed 'val' to 'node'
2. changed literal of 'val' from ``list1.val `` to `` list1`` everywhere.



```pycon
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # when first list is None and Another list is not None
        if ( (list1 == None ) and  ( (list2 != None)) ) :
            return  list2
        elif ( (list1 != None ) and  (list2 == None)) :
            return list1
        elif ( ( list1 is None) and (list2 is None)) :
            return None
        # merge_sort
        head = ListNode() 
        # temp 
        temp = head

        # merging list
        while ( list1 is not None) or ( list2 is not None) :
            # when any of the list becomes None
            if ( list1 is not None) and ( list2 is None) :
                node = list1
                list1 = list1.next
            elif ( list1 is None) and ( list2 is not None) :
                node = list2
                list2 = list2.next
            else :
                if (list1.val <= list2.val) :
                    node = list1
                    list1 = list1.next
                else :
                    node = list2
                    list2 = list2.next
            temp.next = node
            temp = temp.next
        return head.next
```        


