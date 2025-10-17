'''
Leetcode 268. Missing Number
Given an array nums containing n distinct numbers in the range [0,n],
return the only number in the range that is missing from teh array.
'''

def solution(nums: list) -> int:
    actual = sum(nums)

    expected = 0
    for i in range(0,len(nums)+1):
        expected += i
    
    return(expected - actual)

print(solution([0,1,3]))