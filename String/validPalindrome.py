# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
def isPalindrome(s:str) -> bool:
    validS = ""
    for c in s:
        if c.isalnum():
            validS += c.lower()
    i,j = 0, len(validS)
    while i <= j:
        if validS[i] != validS[j]:
            return False
        i += 1 
        j -= 1
    return True