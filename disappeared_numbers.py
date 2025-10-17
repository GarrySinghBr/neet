'''
# Leetcode 448. Find All Numbers Disappeared in Array
Given an array nums of n integers where nums[i] is in the range [1,n],
return an array of all the integers in the range [1,n] that do not appear in nums
'''

def solution(nums: list) -> list:
    # convert to set to avoid duplicates
    # loop through the range of len(nums) + 1
    # check if set contains, if it doesnt, we add the index
    setA = set(nums) # O(n)

    missing = []
    for i in range(1, len(nums)+1): # O(n)
        if i not in setA:
            missing.append(i)
    return missing