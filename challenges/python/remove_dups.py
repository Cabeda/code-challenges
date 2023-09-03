#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

def removeDuplicates(nums: list[int]) -> int:
    nums = list(set(nums))
    print(nums)
    return len(nums)
        

# nums = [0,0,1,1,1,2,2,3,3,4]


nums = [1,1,2]
expectedNums = [1,2]

k = removeDuplicates(nums)

assert k == len(expectedNums)
for i in range(0, k):
    assert nums[i] == expectedNums[i]