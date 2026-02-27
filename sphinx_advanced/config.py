# Add Your Name Here

# TODO: Add a module-level docstring explaining what configuration is used for.

"""Configuration and Constants Module.

This module defines all configuration constants used throughout the application.
These settings control behavior of data processing, output formatting, and
logging. Modify these constants to customize application behavior.
"""

from __future__ import annotations

# TODO: Add comprehensive docstrings for each constant below.
# Explain what each constant does and typical values.

# Default batch size for processing large datasets
DEFAULT_BATCH_SIZE = 100

# Maximum number of data points to process without batching
MAX_UNBATCHED_SIZE = 1000

# Formats supported for output
SUPPORTED_FORMATS = ['text', 'json', 'table']

# Default output format
DEFAULT_OUTPUT_FORMAT = 'text'

# Standard deviation threshold for outlier detection
OUTLIER_THRESHOLD = 2.0

# Whether to log events
ENABLE_LOGGING = True

# Log level: 'DEBUG', 'INFO', 'WARNING', 'ERROR'
LOG_LEVEL = 'INFO'

# Application version
APP_VERSION = '3.0.0'

# Author information
AUTHOR = 'Your Name'

# Project name
PROJECT_NAME = 'Advanced Analytics'

# Documentation URL
DOCS_URL = 'https://example.com/docs'

# Maximum number of retries for failed operations
MAX_RETRIES = 3

# Timeout in seconds for operations
OPERATION_TIMEOUT = 300
