# ==============================================================================
# FILE: assignment2.py
# ==============================================================================
# Assignment 2
# This file provides a function `avg_two`, which calculates the average of
# numbers in a given list that are divisible by 2. Learners are expected to
# implement the logic within the specified section of the function.

# Instructions:
# - Complete the `avg_two` function as described in its docstring.
# - Do not modify code outside the indicated editable section.
#
# Testing:
# - To verify your implementation, run the provided test file:
#   test_assignment2.py, using the command:
#   python -m unittest test_assignment2.py
# ------------------------------------------------------------------------------


def avg_two(input_list: list[int]) -> float:
    """
    This functions takes a list of integers and returns the average for
    the numbers that are divisible by 2.

    :param input_list:  Input list of integers to selectively average.
    :type input_list:   list[int]

    :returns:   Average of numbers in the list that are divisible by 2.
    :rtype:     float
    """
    ############
    # ONLY EDIT UNDER HERE
    #Step 1: Create a new list to house numbers divisible by 2.
    div_by_two = []

    #Step 2: Iterate over the input list and append anything divisible by 2.
    for i in range(len(input_list)):
        if input_list[i] % 2 == 0:
            div_by_two.append(input_list[i])
        else:
            pass
    
    #Step 3: Check the length of the div_by_two list:
    if len(div_by_two) == 0:
        return(0)
    else:
        return(sum(div_by_two)/len(div_by_two))
    # ONLY EDIT ABOVE HERE
    ######
