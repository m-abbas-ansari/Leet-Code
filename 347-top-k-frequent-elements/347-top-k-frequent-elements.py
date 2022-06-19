class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort: where the buckets are the counts in which numbers are put in
        # Maintain a dictionary where keys go from 0 to n where n is the total number of 
        # elements in the nums array. The value for each key is the corresponding element
        # whose number of occurence in the nums array is equal to the key.
        # To get top k: traverse dict from n to 0 (reverse order) and find top k
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # maintains the buckets where index is the count/freq.
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            