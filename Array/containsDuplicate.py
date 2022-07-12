from typing import *
# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Runtime: O(n log n) Space: O(1)
# Sorted Solution
def containsDuplicate1(nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

# Runtime: O(1) Space: O(n)
# HashSet Solution
def containsDuplicate2(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
    