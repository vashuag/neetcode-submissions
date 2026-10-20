class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res=[1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *=nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix *=nums[i]
        return res
        # n = len(nums)
        # res = [0]*n
        # for i in range(0,len(nums)):
        #     prod = 1
        #     for j in range(0,len(nums)):
        #         if i == j:
        #             continue
        #         prod *= nums[j]
                
        #     res[i] = prod
        # return res
        