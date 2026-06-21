# LeetCode Question 1840
```txt 
Programmer has to build n new buildings in a row/line labelled from 1 to n,
It is given that height of building is non negative in which the first building's height is always Zero,
constraint is that difference between any adjacent building must not exceeds 1.
additionally some buildings has restriction on their heights , these restrictions are given in the form of 2D array,
in Restriction which has list containing two fields , on 0th index number of the building , 
on 1th position highest possible height of the building is given.

Programmer should found the highest height of building
```

## What the questoin is conveying ?
```txt
1. building n buildings in a row --> we might store them in arrays, ( It will be more costly )
2. Height of any building can't be negative.
3. Height of adjacent buildings can't exceeds 1 ,means
	difference between previous and next building of a building can't be  greater than 1 , 
	It is okay if any adjacent building has same size.
4. We are given a 2D array of Restriciton = [ [building1,height] , [building2,height2]]
5. We have to return highest height of a building.
```




## Approach 1 : Standard
```txt
1. We add first building restriction constraints in the 2D array 'R'.
2. we add the last building if not present in the 2D array 'R'.
3. we sort the 2D array.
4. we check and update Restriction 2D array from left side via
	distance = R[i][0] - R[i-1][0]
	| R[i][1] = min( R[i][1] ,R[i-1][1] + distance |
We are changing height of the buildings with respect to distance
5. Then we do the same from right side , if we move from m-2 to -1 by -1 each step , where m = len(R)
	distance = R[i+1][0] - R[i][0]
	| R[i][1] = min( R[i][1] , R[i+1][1] + distance |
6. We will find the max height of the buidling using a formula
	peak = (height of the current_building + height of the previous + distance between them ) // 2
	We are determining highest peak between consecutive building given in Restriction 'R' Without creating huge array of buildings.
```

## Implementation of the Approach 1
```python
class Solution :
	def maxBuilding(self,n,R) -> int :
		# We will add first building in 'R'
		R.append([1,0])
		# Sorting the Restrictions
		R.sort() # R.sort(key=lambda : x[0])
		# We check whether the last building present in R or not
		if R[-1][0] != n :
			R.append([n,n-1])
		# length of R
		m = len(R)
		# we will check the heights of buildings from left 
		for i in range( 1 , m) :
			R[i][1] = min(R[i][1], R[i-1][1] + R[i][0] - R[i-1][0])
		# Now we will check and update heights of buildings from right side
		for i in range(m-2,-1,-1) :
			R[i][1] = min( R[i][1] , R[i+1][1] + R[i+1][0] - R[i][0] )
		
		# Now we can caluculate the most probable peak height between two  consecutive buildings in R
		ans = 0 
		for i in range(1,m) :
			x1,h1 = R[i-1]			
			x2 , h2  = R[i]
			distance = x2 - x1
			peak = ( h1 + h2 + distance) // 2
			ans = max(ans,peak)
			
		#Return the ans
		return ans
		
		
		
s = Solution()
n = 10
R = [ [5,3] , [2,5] , [7,4] , [10,3] ]
ans  = s.maxBuilding(n,R)
print("max height of building is :	" , ans)

```

### Cost and Trade-offs
1. Time Complexity : 
2. Space Complexity :

### Mistakes i made during the solutions
1. forget that list1.append() is used to add element at the end of the list
```txt
I was using R.add() which gave Errors , and that time i do not have internet access so
i found the correct function using build in ``help(list)`` module
```
2. Adding first and last building in the restroctopn or R
3. Faced difficulty in understanding whether sort is neede.
4. Faced difficulty in passing left checks and right checks.
5. Took time to know why does ``peak`` formula works

### Is Solution prepared by Self without any help
```txt
No, i took help from chatGpt to understand the question properly, and what steps taken 
to solve the problems, i took code form chatGPT and invested a significant time to undestand it
```






