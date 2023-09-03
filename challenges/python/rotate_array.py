def rotate(nums: list[int], k: int) -> None:
    print(nums)
    for i in range(0, k):
        val = nums.pop()
        nums.insert(0, val)
        print(nums)



nums = [1,2,3,4,5,6,7]

rotate(nums, 3)