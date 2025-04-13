# From now on, we are going to use .py files
# .py files are how people actually code in Python
# Jupyter notebooks are intended for beginners or educational purposes.

# Today, we will learn how to take text from the command line and parse it into something a program can 
# work with.

# Follow the tutoral here: https://cs.stanford.edu/people/nick/py/python-input.html

# Task: 
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
# removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric 
# characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

def read_important_text(s: str):
    # Hint: remove all spaces, commas, etc. We only care about letters
    # use a for loop to iterate over all chars in the string.
    # if the char is a letter, add it to a list

    # iterate over the array (have two pointers, one at the front and one at the back)

    # when would the word not be palindrome? (hint: compare left and right entries)

    print(s)

if __name__ == '__main__':
    s = input('Enter your message here: ')
    read_important_text(s)