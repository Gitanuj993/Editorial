class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binary_search(low,high) :
            # base case
            if low >  high :
                return -1
            mid = ( low + high ) // 2
            # if target found
            if nums[mid] == target :
                return mid                        
            # recursive calls
            #	if target is greater than mid
            if nums[mid] < target : 
                low = mid + 1
                return binary_search( low , high)
            else :
                high = mid - 1
                return binary_search(low,high)
        result = binary_search(0,len(nums)-1)
        return result
                
s = Solution()
nums = [ -1,0,3,5,9,12]            
target = 9
res= s.search(nums,target)
print("result is :	", res)
