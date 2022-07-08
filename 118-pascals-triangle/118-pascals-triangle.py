class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            result.append([1])
        for j in range(1,numRows):
            result[j].append(1)
        for k in range(2,numRows):
            for x in range(1,k):
                result[k].insert(x,result[k-1][x-1]+result[k-1][x])
                    
        return result
            
        