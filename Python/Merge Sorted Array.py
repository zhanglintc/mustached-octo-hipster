# Merge Sorted Array
# for leetcode problems
# 2014.09.14 by zhanglin

# Problem Link:
# https://leetcode.com/problems/merge-sorted-array/

# Problem:
# Given two sorted integer arrays A and B, merge B into A as one sorted array.

# Note:
# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B.
# The number of elements initialized in A and B are m and n respectively.

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        while m != 0 and n != 0: # while A and B not NULL
            if A[m - 1] >= B[n - 1]: # if A >= B, put A to the end
                A[m + n - 1] = A[m - 1]
                m -= 1
            else: # else if A < B, put B to the end
                A[m + n - 1] = B[n - 1]
                n -= 1

        while m != 0: # if A remains items
            A[m + n - 1] = A[m - 1]
            m -= 1

        while n != 0: # if B remains items
            A[m + n - 1] = B[n - 1]
            n -= 1



