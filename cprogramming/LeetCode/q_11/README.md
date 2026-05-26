# LeetCode Q_11 : Container with the most water .

Question : There is  given an array which contains heights of the pipes ( say lines ), and the index acts as the width from the initial position.
Your tasks is to find out a area between two lines which contains most water or simply max area.

## My approaches 
1. i tried all the possible combinations made from all the lines. which gives correct answer but
whose time complexity is O(n^2), 

2. i tried by taking two lines , one from first and second one from the end. in short "Two pointers"
one pointer moves from left to right and another pointer moves from right to left. 
in this process we compute the area and compare it with the max_area.


## Approach_1 : Brute Force 
**" In this approach we will take  every pipe/line and calculate the area and then compare it with previous max_area , 
and if the area is greater than Max_area then store the value of area in math_area.
"** <br> <br>
### Algorithm
1. set a max_area equal to 0
2. take one pipe from the array and compare it with other pipes.
3. calculate the area and and compare it with the previous max_area.
4. repeat step 2, untill all the pipes are compared.
5. return the max_area

```python
# program to calculate max
class Solution :
	def max_water(self,list1) :
		max_ = 0 
		n = len(list1)
		print(" LENGTH  is : " , n)
		for i in range (n) :
			for j in range ( i + 1 , n ) :
				area = ( j - i ) * min (list1[i], list1[j] )
				max_ = max ( max_ , area )
		# return the maximum area.
		return max_
s = Solution()
test = [ 1,8,6,2,5,4,8,3,7,10,11]
res = s.max_water(test)
print(" max capacity is :	" , res )		

```		
> [!note]
> Time Complexity : O(n^2)
> Space Complexity : O(1)
> Leetcode :  rejected , Time bound error 


### Qans
1. Why Time complexity is O(n^2) ?
ans : Time Complexity is O( n^2) because we are taking one element from the array and compare it with the
rest elements , then take another element from the array and compare it with the rest of the elemenst.

traversing array for taking one element at a time , which gives O(n) and then using this element to compare rest elements
of the array which including traversing the array again which gives O(n^2).
We are traversing the array two times concurrenlty. thus overalll timecomplexity becomes O(n^2).


2. Why Space Complexity is O(1) ?
ans : Space complexity is O(1) becouse number of variables used to store results and for flags/signals are constants.
which do not grow with number of inputs ( say number of elements present in the array ).


## Approach_2 : Linear
**" We will take two pointers , one from the start and another from the end .
from this two pointers we will calculate the area and compare it with the max_area , and move the smaller pointer.
"**

### Algorithm

1. set max_area equal to 0
2. take two pointers one from start and another from end.
3. calculate area and compare it with the max_area , if the area > max_area , put values of area into max_area.
4. if the left pointer > right pointer then move the left pointer to right side or else move right pointer to left side.
5. repeat steps 3 and 4 untill left pointer >= right pointer.
6. return the max_area.

```python
# program to calculate max
class Solution :
	def max_water(self,list1) :
		max_ = 0 
		n = len(list1)
		print(" LENGTH  is : " , n)
		left , right = 0 , n-1
		while left < right :
				area = ( right - left) * min( list1[left],list1[right])
				max_ = max(max_ , area)
				if list1[left] < list1[right] :
					left +=1
				else :
					right -= 1
				
		return max_
s = Solution()
test = [ 1,8,6,2,5,4,8,3,7,10,11]
res = s.max_water(test)
print(" max capacity is :	" , res )		

```		
> [!note]
> Time Complexity : O(n) 
> Space Complexity : O(1)
> Leetcode : Accept 


### Qans 
1. Why time complexity is O(n) 
ans : Time complexity is O(n) becouse we are checking and moving pointers linearly as
we are moving pointers in either left side or in right side. 
pointers movement depends on size of the array.




