# LeetCode problem 9 : Palindrome number 
<h3> Question link : https://leetcode.com/problems/palindrome-number/description/ </h3>

## Intution :
<h3> Palindrome number is a number which can be read and write same as if it is written backward </h3>

<h3> Our Task is to check whether a number is palindrome or not , if number is palindrome then return True else False <br>
Some Illustrations : <br>
1. if number is : 123  <br>
	return  False
2. if number is : 121
	return True
3. if number is : -121
	return False 
	// as Technically reverse of -121 would be 121- , which are unequl thus return False
4. if number is : greater than 32 bit integer 
	return False

</h3>
## Best practices to solve the problem
<h3> 
1. if number is negative , return false
2. if number is of 1 digit , return true
3. if number ends with 0 then return false
4. if integer overflow occure , return false


## List of Approaches to solve the Problem
1. First reverse the whole number then check original number and reversed number
2. Divide the number in first half and second half , reverse second half , and check first half and reversed half.
	- if original number is odd , remove last digit of reversed half then check with first half
	- if original number is even then no need to remove last digit from the reversed_half



### Approach 1: Reverse Whole number

```
Our task is to check wheather a number is palindrome number or not , without converting nums string and string slicing.
To do the job we ,first eliminate some edge cases given in the "Best practices to solve the problem "

lets  store the reversed number into a varible say reversed_num , initialized with '0'
lests copy the original number to perform mathematical operations , say temp = original_num

we can perform the operation on temp untill no further operation can be performed,
we extract last digit one by one from the temp , and put into reversed_num.
to actually reverse number we shift the previous digit to left side .
after adding extracted digit into the reversed_num we will continue extracting last digits.
to extract another last digit we have to remove previous last digit.
we would remove previous last digit and continue the process until the temp varible become empty.

```

<h3>
Procedure or algorithm 
</h3>
1. set reversed_num = 0
2. copy original_num to variable temp
3. while temp not become '0' 
	- extract digit from the temp , using remainder , temp % 10
	- shift the extracted digit into reversed_num , reveresd_num = reversed_num * 10 + digit
	- remove last digit of temp
4. do the step 3 until temp become '0'
5. compare original number and reversed_num , return result
6. stop 

# Time complexity , Space Complexity and clean code Optimization.
```
Time complexity of above approach is : O(logn) of base 10.
space complexity of above approach is : O(1)

We can optimize code by using properties of palindromes , 

```


## Approach 2 : comparing first half of number and second reversed half

```
In this approach we can simply halve the number , say first_half and second reversed_half
then we compare both the halfs while keeping in mind about odd and even numbers.
as in odd number case reversed_half has one digit greater than the first half thus we will do 
comparison after removing last digit of reversed_half.

```

<h3> Procedure  </h3>
1. We would do good  practices first to reduce unnecessary operations.
2. set temp = original number
3. set reversed_half  = 0
4. we will continously do the operation on temp  untill it revered_num > temp
	- extract digit using int digit = temp % 10 
	- check range of reversed_num to tackle integer overflow if needed , like in c,c++, java etc.
	- To check range we ensure reversed_num < ( INT_MAX ( 32 bit highest integer ) - digit ), and divide by 10
	- if reversed_num exceeds range then return false , in case of languages like C , C++  , java etc.
	- we add the extracted digit into the reversed_num and shift previous digits to left side
	- remove last digit of temp 
	- continue the process

5. compare temp and reversed_half , 
	- if original number is odd then remove last digit of reversed_half using reversed // 10
6.Stop , return the result.
