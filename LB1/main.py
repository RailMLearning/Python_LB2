def sum_finder(nums, target):
    if len(nums) <= 1:
        return None
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return [i,j]
    return None