def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    result = {}

    for num in nums:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1

    highest_count = 0
    num_to_return = 0
    for key in nums:
        if result[num] > highest_count:
            highest_count = result[num]
            num_to_return = num

    return num_to_return

