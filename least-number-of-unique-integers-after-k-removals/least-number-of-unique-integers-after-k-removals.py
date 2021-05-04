class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        countMap = {}
        for num in arr:
            if num not in countMap:
                countMap[num] = 1
            else:
                countMap[num] += 1
                
        sortMap = dict(sorted(countMap.items(), key = lambda x:x[1]))
       
        while k != 0:
            for key,value in sortMap.items():
                if k < sortMap[key]:
                    return len(sortMap)
                else:
                    k = k - sortMap[key]
                    sortMap.pop(key)
                    break
        return len(sortMap)
        
                
                               
                
#         print(countMap)
#         while k != 0:
#             if countMap[num] == 1:
#                 del countMap[num]
#                 k -= 1
#                 print(countMap,k)
                
#             # if countMap[num] > 1:
#             #     del countMap[num]
#             #     k -= 1
        
#         return len(countMap)
                    