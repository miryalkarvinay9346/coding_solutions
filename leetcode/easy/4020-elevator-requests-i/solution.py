class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        m=requests[0]
        for i in range(1,len(requests)):
            m+=abs(requests[i]-requests[i-1])
        return m