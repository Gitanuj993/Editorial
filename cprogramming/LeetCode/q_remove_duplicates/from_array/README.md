# Remove Duplicate Elements from the array.

Question : A given sorted  array has n number of elements and your task is to return array which doesn't have duplicate_elements.


## Approach_1 : Two pointers

**" traverse the array and compare consecutive elements (say i,j ) if the consecutive elements are different then copy the element at i into a result_array.
and if the element at i and j are same then move pointers by 1.


## Algorithm 
1. set result equal to empty list or empty array.
2. take two pointers i and j , where i pointes to first pointer and 'j' points to next element of 'i'.
3. append the element at 'i' if the element at 'i' and 'j' are not same.
4. move the poiters by 1 index.
5. repeat step 3 and 4 , untill i becomes n-1.
6. return the result array.


```pycon

# main program .
list1 = [1,2,2,3,4,5,5,5,5,6,7]
print(" target list is :	", list1)
result = []
n  = len(list1)
for i in range(n) :		
	if i ==  (n - 1 ) :
		result.append( list1[i])
		break		
	j = i + 1
	if list1[i] != list1[j] :
		result.append( list1[i])
		
print( " result is :	" , result )		

```
> [!note]
> Time Complexity : O(n)
> Space Complexity : O(n)


```pycon
# removing duplicate elements using while loop 
#	program to eliminate duplicate numbers from a sorted list.


# main program .
list1 = [1,2,2,3,4,5,5,5,5,6,7]
print(" target list is :	", list1)
result = []
n  = len(list1)

#for i in range(n) :		
i = 0
while i < n+1 :
	if i ==n-1 :
		result.append(list1[i])
		break
	j = i + 1
	if list1[i] != list1[j] :
		result.append(list1[i])
	i += 1
					
print( " result is :	" , result )		
	
```
### Remove duplicate elements from an array withing a array.
#	program to eliminate duplicate numbers from a sorted list.


# main program .
list1 = [0,1,2,2,3,4,5,5,5,5,6,7]
is_first_element_zero = False
if list1[0] == 0:
	is_first_element_zero = True 
print(" target list is :	", list1)
# lenght of list
n  = len(list1)
# flag all the duplicate elements.
for i in range(n) :
	if i == n-1 :
		break
	j = i+1
	if list1[i] == list1[j] :
		list1[i] = 0
# count totla number of flag elements
total_flaged = list1.count(0)

for i in range(total_flaged) :
	list1.remove(0)
if is_first_element_zero :
	list1.insert(0,0)
print( "result is :	" , list1 )		

```	

2. Another method
```pycon
#	program to eliminate duplicate numbers from a sorted list.


# main program .
list1 = [0,1,2,2,3,4,5,5,5,5,6,7]
print(" target list is :	", list1)
# lenght of list
n  = len(list1)
# flag all the duplicate elements.
for i in range(n) :
	if i == n-1 :
		break
	j = i+1
	if list1[i] == list1[j] :
		list1[i] = "True"
# count totla number of flag elements
total_flaged = list1.count("True")

for i in range(total_flaged) :
	list1.remove("True")

print( "result is :	" , list1 )		
```	


