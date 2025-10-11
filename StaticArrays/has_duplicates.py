from typing import List

def remove_duplicates(nums: List[int]) -> bool:
    newSet = set(nums)
    if len(nums) != len(newSet):
        return True
    return False
