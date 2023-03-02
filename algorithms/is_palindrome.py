"""
this method checks if a given string is a valid palindrome
"""

def is_palindrome(string):
    clean = ''.join([i for i in string if i.isalnum()])

    reverse = clean [::-1]

    return clean.lower() == reverse.lower()

    """
    this method is big O time of O(n) where n is the number of characters in the input string
    Its Big O space of O(n) since we create new strings using new memory space for the initial string 
    and the reversed string, which take space comparable to the length of the input string or n 

    https://leetcode.com/problems/valid-palindrome/
    """