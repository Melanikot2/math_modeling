def is_devide_by_three(a):
    return (a % 3 == 0)

nums = [24, 65, 23, -32]
result = list(map(is_devide_by_three, nums))

print(result)


def my_func(a, b):
    return a * b

nums1 = [6, 7, 8, 9]
nums2 = [1, 2, 3, 4]

nums_multipiy = list(map(my_func, nums1, nums2))

print(nums_multipiy)