class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ret = 0
        cur = 0
        # cur dict will keep track of freqs of elements currently
        #   in subarray
        cur_dict = {}
        left = 0
        # each subarray has a rightmost element
        for right in range(len(nums)):
            # assume element is in subaray
            if nums[right] in cur_dict:
                cur_dict[nums[right]] += 1
            else:
                cur_dict[nums[right]] = 1
            # if adding this element causes feq > k, move left of
            #   subarray until we have lost 1 copy of the element
            if cur_dict[nums[right]] > k:
                while nums[left] != nums[right]:
                    cur_dict[nums[left]] -= 1
                    left += 1
                    cur -= 1
                cur_dict[nums[right]] -= 1
                left += 1
            else:
                cur += 1
                if cur > ret:
                    ret = cur

        return ret
