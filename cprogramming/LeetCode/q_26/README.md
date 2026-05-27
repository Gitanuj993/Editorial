# LeetCode Question_26 : Remove duplicates from a sorted array in place.

" In this question, an sorted array is given in which duplicate elements are present ,
our task is to remove the duplicate elements from the list and return the length of sorted array.
<br>
For more illustaration ! <br>
If the array is : [ 1,2,2,2,3,4,5 ] <br>
then array would become : [ 1, 2, 3, 4, 5 , _ , _ ] <br>
thus return lenght of sorted array : 5 ; '_' referes to absence of value.

## Approaches !
1. 
2.
3.




### Approach_1 : 

```pycon
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #result = []
        n = len(nums)
        count_duplicates = 0
        for i in range(len(nums)) :
            if i == n-1 :                
                break
            j = i + 1
            if nums[i] == nums[j] :
                nums[i] = "True"
                count_duplicates += 1

        for i in range(count_duplicates) :
            nums.remove("True")

            
        return n - count_duplicates
```
## Approach_2 

```pycon
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #result = []
        n = len(nums)
        
        i = 0 
        max_len = n
        while i < max_len :
            if i >= max_len-1 :
                break
            else :
                j = i + 1            
            if nums[i] == nums[j] :
                nums.remove(nums[i])
                if i<=0 :
                    0
                else :
                    i -= 1
                max_len -=1
            else :
                i += 1
        
            
        return max_len
```
# Approach_3

```pycon
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #result = []
        n = len(nums)
        
        i = 0 
        max_len = n
        while i < max_len :
            if i >= max_len-1 :
                break
            j = i + 1
            while  (j < max_len) and (nums[i] == nums[j] )  :
                nums.pop(j)
                max_len -= 1
            i += 1
            
            
            
        return max_len
```
