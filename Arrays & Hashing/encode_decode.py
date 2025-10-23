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

START_OF_STRING = "#"

def encode(strs: List[str]) -> str:
    translation = []
    for str in strs:
        translation.append(START_OF_STRING)
        for c in str:
            translation.append(c)
    return "".join(translation)

# problem: delimiter only approach is messy, and will break on empty strings! RETHINK ENCODER!

#we#say#:#yes
def decode(s: str) -> List[str]:
    original = []
    word = []
    for i in s:
        if i != START_OF_STRING:
            word.append(i)
        else:
            original.append("".join(word))
            word.clear()
    return original


encoded = encode(["neet","code","love","you"])
print(encoded)
decoded = decode(encoded)
print(decoded)
