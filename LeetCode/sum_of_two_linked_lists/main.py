# adding two linked list

class Node :
	def __init__(self,val = 0 , next = None) :
		self.val = val
		self.next = next
		

linked_list_1_values = [ 7,8,9]
linked_list_2_values = [ 4,3,2]
linked_list_1 = Node()
linked_list_2 = Node()

#	adding values in linked_list 1
temp = temp = linked_list_1
for val in linked_list_1_values :
	temp.next = Node(val)
	temp = temp.next
temp = linked_list_1.next	

#	adding values in linked list 2
temp = linked_list_2
for val in linked_list_2_values :
	temp.next = Node(val)
	temp = temp.next
# printing values in linked_list 1	
temp = linked_list_1.next
while ( temp is not None ) :
		print(temp.val,"->",end = "")
		temp = temp.next
print("None")
		
# printing values in linked_list 2	
temp = linked_list_2.next
while ( temp is not None ) :
		print(temp.val,"->",end = "")
		temp = temp.next
print("None")
	

#	addition of two linked list 
sum = Node()
t1 = linked_list_1.next
t2 = linked_list_2.next
s = sum
carry = 0
print( " addition of two linked list")
while ( t1 != None  ) or ( t2 != None) or ( carry != 0) :	
	val1 = t1.val if t1 is not None else 0
	val2 = t2.val if t2 is not None else 0
	total = val1 + val2 + carry
	if total > 9 :
		digit = total % 10
		carry = total // 10	
	else :
		digit = total
		carry = 0
	s.next = Node(digit) 
	s = s.next		
	if t1 : t1 = t1.next
	if t2 : t2 =  t2.next

		
print( " addition of two linked list is ")
temp = sum
while temp is not None :
	print(temp.val , "-> " , end = "")
	temp = temp.next
print("None")
	
					

