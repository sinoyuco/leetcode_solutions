class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m] = nums2[i]
            temp = m - 1
            while temp >= 0 and nums2[i] < nums1[temp]:
                nums1[temp], nums1[temp+1] = nums1[temp+1], nums1[temp]
                temp -= 1
            m += 1
        return nums1
