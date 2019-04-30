"""
设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

示例:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
说明:
你可以假设 nums 的长度≥ k-1 且k ≥ 1。

input : ["KthLargest","add","add","add","add","add"] [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
output: [null,4,5,5,8,8]

"""
import heapq
from typing import List


class KthLargest:

    # def __init__(self, k: int, nums: List[int]):
    #     self.k = k
    #     self.nums = []
    #     for num in nums:
    #         self.add(num)
    #
    # def add(self, val: int) -> int:
    #     if len(self.nums) < self.k:
    #         self.nums.append(val)
    #         self.heappush()
    #         if len(self.nums) < self.k:
    #             return None
    #     else:
    #         if val > self.nums[0]:
    #             self.nums[0] = val
    #             self.heapreplace()
    #     return self.nums[0]
    #
    # def heappush(self):
    #     if len(self.nums) > 1:
    #         i = len(self.nums) - 1  # the last node
    #         father = int((i - 1) / 2)
    #         while i > 0 and self.nums[i] < self.nums[father]:
    #             self.nums[i], self.nums[father] = self.nums[father], self.nums[i]
    #             i = father
    #             father = int((i - 1) / 2)
    #
    # def heapreplace(self):
    #     if self.k > 1:
    #         i = 0
    #         while i <= int((self.k - 2) / 2):
    #             left = 2 * i + 1
    #             right = min(2 * i + 2, self.k - 1)
    #             smaller = left if self.nums[left] <= self.nums[right] else right
    #             if self.nums[i] > self.nums[smaller]:
    #                 self.nums[i], self.nums[smaller] = self.nums[smaller], self.nums[i]
    #                 i = smaller
    #             else:
    #                 break

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        # heapq模块实现了一个适用于Python列表的最小堆排序算法。
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]
