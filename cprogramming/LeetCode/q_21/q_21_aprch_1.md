# Leetcode Qeustion 21 , Merge two sorted linked lists.

## Question :
Our tasks is to merge two sorted Linked list , for illustration  <br>
say `` list1 is 1 -> 3 -> 4 -> None `` and `` list is : 1 -> 2 -> 4 -> None `` <br>
then Merged linked list is : `` 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None ``


## Intutions 
We will traverse and compare each linked list and compare the elements of both the  lists,
smaller element wil be added first in the merged_list.



# What would be the approach to solve it .
1. First understand the questions , visualise what to do and what the question is asking.
like in this question , i write both the lists seperatly then created a new merged_list on paper by observing all the
element of the both the lists.
2. Then write a pseudo code , then dry run the code.
for More illustration, 
	- what to do one list 1 is empty and list 2 is not empty
	- what to do on first list is not empty and second list is empty
	- what to do when both the lists are empty or None
	- untill when to merge the  lists
	- what to do if first list beocmes None
	- what to do if second list becomes None
	- exit the looop when both the list becomes None

# My Mistakes while Solving it
1. logic Error : write 'or' instead of 'and' , which causes
list 2 added at the end. , This issue in the implementation code not pseudo code
2. logic Error : wrote '>' instead of '<' which cause the greater elements added at first or simply
arranging element into descending order. <br>
This error is in pseudo code , solved in implementation testing.



# Here is the Sample code to learn and implement 
```pycon
# Merging of 2 sorted Linked List 
class Node :
	def __init__(self,val=0,next=None) :
		self.val = val
		self.next = next
		
# returning a linked list 
def convert_list(nums) :
	head = Node()
	temp = head
	for i in nums :
		temp.next = Node(i)
		temp = temp.next		
	return head.next

# show linked list
def show_list(list1) :
	temp = list1
	while temp != None :
		print(temp.val , " -> ", end="")
		temp = temp.next
	print(None)

# merge linked_list
def merge_list(list1,list2) :
	# when both list1 and list2  is None 
	if ( list1.val == None ) and (list2.val == None ) :
		print("both the lists are None")
		return list1
	# when list 1 is None but list 2 is not None
	elif ( list1.val == None) and ( list2.val != None) :
		return list2
	# when list1 is not None  and list2 is not None
	elif (list1.val != None ) and ( list2.val == None) :
		return list1
		
	#	when both lists are not None
	# Head node which contains merged list
	head = Node()
	# temp variable which merge linked lists.
	temp = head
	
	# Merge the lists untill both the lists not become None or empty or Merged.
	while (  ( list1 != None) or ( list2 != None ) ) :
		
		# when list1 become None 
		if ( ( list1 == None ) and ( list2 != None) ) :
			val = list2.val
			# Move to the next element
			list2 = list2.next
			
		# when list2 becomes None 
		elif ( ( list1 != None ) and ( list2 == None ) ):
			
			val = list1.val
			# Move to the next element
			list1 = list1.next
			
		# if any of the list is not None
		else :			
			# if element of list1 is less than or equal to element 2
			if ( list1.val <= list2.val  ) :
				
				val = list1.val
				list1 = list1.next
			# if element of list 2 is less than list1
			else  :
				val = list2.val
				list2 = list2.next
		
		# Merging or adding values 'val' into the Merged list.
		temp.next = Node(val)
		# shifting pointer to next
		temp = temp.next
		
	# returning merged list
	return head.next
			
# Main program
l1 = [1,3,4]
l2 = [1,2,4]

list1 = convert_list(l1)
list2  = convert_list(l2)

#res =  merge_list(list1.list2)
# printing of linked list
print(" list 1 is : ",end="")
show_list(list1)
print(" list 2 is : ",end="")
show_list(list2)

# Merging lists
result = merge_list(list1,list2)
print(' result is : ' , end = "")
show_list(result)

```



# LeetCode Solution 
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
                val = list1.val
                list1 = list1.next
            elif ( list1 is None) and ( list2 is not None) :
                val = list2.val
                list2 = list2.next
            else :
                if (list1.val <= list2.val) :
                    val = list1.val
                    list1 = list1.next
                else :
                    val = list2.val
                    list2 = list2.next
            temp.next = ListNode(val)
            temp = temp.next
        return head.next
        
```

## ADA : Analysis & Desgn of Algorithm.
1. Time Complexity : O(n) or O(m+n)
2. Space Complexity : O(1)

## Trade-offs
1. We are re using nodes thus previous lists will be empty.
or previous lists actually merged into a single list.
2. we can not undo this process.

