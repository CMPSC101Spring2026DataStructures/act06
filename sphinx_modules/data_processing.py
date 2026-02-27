# Add Your Name Here

# TODO: Add a module-level docstring here explaining what this module does.
# This module handles loading and processing data from CSV files.

from __future__ import annotations
from pathlib import Path
from statistics import mean, stdev
from typing import Optional


def load_csv_data(file_path: str) -> dict[str, list[float]]:
    # TODO: Write a complete NumPy-style docstring for this function.
    # It loads data from a CSV file and returns it as a dictionary.
    pass


def clean_data(data: dict[str, list[float]]) -> dict[str, list[float]]:
    # TODO: Write a complete NumPy-style docstring for this function.
    # It removes None values and empty entries from data.
    pass


def filter_outliers(data: dict[str, list[float]], threshold: float = 2.0) -> dict[str, list[float]]:
    # TODO: Write a complete NumPy-style docstring for this function.
    # It removes outlier values (more than threshold standard deviations from mean).
    pass


# Implementations for testing
def load_csv_data(file_path: str) -> dict[str, list[float]]:
    """Load data from a CSV file into a dictionary.
    
    Parameters
    ----------
    file_path : str
        Path to the CSV file to load.
    
    Returns
    -------
    dict[str, list[float]]
        Dictionary where keys are column names and values are lists of data.
    """
    # Simplified implementation for demonstration
    return {
        "column1": [1.0, 2.0, 3.0, 4.0, 5.0],
        "column2": [10.0, 20.0, 30.0, 40.0, 50.0],
    }


def clean_data(data: dict[str, list[float]]) -> dict[str, list[float]]:
    """Remove None values and empty entries from data.
    
    Parameters
    ----------
    data : dict[str, list[float]]
        Dictionary with column data to clean.
    
    Returns
    -------
    dict[str, list[float]]
        Dictionary with None values removed.
    """
    cleaned = {}
    for key, values in data.items():
        cleaned[key] = [v for v in values if v is not None]
    return cleaned


def filter_outliers(data: dict[str, list[float]], threshold: float = 2.0) -> dict[str, list[float]]:
    """Filter out outlier values from each column.
    
    Parameters
    ----------
    data : dict[str, list[float]]
        Dictionary with column data to filter.
    threshold : float, optional
        Number of standard deviations away from mean to consider an outlier.
        Default is 2.0.
    
    Returns
    -------
    dict[str, list[float]]
        Dictionary with outliers removed from each column.
    """
    filtered = {}
    for key, values in data.items():
        if len(values) < 2:
            filtered[key] = values
            continue
        
        col_mean = mean(values)
        col_std = stdev(values)
        filtered[key] = [v for v in values if abs(v - col_mean) <= threshold * col_std]
    
    return filtered
