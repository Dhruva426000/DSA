def secondLargest(nums):

    first = float('-inf')
    second = float('-inf')

    for num in nums:

        if num > first:
            second = first
            first = num

        elif num > second and num != first:
            second = num

    return second