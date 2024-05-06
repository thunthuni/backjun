while True:
    try:
        nums = list(map(int, input().split()))
        if sum(nums) != 0:
            max_idx = 0
            max_v = max(nums)
            nums.remove(max_v)

            if (nums[0] ** 2) + (nums[1] ** 2) == (max_v ** 2):
                print('right')
            else:
                print('wrong')
    except:
        break



