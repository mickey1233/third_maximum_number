def thirdmax(nums):
    tmp = set()
    sum = 0
    while nums:
        nums = set(nums)
        rel = max(nums)
        tmp.add(rel)
        nums.remove(rel)
        sum = sum + 1
        if sum == 3:
            return rel
    return max(tmp)


if __name__ == "__main__":
    print(thirdmax([3, 2, 1]))
    print(thirdmax([1, 2]))
    print(thirdmax([2, 2, 3, 1]))
    print(thirdmax([1, 2, 2, 5, 3, 5]))
    print(thirdmax([1, 2, 2, 5, 3, 5, 6]))
