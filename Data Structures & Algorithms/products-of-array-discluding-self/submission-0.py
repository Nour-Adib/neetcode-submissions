class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        products = []

        for i in range(0, len(nums)):
            interm_product = 1
            for j in range(0, len(nums)):
                if i != j:
                    interm_product = interm_product * nums[j]

            products.append(interm_product)

        return products 

        