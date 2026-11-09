class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final = []
        a = b = 0

        while a < len(nums1) and b < len(nums2):
            if nums1[a] <= nums2[b]:
                final.append(nums1[a])
                a += 1
            else:
                final.append(nums2[b])
                b += 1
        
        final.extend(nums1[a:])
        final.extend(nums2[b:])

        if len(final) % 2 != 0:
            mid = (0 + len(final)) // 2
            return final[mid]
        
        mid = (0 + len(final)) // 2
        return (final[mid] + final[mid - 1]) / 2