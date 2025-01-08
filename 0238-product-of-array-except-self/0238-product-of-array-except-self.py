class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n

        total_product = 1
        zero_count = 0
        zero_idx = -1

        for idx, num in enumerate(nums):
            if num == 0:
                print(idx)
                zero_count += 1
                zero_idx = idx

                if zero_count > 1:
                    return answer
            else:
                total_product *= num

        if zero_count == 1:
            answer[zero_idx] = total_product
        else:
            for idx, num in enumerate(nums):
                answer[idx] = total_product // num

        return answer
