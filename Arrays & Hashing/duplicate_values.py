'''
# Leetcode 217. Contains Duplicate
# Given integer array nums, return T if any values appears atleast twice
# Return F if every element is distinct
'''
def solution(nums: list) -> bool:
    a = set(nums)
    if len(a) != len(nums):
        return True
    else:
        return False
