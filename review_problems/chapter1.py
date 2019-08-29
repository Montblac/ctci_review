# Chapter 1: Arrays and Strings
# Pages 90 - 91, and additional questions

# 1.1 Is Unique
#   Implement an algorithm to determine if a string has all unique characters.
#   What if you cannot use additional data structures?
def isUnique(x: str) -> bool:
    if len(x) > 128:
        return False
    char_table = {}
    for char in x:
        if char not in char_table:
            char_table[char] = 1
        else:
            return False
    return True


assert isUnique('cat')
assert isUnique('word@#')
assert not isUnique('apple')
assert not isUnique('cat  ')
assert not isUnique('$watermelon')


# 1.2 Check Permutation
#   Given two strings, write a method to decide if one is a permutation of the other.
def checkPermutation(s1: str, s2: str) -> bool:
    return False if len(s1) != len(s2) else sorted(s1) == sorted(s2)


assert checkPermutation('dog', 'god')
assert checkPermutation('@$%&^', '$&%^@')
assert checkPermutation('crackingthecode', 'kigthecodecracn')
assert not checkPermutation('wumpus', 'swompu')
assert not checkPermutation('alphabet', 'alphabe')
assert not checkPermutation('word', 'word ')


# 1.3 URLify
#   Write a method to replace all spaces in a string with '%20'. You may assume that
#   the string has sufficient space at the end to hold the additional characters, and
#   that you are given the 'true' length of the string.
def urlify(x: str, n: int) -> str:
    return x.replace(' ', '%20')


assert urlify('banana ', 9) == 'banana%20'
assert urlify(' pine apple ', 12) == '%20pine%20apple%20'
assert urlify('apple', 5) == 'apple'
assert urlify(' grapes', 9) != ' grapes'
assert urlify(' ', 3) != ' '


# 1.4 Palindrome Permutation
#   Given a string, write a function to check if it is a permutation of a palindrome.
#   A palindrome is a word or phrase that is the same forwards and backwards. A
#   permutation is a rearrangement of letters. The palindrome does not need to be limited
#   to just dictionary words.
def palinPermutation(x: str) -> bool:
    char_table = {}
    for c in x:
        if c not in char_table:
            char_table[c] = 1
        else:
            char_table[c] += 1
    count = 0
    for val in char_table.values():
        if val % 2 != 0:
            count += 1
    return count <= 1


assert palinPermutation('racecar')
assert palinPermutation('raadr')
assert palinPermutation('snppssnaas')
assert not palinPermutation('tiger')
assert not palinPermutation('racecar ')
assert not palinPermutation('tomatomx')


# 1.5 One Away
#   There are three types of edits that can be performed on strings: insert a character,
#   remove a character, or replace a character. Given two strings, write a function to
#   check if they are one edit (or zero edits) away.
def oneAway(s1: str, s2: str) -> bool:
    pass


# 1.6 String Compression
#   Implement a method to perform basic string compression using the counts of repeated
#   characters. For example, the string aabccccaaaa would become a2b1c5a3. If the
#   'compressed' string would not become smaller than the original string, your method
#   should return the original string. You can assume the string has only uppercase
#   and lowercase letters (a-z).
def strCompression(x: str) -> str:
    pass


# 1.7 Rotate Matrix
#   Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
#   write a method to rotate the image by 90 degrees. Can you do this in place?
def rotateMatrix(x: list) -> list:
    pass


# 1.8 Zero Matrix
#   Write an algorithm such that if an element in MxN matrix is 0, its entire row and column
#   are set to 0.
def zeroMatrix(x: list) -> list:
    pass


# 1.9 String Rotation
# Assume you have a method isSubstring which checks if one word is a substring of another.
#   Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only
#   one call to isSubstring (e.g., 'waterbottle' is a rotation of 'erbottlewat').
def strRotation(s1: str, s2: str) -> bool:
    pass