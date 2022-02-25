import sys, os
sys.path.append(os.path.join("..", "Solutions"))
sys.path.append(os.path.join("Solutions"))


from PalindromeNumber import Solution

solution = Solution()

def test_palindrome_number_1():
    assert solution.isPalindrome(121) == True
    
def test_palindrome_number_2():
    assert solution.isPalindrome(1234) == False