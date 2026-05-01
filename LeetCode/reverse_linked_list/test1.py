# reversing a linked list or 

class Node :
	
	def __init__(self,value = 0 , next = None) :
		self.value = value
		self.next  = next
		
		

# feature reversing a linked list 	
if __name__ == '__main__' :
	
#	while True :
#		 create a linked list
	values = [  1,2,3,4,5,6,7,8,9,10 ,11 ]
	head = Node(len(values))
	temp	= head
	#	creating linked list from the above values
	for val in values :
		new_node = Node(val)
		temp.next = new_node
		temp = temp.next
		
		
	# printiting of values 
	temp = head.next
	while( temp is  not None ):
		print( temp.value, " ->  " , end="")
		temp = temp.next
	print("None")
			
	# reversing a linked list
	temp = head.next
	previous_node = None

	while temp is not None :		  
		  current_node = temp		  
		  next_node = current_node.next
		  current_node.next = previous_node		  
		  previous_node = current_node
		  temp = next_node
reversed_linked_list = previous_node
temp = reversed_linked_list
while  ( temp is not None) :
	print( temp.value, " - > " , end="")
	temp  = temp.next
print("None")
		  








