class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_list = []
        product = 1
        zero_seen = False
        for x in range(0,len(nums)):
            if nums[x] != 0:
                product = nums[x] * product
            else:
                if zero_seen == True:
                    product = 0
                zero_seen = True
        for y in range(0,len(nums)):
            if nums[y] == 0:
                prod_list.append(product)
            elif zero_seen == True:
                prod_list.append(0)
            else:
                div_prod = int(product/nums[y])
                prod_list.append(div_prod)
        return prod_list
