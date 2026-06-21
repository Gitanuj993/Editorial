def lengthOfLongestSubstring(s: str) -> int:
        substring = []
        for i in s :
            if i not in substring :
                substring.append(i)

        len_substring = len(substring)
        print(substring)
        return len_substring
        
result=lengthOfLongestSubstring(input("Enter string : "))          
print("results is :	", result)

# this is not a solution
       
