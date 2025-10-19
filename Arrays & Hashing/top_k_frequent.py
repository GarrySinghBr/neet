'''
Neetcode: Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

ex)
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Input: nums = [7,7], k = 1
Output: [7]
'''
from typing import List


def solution(nums: List[int], k: int) -> List[int]:

    # build frequency dictionary
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] +=1
        else:
            freq[i] = 1

    # build buckets/blocks for each frequency
    buckets = [[] for _ in range(0,len(nums)+1)]

    for element in freq:
        buckets[freq[element]].append(element)

    solution = []
    for i in range(len(buckets)-1, 0, -1):
        for j in buckets[i]:
            solution.append(j)
            if len(solution) == k:
                return solution
