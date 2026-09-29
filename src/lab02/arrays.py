def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError

    minimum = nums[0]
    maximum = nums[0]

    for i in nums:
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i

    return minimum, maximum

def unique_sorted(nums: list[float | int]) -> list[float | int]:

    uniq_nums = list(set(nums))

    for i in range(len(uniq_nums)):
        for j in range(len(uniq_nums)-i-1):
            if uniq_nums[j] > uniq_nums[j+1]:
                uniq_nums[j], uniq_nums[j+1] = uniq_nums[j+1], uniq_nums[j]
    return uniq_nums


def flatten(mat: list[list | tuple]) -> list:

    result = []

    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError

        result.extend(row)

    return result

if __name__ == "__main__":

    print(min_max([3, -1, 5, 5, 0]))
    print(min_max([42]))
    print(min_max([-5, -2, -9]))
    print(min_max([1.5, 2, 2.0, -3.1]))
    print(min_max([]))

    print(unique_sorted([3, 1, 2, 1, 3]))
    print(unique_sorted([]))
    print(unique_sorted([-1, -1, 0, 2, 2]))
    print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

    print(flatten([[1, 2], [3, 4]]))
    print(flatten([[1, 2], (3, 4, 5)]))
    print(flatten([[1], [], [2, 3]]))
    print(flatten([[1, 2], "ab"]))