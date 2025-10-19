'''
Neetcode: Two Sum
Given a list of numbers and target k, return indices i,j such that
nums[i] + nums[j] == target and i != j. (Assume exactly 1 soln)
'''
from typing import List

def solution(nums : List, target : int) -> List:
    map = {}
    sol = []
    for i,v in enumerate(nums):
        complement = target - v
        if complement in map:
            sol.append(map[complement])
            sol.append(i)
        else:
            map[v] = i