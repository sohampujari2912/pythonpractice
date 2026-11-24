class Solution(object):
    def duplicateZeros(self, arr):
        n = len(arr)
        
        i = 0
        while i < n - 1:
            if arr[i] == 0:
                for j in range(n - 1, i, -1):
                    arr[j] = arr[j - 1]
                
                i += 1
            
            i += 1
arr=[1,2,0,0,3,4,0,5,0]

obj=Solution()
obj.duplicateZeros(arr)

print(arr)