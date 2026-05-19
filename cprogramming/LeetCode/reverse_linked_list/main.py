# creating a linked list . 

class Node :
	def __init__(self,value=0,next = None) :
		self.value = value
		self.next = next
		
dummy = Node()
temp = dummy		
values = [ 1 ,2 ,3, 4,5,6]
for value in values	:
	temp.next = Node(value)
	temp = temp.next
	
head = dummy	
print("          node : "  , head.next.value)
temp = head.next
while         ( temp is not None) :
	print( temp.value, " - > " , end="")
	temp  = temp.next
print("None")

	
# reversing a linked list
temp = head.next
previous_node = None
while ( temp is not None) :
	next_node = temp.next
	temp.next = previous_node
	previous_node = temp
	temp = next_node
# linked List achieved
temp = previous_node
while  ( temp is not None) :
	print( temp.value, " - > " , end="")
	temp  = temp.next
print("None")

