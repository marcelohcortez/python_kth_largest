'''
Use the simplest approach to solve the problem
'''

from typing import List


def find_kth_largest_ele(nums: List[int], k: int) -> int:
    # sort the array
    nums.sort()

    # count down from the righ most part of the array
    # to find the 'kth largest element'
    return nums[len(nums) - k]
