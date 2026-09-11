#!/usr/bin/python3
def weight_average(my_list=[]):
    """Compute the weighted average of a list of (score, weight) tuples

    Args:
        my_list: a list of tuples (score, weight), both integers

    Returns:
        The weighted average of all scores, or 0 if my_list is
        empty or the total weight is 0
    """
    if len(my_list) == 0:
        return 0

    total_score = 0
    total_weight = 0
    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    return total_score / total_weight
