class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:
            row.reverse()#flipping  horizontally
            for i in range(len(row)):
                row[i]=1-row[i]# inverting result
        return image