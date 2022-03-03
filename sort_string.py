#Write a function that takes in an input string, and returns that input string with the words sorted alphabetically. 
#Note: the input string may have capital letters, but the capital letters should not factor into the sorting of the words, and
#even though it should not be factored into the sorting, the word should still be returned capitalized if it was capitalized on
#entry.
#Ex - input: "apple ORANGE banana" should still return "apple banana ORANGE"
import re

def first_letter(current_string):
    letters = [x for x in current_string if x in re.findall(r'[A-z]', current_string)]
    return letters[0].lower()

def sort_string(my_string):
    return ' '.join(sorted(my_string.split(), key = first_letter))

print(sort_string("apple ORANGE banana"))
