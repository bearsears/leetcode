class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return list(map(lambda x: map(lambda y: y ^ 1, x[::-1]), image))