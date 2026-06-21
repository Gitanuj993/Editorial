class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if integer is negative
        if x < 0 :
            return False
        # if length og number is 1
        if (x < 10)  :
            return True
        # return false if end digit of any number is 0, unless number itself is zero
        if ( x % 10 == 0 ) and x != 0 :
            return False
        # lets check pallindrome number
        # reverse number variable
        reversed_num = 0
        # temp variable of x for Mathematical operation
        temp = x
        # while temmp not equal to 0 , do following operations
        while temp != 0 :
            # extrating digit 
            digit = temp % 10
            # puting digit into reversed number
            reversed_num = reversed_num * 10 + digit # multiple rev by 10 and add extracted digit
            # operation done now remove extracted digit
            temp //= 10

        # lets compare original number and reversed number
        return reversed_num == x 
        
if __name__ == '__main__' :
	s = Solution()
	x = int(input("Enter integer : " ))
	print(s.isPalindrome(x))
