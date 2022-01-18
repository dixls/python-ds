def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_counts = {x: nums.count(x) for x in nums}
    highest = 0
    for num in num_counts.keys():
        if highest == 0:
            highest = num
        if num_counts[num] > num_counts[highest]:
            highest = num
    return highest