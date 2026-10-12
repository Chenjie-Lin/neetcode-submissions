import random
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        def quickSort(arr, lo, hi):
            if lo >= hi:
                return 
            p = partition(arr, lo, hi)
            quickSort(arr, lo, p-1)
            quickSort(arr, p+1, hi)
        
        def partition(arr, lo, hi):
            r = random.randint(lo, hi)
            i = lo
            pivot = arr[r]
            arr[r], arr[hi] = arr[hi], arr[r]
            for j in range(lo, hi):
                if arr[j] < pivot:
                    arr[j], arr[i] = arr[i], arr[j]
                    i += 1
            
            arr[i], arr[hi] = arr[hi], arr[i]

            return i

        quickSort(nums, 0, len(nums) - 1)