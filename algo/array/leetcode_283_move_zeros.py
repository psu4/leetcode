class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    #https: // www.youtube.com / watch?v = VSeVT - oKZE4
    #  [0,1,0,3,12]

    #         pos | i  | nums[i]

    #         0   | 0  | 0

    #         1.    1    1

        pos = 0

        for i in range(len(nums)):  # if the numbers are not 0, put them to the front with the same order

            if nums[i] != 0:
                nums[pos] = nums[i]

                pos += 1

        for i in range(pos, len(nums)):
            nums[i] = 0

        return nums