#Write a function that returns a boolean value, representing whether or not a given input string is a palindrome. The function
#should only consider characters from A-Z, regardless of case, meaning that spaces and special characters should not mean that
#a string is not a palindrome

def is_palindrome(my_string):
    filtered_alphas = filter(str.isalpha, my_string)

    my_string = "".join(filtered_alphas).lower()

    left = 0
    right = len(my_string) - 1
    chars_match = True

    while left <= right:
        if my_string[left] != my_string[right]:
            chars_match = False
        left += 1
        right -= 1

    return chars_match

print(is_palindrome("Go hang a salami - I'm a lasagna hog."))

#Solution two
import re

def is_palindrome_two(my_string):
    joined_string = ''.join(re.findall(r'[a-z]+', my_string.lower()))
    reversed_string = joined_string[::-1]
    return joined_string == reversed_string

print(is_palindrome_two("Go hang a salami - I'm a lasagna hog."))