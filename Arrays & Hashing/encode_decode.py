'''
Encode and Decode Strings
Design an algorithm to encode a list of strings to a single string. The encoded string 
is then decoded back to the original list of strings. Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]
'''
from typing import List

DELIMITER = "#"

def encode(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    scrambled = []
    for word in strs:
        length = len(word)
        scrambled.append(str(length))
        scrambled.append(DELIMITER)
        for char in word:
            scrambled.append(char)
    return "".join(scrambled)

def decode(s: str) -> List[str]:
    solution = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != DELIMITER:
            j = j +1
        length = int(s[i:j])
        word = s[j+1: j+length+1]
        solution.append(word)
        i = j + length + 1
    return solution
