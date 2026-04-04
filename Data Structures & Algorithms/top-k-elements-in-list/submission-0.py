class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        top_k_element = count.most_common(k)
        return [item[0] for item in top_k_element]

        