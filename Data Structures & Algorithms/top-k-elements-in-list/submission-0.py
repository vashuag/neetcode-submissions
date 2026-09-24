class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for i in nums:
            hashmap[i] += 1
            
        top_k_keys = [item[0] for item in sorted(hashmap.items(), key=lambda item: item[1], reverse=True)[:k]]
        return top_k_keys