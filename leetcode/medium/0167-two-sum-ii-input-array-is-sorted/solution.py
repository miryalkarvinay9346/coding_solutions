class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a=[0,0]
        for i in range(len(numbers)):
            a[0]=i+1
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    a[1]=j+1
                    return a