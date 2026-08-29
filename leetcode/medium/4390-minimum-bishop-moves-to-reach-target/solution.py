class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        if source[0]==target[0] and source[1]==target[1]:
            return 0
        if abs(source[0]-target[0])==abs(source[1]-target[1]):
            return 1
        if (sum(source)%2)!=(sum(target)%2):
            return -1
        return 2
            