from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashTable = {}

        for i, num in enumerate(nums):
            hashTable[num] = i
            print(f'key: {num}')
            print(f'value: {hashTable[num]}\n')
            
            #print(f'i: {i}\n')
        
        #for i in enumerate(nums):
            #print(f'Using enumerate to print out {i}')
        
        print(f'{hashTable.keys()}')
        print(f'{hashTable.values()}')



#driver
if __name__ == "__main__":
    mySolution = Solution()

    nums = [2,7,11,15]
    target=50

    result = mySolution.twoSum(nums, target)
    print(result)