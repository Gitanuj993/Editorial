#m zig zag string retur leetcode problem
def zig_zag(s:str,rows:int)-> str :
	if rows ==  1 :
		return s
	# creating a           2d array
	arr = []
	print(" arr :	", arr)
	for i in range(rows):
		arr.append([])		
	print(" arr :	", arr)
	# now putting values into the 2d array
	i = 0	
	isDown = True
	for char in s :
		print(" char s : " , char)
		if  isDown == True :			
			arr[i].append(char)
			i += 1
			if i == rows :
				isDown = False		
				i -= 2
				print(i)
		elif isDown == False :
				 print(" else i : " , i)
				 arr[i].append(char)
				 i -= 1				
				 if i <= 0 :
#				 	arr[i].append(char)
				 	isDown = True				 	
				 	
		#print(" arr :	", arr)
	# creating zig zag
	print(arr)
	res = ""
	for i in arr :
		for j in i :
			res += j
	return res
	#return ''.join(''.join(row) for row in arr)
				
	
test = "ABCDEF"	
print("test is : ", test)
rows = 2
res = zig_zag(test,rows)
print("result is : ",res)
	
	
