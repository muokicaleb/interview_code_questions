"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        size = len(nums)

        if k < size:
            k = k
        else: 
            k = k % size
        nums[k:], nums[:k] = nums[:size-k], nums[size-k:]
