def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0
        
        for i, x in enumerate(nums):
            if leftsum == (S - x - leftsum):
                return i
            leftsum += x
        return -1

def dominantIndex(self, nums: List[int]) -> int:
        import numpy as np
        largest = max(nums)
        for i, x in enumerate(nums):
            if x*2 > largest and x!=largest:
                return -1
        return np.argmax(nums)

def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        lst = []
        for i in digits:
            num += str(i)
    
        num = int(num)+1
        for i in str(num):
            lst.append(i)
        return lst