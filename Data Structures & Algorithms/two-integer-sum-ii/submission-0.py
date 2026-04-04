class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = []
        for i,num in enumerate(numbers):
            complement = target - num
            if complement in seen:
                first_index = seen.index(complement)
                return [first_index + 1, i + 1]
            seen.append(num)


        