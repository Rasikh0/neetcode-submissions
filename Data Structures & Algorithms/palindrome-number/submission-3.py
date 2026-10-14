class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False #edge case, returns false immediately when (-)

        #the goal for div is to become the place value of the first digit in x
        #below code snippet will find the place value of the first digit in x
        #below code snippet assumes x is non-negative
        div = 1
        while x >= 10 * div:
            div *= 10
        
        while x: #keep doing this while x is not 0
            if x // div != x % 10: return False
            x = (x % div) // 10 # this line updates x and chops off the left and right digits
            div = div // 100
        
        return True