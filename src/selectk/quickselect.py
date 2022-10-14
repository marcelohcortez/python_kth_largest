'''
Use the 'quickselect' approach with recursion that
has a better average time complexity than the simplest approach
'''

from typing import List


def find_kth_largest_ele(nums: List[int], k: int) -> int:

    k = len(nums) - k

    def quickselect(left_most, right_most):
        # we use the 'pivot' to have a reference
        # and we opt for using the last number in the array.
        # We use 'p' to pin the last index used
        pivot, p = nums[right_most], left_most

        # look all the array except for the last item
        for i in range(left_most, right_most):

            # if that value is lower or equal to the pivot,
            # swap the values to sort the array and keep track of the 'pin'
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1

        # when the for ends, swap the values
        nums[p], nums[right_most] = nums[right_most], nums[p]

        if p > k:
            # search in the left part of the array, run the function again
            return quickselect(left_most, p - 1)
        elif p < k:
            # search in the right part of the array, run the function again
            return quickselect(p + 1, right_most)
        else:
            # found the answer, return
            return nums[p]

    return quickselect(0, len(nums) - 1)
