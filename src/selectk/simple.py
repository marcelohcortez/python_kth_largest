'''
Use the simplest approach to solve the problem
'''

from typing import List

def find_kth_largest_ele(nums: List[int], k: int ) -> int:
    nums.sort() #sort the array
    return nums[len(nums) - k] #count down from the righ most part of the array to find the 'kth largest element'
