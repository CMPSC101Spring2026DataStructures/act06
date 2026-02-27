# Add Your Name Here

# TODO: Add a module-level docstring at the very top, before any imports.
# A module docstring explains what this entire module does.
# Format:
# """
# Module name and brief description.
# 
# Longer description explaining what this module does.
# """

from __future__ import annotations
from statistics import mean, median, stdev
from typing import Optional


def calculate_mean(data: list[float]) -> float:
    # TODO: Write a complete docstring for this function in NumPy format.
    # Include: description, Parameters section, Returns section, and Examples section.
    # Hint: The function calculates the average of a list of numbers.
    pass


def calculate_median(data: list[float]) -> float:
    # TODO: Write a complete docstring for this function in NumPy format.
    # Include: description, Parameters section, Returns section, and Examples section.
    # Hint: The function finds the middle value in a sorted list.
    pass


def calculate_standard_deviation(data: list[float]) -> float:
    # TODO: Write a complete docstring for this function in NumPy format.
    # Include: description, Parameters section, Returns section, and Examples section.
    # Hint: The function measures how spread out the values are.
    pass


def find_outliers(data: list[float], std_multiplier: float = 2.0) -> list[float]:
    """Find outlier values in a dataset based on standard deviation.
    
    This function identifies values that are more than a specified number of
    standard deviations away from the mean. These values are considered outliers.
    
    Parameters
    ----------
    data : list[float]
        A list of numeric values to analyze.
    std_multiplier : float, optional
        How many standard deviations away from the mean qualifies as an outlier.
        Default is 2.0 (values more than 2 standard deviations from mean).
    
    Returns
    -------
    list[float]
        A list of all values that are outliers, in the order they appear
        in the original data list.
    
    Examples
    --------
    >>> find_outliers([1, 2, 3, 4, 100])
    [100]
    >>> find_outliers([10, 20, 30, 40, 50], std_multiplier=1.0)
    [10, 50]
    """
    if len(data) < 2:
        return []
    
    dataset_mean = calculate_mean(data)
    dataset_std = calculate_standard_deviation(data)
    
    outliers = []
    for value in data:
        distance_from_mean = abs(value - dataset_mean)
        if distance_from_mean > (std_multiplier * dataset_std):
            outliers.append(value)
    
    return outliers


# IMPORTANT: Implement the TODO functions above with these definitions:
# For calculate_mean: return mean(data)
# For calculate_median: return median(data)
# For calculate_standard_deviation: return stdev(data)
