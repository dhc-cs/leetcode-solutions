from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #creating an empty hash map/dictionary
        #will hold key value pairs 
        #Each key will be the value of nums list 
        #and each value will be its index
        numsDict = {}

        #iterating over the list to populate the hash map 
        for i, num in enumerate(nums):
            numsDict[num] = i
        
        #iterate over the list to compute the compliment
        for i, num in enumerate(nums):
            compliment = target - num

            #check to see if compliment exits in hashmap
            if compliment in numsDict:
                #check to make sure we aren't using the same element twice
                if numsDict[compliment] != i:
                    #return the index of both numbers 
                    return [i, numsDict[compliment]]


#driver
if __name__ == "__main__":
    mySolution = Solution()

    nums = [2,7,11,15]
    target=50

    result = mySolution.twoSum(nums, target)
    print(result)