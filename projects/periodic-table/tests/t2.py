# CLI program to take two elements from the modern periodic table and return compound made from them
# oops concepts

# data global scope
data = [ {"name":"H","atomic_no" : 1,"group":1,"valency":+1,"type":"hydride"},
	{"name":"He","atomic_no" : 2,"group":18,"valency":0,"type":"inert"},
	{"name":"Li","atomic_no" : 3,"group":1,"valency":+1,"type":"metal"},
	{"name":"Be","atomic_no" : 4,"group":2,"valency":+2,"type":"metal"},
#	{"name":"B","atomic_no" : 5,"group":13,"valency":,"type":"Hydride"},

	{"name":"B","atomic_no":5,"group":13,"valency":+3,"type":"metalloid"},
{"name":"C","atomic_no":6,"group":14,"valency":4,"type":"non-metal"},
{"name":"N","atomic_no":7,"group":15,"valency":-3,"type":"non-metal"},

{"name":"O","atomic_no":8,"group":16,"valency":-2,"type":"non-metal"},
{"name":"F","atomic_no":9,"group":17,"valency":-1,"type":"non-metal"},
{"name":"Ne","atomic_no":10,"group":18,"valency":0,"type":"inert"},

{"name":"Na","atomic_no":11,"group":1,"valency":+1,"type":"metal"},
{"name":"Mg","atomic_no":12,"group":2,"valency":+2,"type":"metal"},
{"name":"Al","atomic_no":13,"group":13,"valency":+3,"type":"metal"},
{"name":"Si","atomic_no":14,"group":14,"valency":4,"type":"metalloid"},

{"name":"P","atomic_no":15,"group":15,"valency":-3,"type":"non-metal"},
{"name":"S","atomic_no":16,"group":16,"valency":-2,"type":"non-metal"},
{"name":"Cl","atomic_no":17,"group":17,"valency":-1,"type":"non-metal"},
{"name":"Ar","atomic_no":18,"group":18,"valency":0,"type":"inert"},

{"name":"K","atomic_no":19,"group":1,"valency":+1,"type":"metal"},
{"name":"Ca","atomic_no":20,"group":2,"valency":+2,"type":"metal"}]

# data declaration end

#process or main logic
def process(ele1,ele2) : # atomic number of two elements is taken	
 	# process start
 	# realation between index an atomic number is , index_no =  atomic_no -1
 	#	if one element is metal group 1,2 and  another is non metal group  14,15,16,17
	 	## iif element belongs to group 1 ,  
	 	
	 	# Error cases or not reactivity cases 
	 	if ( data[ele1-1] == data[ele2-1]) :
	 		print(" same element do no react !")
	 	# Error same group elements do not react except Hydrozen
	 	#
	 	
	 	# inert gases do not rect 
	 	elif ( (data[ele1-1]["type"] == "inert" ) or (data[ele2-1]["type"] == "inert") ) :
	 		print(" Inert elements do not react !")
	 		
	 	elif ((data[ele1-1]["group"] == 1 ) and  (data[ele2-1]["group"] in  [15,16,17])  ) :
	 		if ( data[ele2-1]["group"] == 17) : # group 17	 				 				 			 
		 		print(f" Compound formed is :	{ data[ele1-1]["name"] + data[ele2-1]["name"] } " ) 
		 	elif ( data[ele2-1]["group"] == 16) :
		 		print(f" Compound formed is :	{ data[ele1-1]["name"]+'2' + data[ele2-1]["name"] } " )
		 	elif ( data[ele2-1]["group"] == 15) :
		 		print(f" Compound formed is :	{ data[ele1-1]["name"]+'2' + data[ele2-1]["name"] + '2' } " ) 
			# working here					
		 		
 	




if __name__ == "__main__" :
	print('Welcome AT')	
	print(len(data)) # length of data
	len_data = len(data)
	# show data 	
	print(" Choose from the following two elements to know which compund will form from this two !")
	for i in range(len_data) :
		print(f"name : {data[i]["name"]} and atomic_no : { data[i]["atomic_no"]} ")
	
		# Taking two element's atomic number	
	element1 = int(input("Enter atomic_no of 1st element : "))
	element2 = int(input("Enter atomic_no of 2nd element  : "))
		
	# 	 function to check for new compound 
	x = process(element1,element2)
	
	







