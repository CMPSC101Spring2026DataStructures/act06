# Add Your Name Here

# TODO: Add a comprehensive module-level docstring explaining this module's purpose.
# This module contains helper and utility functions.

from __future__ import annotations
from typing import Any
import json
from datetime import datetime


def format_output(data: dict[str, Any], format: str = "text") -> str:
    # TODO: Write a complete NumPy-style docstring.
    # Formats data for output in various formats.
    pass


def calculate_metrics(results: dict[str, Any]) -> dict[str, float]:
    # TODO: Write a complete NumPy-style docstring.
    # Calculates additional metrics from results.
    pass


def log_event(event_type: str, message: str) -> None:
    # TODO: Write a complete NumPy-style docstring.
    # Logs an event with timestamp.
    pass


# Implementations follow
def format_output(data: dict[str, Any], format: str = "text") -> str:
    """Format data for output in various formats.
    
    Takes a dictionary and returns it formatted as requested. Supports
    multiple output formats for flexibility in how results are displayed.
    
    Parameters
    ----------
    data : dict[str, Any]
        Data dictionary to format.
    format : str, optional
        Output format: 'text' (default), 'json', or 'table'.
    
    Returns
    -------
    str
        Formatted data as a string.
    
    Examples
    --------
    >>> data = {'mean': 3.5, 'count': 10}
    >>> text_output = format_output(data, format='text')
    >>> json_output = format_output(data, format='json')
    """
    if format == 'json':
        return json.dumps(data, indent=2)
    elif format == 'table':
        output = "Key              | Value\n"
        output += "-" * 40 + "\n"
        for key, value in data.items():
            output += f"{key:16} | {value}\n"
        return output
    else:  # text format (default)
        output = ""
        for key, value in data.items():
            output += f"{key}: {value}\n"
        return output


def calculate_metrics(results: dict[str, Any]) -> dict[str, float]:
    """Calculate additional metrics from processing results.
    
    Takes basic statistical results and computes derived metrics
    like coefficient of variation and range.
    
    Parameters
    ----------
    results : dict[str, Any]
        Dictionary from process_data() with basic statistics.
    
    Returns
    -------
    dict[str, float]
        Dictionary with additional metrics:
        - 'range': max - min
        - 'coefficient_of_variation': std / mean
        - 'relative_std': std / mean * 100
    
    Examples
    --------
    >>> results = {'mean': 10, 'std': 2, 'min': 5, 'max': 15}
    >>> metrics = calculate_metrics(results)
    >>> metrics['range']
    10
    """
    mean_val = results.get('mean', 0)
    std_val = results.get('std', 0)
    min_val = results.get('min', 0)
    max_val = results.get('max', 0)
    
    cv = std_val / mean_val if mean_val != 0 else 0.0
    
    return {
        'range': max_val - min_val,
        'coefficient_of_variation': cv,
        'relative_std': cv * 100
    }


def log_event(event_type: str, message: str) -> None:
    """Log an event with timestamp.
    
    Records an event to the console with a timestamp for debugging
    and monitoring purposes.
    
    Parameters
    ----------
    event_type : str
        Type of event (e.g., 'INFO', 'WARNING', 'ERROR').
    message : str
        Event message to log.
    
    Returns
    -------
    None
    
    Examples
    --------
    >>> log_event('INFO', 'Processing started')
    [2024-02-26 10:30:45] INFO: Processing started
    >>> log_event('ERROR', 'Invalid data')
    [2024-02-26 10:30:46] ERROR: Invalid data
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {event_type}: {message}")
