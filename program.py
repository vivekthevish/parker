# coding=utf-8
"""
Write a program that decides the winner among 2 players with the following rules
Each player will present a string which needs to be compared
Each string would be at least 1 char long  
The first string wins if it contains more z’s than the second string. If they have the same number  of z’s, then the string
with the most y’s wins. If they have the same number of y’s, then the number of x’s determines the winner, etc.  
If they contain the same number of z’s, y’s .... a’s, then it’s a tie and there is no winner.  
If either string contains the character sequence “no”, it is a tie.  
If either string contains a number or symbol, then it’s a tie.
Each round contains two strings on a line, separated by a space.
Examples
In this example, the second string wins: abcdefg hijklmn
In this example, the first string wins: zaay zaac
In this example, there is no winner: post post
In this example, there is no winner: adflkj# fawefkj
In this example, there is no winner: awefnoafwe fakwjefzzzz
Please ensure that your program is modular in nature and has sufficient number of unit tests.
"""

from collections import Counter
from string import ascii_lowercase


str1 = raw_input("Enter string by Player1: ")
str2 = raw_input("Enter string by Player2: ")
if str1.isalnum() and str2.isalnum():
    count1, count2 = Counter(str1), Counter(str2)
    print max(count1, count2)
elif str1 == str2:
    print "No Winner"


