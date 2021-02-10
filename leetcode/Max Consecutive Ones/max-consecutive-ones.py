class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # string = ''.join(str(num) for num in nums).split('0')
        # return max([len(s) for s in string])
        max_range = 0
        count = 0
        for num in nums:
            count += 1
            if num == 0:
                count = 0
                continue
            if count > max_range:
                max_range = count

        return max_range