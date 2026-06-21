class Solution {
public:
    bool isPalindrome(int x) {
        // if integer is negative
        if ( x < 0 ) {
            return false ; }
        // if length of number is 1
        if (x < 10)  {
            return true; }
        // return false if end digit of any number is 0, unless number itself is zero
        if ( ( x % 10 == 0 ) && ( x != 0 ) ) {
            return false ;}
        // integer 32 bit
        if ( x > INT_MAX ) {
            return false ;
        }
     //   int INT_MAX = 2**31 - 1 ; // already defined in the library
        // reverse number variable
        int reversed_num = 0 ;
        // temp variable of x for Mathematical operation
        int temp = x ;
        // while temmp not equal to 0 , do following operations
        while ( temp != 0 ) {
            
            // extrating digit 
            int digit = temp % 10;
            // integer overfow edge case
            if ( reversed_num > ( INT_MAX - digit ) / 10  ){
                return false ;
            }
            // puting digit into reversed number
            reversed_num = reversed_num * 10 + digit ; // multiple rev by 10 and add extracted digit
            // operation done now remove extracted digit
            temp /= 10 ;
            }

        // lets compare original number and reversed number
        return ( reversed_num == x ) ;
    
        
    }
};
