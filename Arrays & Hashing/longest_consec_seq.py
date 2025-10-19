'''
Neetcode:Longest Consecutive Sequence

Given an array of integers nums, return the length of the longest consecutive
sequence of elements that can be formed.A consecutive sequence is a sequence 
of elements in which each element is exactly 1 greater than the previous element.
The elements do not have to be consecutive in the original array. You
must write an algorithm that runs in O(n) time.

Input: nums = [2,20,4,10,3,4,5]
Output: 4

'''
from typing import List

def solution(nums: List) -> int:
    numsSet = set(nums)
    maxCount = 0
    for i in nums:
        if (i-1) not in numsSet:
            localMax = 1
            j = i
            while True: # this loop can be improved with while j+1 in numsSet
                if (j+1) in numsSet:
                    localMax += 1
                    j +=1
                else:
                    if localMax > maxCount:
                        maxCount = localMax
                    break
    return maxCount
