def test_quick_sort():
    print("Quick Sort!!!")
    nums = [5, 9, 10, 12, 1, 4, 7]

    quick_sort_recursive(nums, 0, len(nums) - 1)
    print(nums)


def quick_sort_recursive(nums: list, l: int, r: int) -> None:
    if l > r:
        return

    pivot = partition(nums, l, r)

    quick_sort_recursive(nums, l, pivot - 1)
    quick_sort_recursive(nums, pivot + 1, r)


def partition(nums: list, l: int, r: int) -> int:
    index = l
    for i in range(index, r):
        if nums[i] < nums[r]:
            tmp = nums[i]
            nums[i] = nums[index]
            nums[index] = tmp
            index += 1

    tmp = nums[index]
    nums[index] = nums[r]
    nums[r] = tmp

    return index


test_quick_sort()
