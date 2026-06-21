# include 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self) :         
        
        temp_org = ListNode(0)
        temp = temp_org
        prev = 0
        while ( ( l1 != None ) or( l2 != None ) or ( prev is not 0 )):
            if l1 == None :
                val1 = 0
            if l2 == None :
                val2 = 0
            if ( l1 == None) or ( l2 ==None) :
                sum = val1 + val2 +prev
            else :
                sum = l1.val + l2.val + prev 
            new_node = ListNode(0)
            if sum >=10 :
                unit = sum % 10
                #carry
                prev = sum // 10
                new_node.val = unit
                #temp = temp.next
                
            else :
                new_node.val = sum
            # if l1 is not None
            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
            temp.next = new_node
            temp = temp.next

        return temp_org.next
            



        
        
        







