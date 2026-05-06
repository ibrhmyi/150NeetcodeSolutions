class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: #DIDNT WORK, went for O(logn)
        l, r = 0, len(nums1) - 1
        mergepoint = 0

        while l <= r:
            m = (l + r) // 2
            if nums1[m] <= nums2[0]:
                l = m + 1
            else:
                r = m - 1
                mergepoint = m

        right = mergepoint + 1
        tomiddle = len(nums1) + right
        half = (len(nums1) + len(nums2)) // 2

        if half < right:
            if (len(nums1) + len(nums2)) % 2 == 1:
                return nums1[half]
            else:
                return (nums1[half] + nums1[half - 1]) / 2

        elif half < tomiddle:
            midindex = tomiddle - half

            if midindex > len(nums2):
                midindex = len(nums2)

            if midindex == 0:
                return nums2[0]

            if (len(nums1) + len(nums2)) % 2 == 1:
                return nums2[-midindex]
            else:
                idx1 = -midindex - 1
                idx2 = -midindex
                if abs(idx1) > len(nums2):
                    idx1 = -len(nums2)
                if abs(idx2) > len(nums2):
                    idx2 = -len(nums2) + 1

                return (nums2[idx1] + nums2[idx2]) / 2

        else:
            leftindex = half - len(nums2)
            if (len(nums1) + len(nums2)) % 2 == 1:
                return nums1[leftindex]
            else:
                return (nums1[leftindex] + nums1[leftindex]) / 2
