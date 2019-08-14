#!/usr/local/bin/python3.7
# -*- coding: UTF-8 -*-


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1

        currentMax = 0

        while l != r:
            currentMax = max(min(height[r], height[l]) * (r-l), currentMax)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return currentMax


if __name__ == "__main__":
    ht = Solution()

    v = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    print(ht.maxArea(v))
