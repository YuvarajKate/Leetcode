class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for elem in nums1:
            i = nums2.index(elem)
            for j in range(i,len(nums2)):
                if nums2[j]>elem:
                    output.append(nums2[j])
                    break
            else:
                output.append(-1)
        return output