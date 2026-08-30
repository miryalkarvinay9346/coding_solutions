class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        cont=set()
        notcont=set()
        for i in range(len(nums)):
            if i==len(nums)-1 or nums[i]!=nums[i+1]:
                if nums[i] in notcont:
                    cont.add(nums[i])
                notcont.add(nums[i])
        return len(set(nums)-cont)
                    
            