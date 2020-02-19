#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

#Note: For the purpose of this problem, we define empty string as valid palindrome.

#Example 1:

#Input: "A man, a plan, a canal: Panama"
#Output: true
#Example 2:

#Input: "race a car"
#Output: false

class Solution:

    def isPalindrome(self, s: str) -> bool:

    # good video explanation:
    
    # https://www.youtube.com/watch?v=rYyn9Vc-dBQ
    
    # we can use 2 pointers to solve this problem:
    
        a=int(0)

        b=len(s)-1

        while a < b:

            if s[a].isalnum() is False:

                a=a+1
                
                continue

            if s[b].isalnum() is False:

                b=b-1
                
                continue


            if s[a].lower() != s[b].lower():

                return False
            
            else:
                
                a=a+1
                
                b=b-1

        return True

        
