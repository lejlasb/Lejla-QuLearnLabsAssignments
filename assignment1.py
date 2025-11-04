# ==============================================================================
# FILE: assignment1.py
# ==============================================================================
# Assignment 1
# This file provides a function `avg_three`, which calculates the average of
# numbers in a given list that are divisible by 3. Learners are expected to
# implement the logic within the specified section of the function.
#
# Instructions:
# - Complete the `avg_three` function as described in its docstring.
# - Do not modify code outside the indicated editable section.
#
# Testing:
# - To verify your implementation, run the provided test file:
#   test_assignment1.py, using the command:
#   python -m unittest test_assignment1.py
# ------------------------------------------------------------------------------


def avg_three(input_list: list[int]) -> float:
    """
    This functions takes a list of integers and returns the average for
    the numbers that are divisible by 3.

    :param input_list:  Input list of integers to selectively average.
    :type input_list:   list[int]

    :returns:   Average of numbers in the list that are divisible by 3.
    :rtype:     float
    """
    ############
    # ONLY EDIT UNDER HERE
    
    #Step 1: Create an empty list to hold the numbers
    div_by_three = []
    
    #Step 2 & 3: Test if each number is div by 3, then append to list or pass.
    #Use a for loop to loop over the entire list and print the list:
    for i in range(len(input_list)):
        if input_list[i] % 3 == 0:
            div_by_three.append(input_list[i])
        else:
            pass

    #Step 4: Check if list is empty
    if len(div_by_three) == 0:
        return(0)
    else:
        #Step 4b: Calculate the average
        average = sum(div_by_three)/len(div_by_three)
        return(average)
    # ONLY EDIT ABOVE HERE
    ######
