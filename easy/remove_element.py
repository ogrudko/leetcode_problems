class Solution:
    def removeElement(self, nums, val):
        iterator = 0
        while iterator < len(nums):
            if nums[iterator] == val:
                nums.pop(iterator)
                iterator -= 1
            iterator += 1
        print(nums)



solution = Solution()
solution.removeElement([3,2,2,3], 3)