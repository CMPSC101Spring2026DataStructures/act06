# Tutorial 3: Advanced Sphinx Features and Professional Documentation

## Overview

In the previous tutorials, you learned Sphinx basics and how to document multi-module projects. In this final tutorial, you'll explore advanced features that professional Python projects use to create polished, comprehensive documentation.

These features include:

- Multiple documentation pages (not just API reference)
- Detailed configuration options
- Custom styling and branding
- Advanced extensions for code examples and testing
- Documentation best practices

By the end, you'll understand how mature projects like Django, NumPy, and Flask maintain high-quality documentation that serves both new users and advanced developers.

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Advanced Topics in Sphinx

### 1. Multiple Documentation Pages

Professional projects have more than just API documentation:

- **Getting Started Guide**: Quick setup instructions for new users
- **Tutorials**: Step-by-step guides for common tasks
- **User Guide**: Detailed explanation of features
- **API Reference**: Complete function documentation (what Tutorial 2 focused on)
- **Contributing Guide**: Instructions for developers wanting to contribute
- **FAQ**: Common questions and answers
- **Troubleshooting**: Known issues and solutions

### 2. Configuration and Customization

Sphinx has hundreds of configuration options in `conf.py`:

- **Theme selection**: Choose or customize the visual appearance
- **Extensions**: Add functionality like code testing, PDF generation, etc.
- **Build output formats**: HTML, PDF, ePub, Markdown, etc.
- **Custom CSS/JavaScript**: Branding and special styling

### 3. Advanced Extensions

Sphinx can integrate with other tools:

- **sphinx.ext.doctest**: Test code examples in documentation
- **sphinx.ext.imgmath**: Render mathematical expressions
- **sphinx.ext.todo**: Track TODO items in documentation
- **sphinx.ext.coverage**: Check if all code is documented
- **sphinx.ext.napoleon**: Parse Google and NumPy style docstrings
- **myst-parser**: Write documentation in Markdown instead of reStructuredText

### 4. Linking and Cross-References

As documentation grows, you need to:

- Link between documentation pages
- Reference specific functions from other modules
- Link to external documentation
- Create automatic indexes and tables of contents

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 1: Create the Project Environment

Move to the project folder:

```bash
cd sphinx_advanced
```

Initialize with UV:

```bash
uv init
```

Install packages including an additional theme:

```bash
uv add sphinx sphinx-rtd-theme sphinx-book-theme
```

This installs:

- **sphinx**: The documentation generator
- **sphinx-rtd-theme**: "Read the Docs" theme (professional, widely-used)
- **sphinx-book-theme**: Alternative modern theme (polished, book-like)

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 2: Understand the Complex Project Structure

This tutorial has a more sophisticated structure:

### [core.py](../sphinx_advanced/core.py)

The main module with several functions. Complete TODO docstrings.

### [utilities.py](../sphinx_advanced/utilities.py)

Helper functions used by core. Complete TODO docstrings.

### [config.py](../sphinx_advanced/config.py)

Configuration and constants. Complete TODO docstrings.

Your tasks:

1. **Complete all function docstrings** in each module (NumPy format)
2. **Add detailed module docstrings** explaining the purpose and usage of each module
3. **Include Examples sections** with realistic code snippets
4. **Document edge cases** where relevant (what happens with unusual inputs)

### Hints

**core.py functions:**

- `process_data()`: Main data processing function
- `validate_input()`: Checks if input is valid
- `generate_report()`: Creates a summary report

**utilities.py functions:**

- `format_output()`: Formats results nicely
- `calculate_metrics()`: Computes summary metrics  
- `log_event()`: Records events

**config.py:**

- Usually just constants and configuration values
- Document what each constant means

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 3: Set Up Advanced Sphinx Configuration

Initialize Sphinx:

```bash
uv run sphinx-quickstart -q -p "Advanced Analytics" -a "Your Name" -r "3.0.0" docs
```

Edit `docs/conf.py`. Update it with advanced configuration:

```python
# Add extensions
extensions = [
    'sphinx.ext.autodoc',        # Auto-include docstrings
    'sphinx.ext.viewcode',       # Show source code
    'sphinx.ext.intersphinx',    # Link to other projects
    'sphinx.ext.doctest',        # Test code in examples
    'sphinx.ext.todo',           # Track TODOs in docs
    'sphinx.ext.napoleon',       # Read NumPy/Google style docstrings
]

# Configure napoleon to use NumPy style
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_admonition_for_examples = True

# Theme selection
html_theme = 'sphinx_book_theme'

# Theme options
html_theme_options = {
    "repository_url": "https://github.com/yourusername/project",
    "use_issues_button": True,
    "use_repository_button": True,
    "logo": {
        "image_light": "logo.png",
        "image_dark": "logo_dark.png",
    }
}

# Add a project-wide search notice
html_search_options = {'typ': 'QueryString'}

# Show TODO items in the documentation
todo_include_todos = True

# HTML output options
html_static_path = ['_static']
html_title = "Advanced Analytics Documentation"
html_logo = "logo.png"
html_favicon = "favicon.ico"
```

### What These Settings Do

**Extensions:**

- `napoleon`: Sphinx needs this to understand NumPy-style docstrings automatically
- `doctest`: Allows testing code examples in documentation
- `todo`: For marking incomplete documentation

**Theme Options:**

- `html_theme = 'sphinx_book_theme'`: Modern, polished appearance
- `html_theme_options`: Customize theme appearance (logo, links, colors)

**HTML Output:**

- `html_static_path`: Location of images, CSS, JavaScript files
- `html_logo`: Project logo displayed in documentation header
- `html_favicon`: Small icon in browser tab

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 4: Create Multiple Documentation Pages

Professional documentation has multiple pages. Create `docs/index.rst`:

```restructuredtext
Advanced Analytics Platform
============================

Welcome to the Advanced Analytics Platform documentation.

This platform provides tools for processing, analyzing, and reporting on
complex datasets. Whether you're new to data analysis or an experienced user,
this documentation has you covered.

**Getting Started**

If you're new, start here:

.. toctree::
   :maxdepth: 2

   getting_started
   tutorial_basic

**User Guide**

Learn how to accomplish specific tasks:

.. toctree::
   :maxdepth: 2

   guide/data_processing
   guide/analysis
   guide/reporting

**API Reference**

Complete reference for all functions and classes:

.. toctree::
   :maxdepth: 2

   api/core
   api/utilities
   api/config

**Additional Resources**

.. toctree::
   :maxdepth: 1

   faq
   troubleshooting
   contributing
```

### Understanding the toctree directive

The `.. toctree::` directive creates:

- A table of contents (outline structure)
- Navigation menus
- Automatic cross-linking between pages

The `:maxdepth:` option controls how many levels of headings to display.

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 5: Create Additional Documentation Pages

Create these RST files in the `docs/` directory:

### docs/getting_started.rst

```restructuredtext
Getting Started
===============

Installation
------------

You can install the Advanced Analytics Platform using pip::

    pip install advanced-analytics

Quick Start
-----------

Here's a simple example to get started:

.. code-block:: python

    from core import process_data
    from utilities import format_output
    
    # Load and process your data
    result = process_data([1, 2, 3, 4, 5])
    
    # Format the output nicely
    output = format_output(result)
    print(output)

Next Steps
----------

- Read the :ref:`tutorial_basic` for a deeper introduction
- Check the :ref:`api_reference` for complete function details
- Visit :ref:`faq` for common questions
```

### docs/faq.rst

```restructuredtext
Frequently Asked Questions
===========================

How do I process large datasets?
---------

Use the batch processing mode in :func:`core.process_data` with the
:code:`batch_size` parameter::

    result = process_data(large_data, batch_size=1000)

What if my data contains errors?
--------------------------------

The :func:`core.validate_input` function automatically checks for issues.
Use it before processing::

    if validate_input(your_data):
        result = process_data(your_data)
    else:
        print("Data has errors")

Can I customize the output format?
----------------------------------

Yes! Use the :func:`utilities.format_output` function with different
format options::

    clean_output = format_output(result, format='json')
    console_output = format_output(result, format='table')
```

### docs/troubleshooting.rst

```restructuredtext
Troubleshooting
===============

Common Issues and Solutions
----------------------------

Import Errors
~~~~~~~~~~~~~

**Problem**: `ImportError: cannot import name 'process_data'`

**Solution**: Make sure you've installed the package correctly::

    pip install --upgrade advanced-analytics

Type Errors
~~~~~~~~~~~

**Problem**: `TypeError: process_data() got unexpected keyword argument`

**Solution**: Check the function signature in the :ref:`api_reference`.
Common issue: using :code:`batch_size` without proper array input.

Performance Issues
~~~~~~~~~~~~~~~~~~

**Problem**: Processing is slow

**Solution**: 
1. Check if you're working with large files (see :ref:`faq`)
2. Use batch processing with smaller :code:`batch_size` values
3. Consider filtering data before processing (see :func:`core.validate_input`)
```

### docs/contributing.rst

```restructuredtext
Contributing
=============

We welcome contributions! Here's how to help:

Setting Up Development Environment
-----------------------------------

1. Clone the repository
2. Create a virtual environment
3. Install development dependencies::

    pip install -e ".[dev]"

4. Run the tests::

    pytest

Documentation Standards
-----------------------

- All public functions must have complete docstrings
- Follow NumPy docstring format (see examples in :ref:`api_reference`)
- Include at least one example in the Examples section
- Document parameters, returns, and possible exceptions

Running Documentation Locally
------------------------------

To build and review documentation locally::

    cd docs
    sphinx-build -b html . _build/html

Then open `_build/html/index.html` in your browser.
```

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 6: Create Sophisticated API Documentation Pages

Create separate files for each module's detailed API documentation.

### docs/api/core.rst

```restructuredtext
Core Module
===========

The core module contains the main functions for data processing.

.. py:module:: core
   :noindex:

.. automodule:: core
   :members:
   :undoc-members:
   :show-inheritance:
```

### docs/api/utilities.rst

```restructuredtext
Utilities Module
================

Utility functions for formatting, metrics, and logging.

.. py:module:: utilities
   :noindex:

.. automodule:: utilities
   :members:
   :undoc-members:
   :show-inheritance:
```

### docs/api/config.rst

```restructuredtext
Configuration Module
====================

Configuration constants and settings.

.. py:module:: config
   :noindex:

.. automodule:: config
   :members:
   :undoc-members:
   :show-inheritance:
```

### docs/guide/data_processing.rst

```restructuredtext
Data Processing Guide
=====================

This guide explains how to process your data effectively.

Overview
--------

The data processing pipeline has three main steps:

1. **Validation**: Check data integrity with :func:`core.validate_input`
2. **Processing**: Transform and analyze with :func:`core.process_data`
3. **Formatting**: Prepare output with :func:`utilities.format_output`

Step-by-Step Example
--------------------

.. code-block:: python

    from core import validate_input, process_data
    from utilities import format_output
    
    # Step 1: Validate
    data = [1, 2, 3, 4, 5]
    if not validate_input(data):
        print("Invalid data!")
        exit(1)
    
    # Step 2: Process
    results = process_data(data)
    
    # Step 3: Format
    nicely_formatted = format_output(results)
    print(nicely_formatted)

Advanced Options
----------------

For more control, see:

- :func:`core.process_data` for advanced parameters
- :func:`utilities.format_output` for output customization
- :ref:`faq` for common questions
- :ref:`troubleshooting` for error solutions
```

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 7: Build Complete Documentation

Build the full documentation with all pages:

```bash
cd docs
uv run sphinx-build -b html . _build/html
```

The build process will:

1. Read all .rst files
2. Extract docstrings from Python modules
3. Generate HTML pages for each section
4. Create automatic table of contents
5. Build search index
6. Apply the theme

If there are errors, they'll be printed to help you fix them.

### View the Result

Open `docs/_build/html/index.html` in your browser.

You now have:

- ✅ A beautiful landing page
- ✅ Getting started guide
- ✅ Tutorial pages
- ✅ Complete API reference
- ✅ FAQ and troubleshooting
- ✅ Contributing guide
- ✅ Professional theme and layout
- ✅ Search functionality across all pages
- ✅ Auto-generated table of contents
- ✅ Cross-references between pages

This is what professional Python project documentation looks like!

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 8: Advanced Features to Explore

Once you have the basic structure working, try these advanced features:

### 1. Add a Logo and Custom Styling

Place a logo image in `docs/_static/logo.png` and update `conf.py`:

```python
html_logo = "_static/logo.png"
```

### 2. Test Code Examples

Add this to `conf.py`:

```python
extensions = [..., 'sphinx.ext.doctest']
```

Then Sphinx can actually run and test the code in your examples!

### 3. Add Badges

In your main `index.rst`, add badges (like "see on GitHub"):

```restructuredtext
.. image:: https://img.shields.io/badge/GitHub-View%20on%20GitHub-blue
   :target: https://github.com/yourusername/yourproject
```

### 4. Support Multiple Languages

Sphinx can generate documentation in multiple languages through configuration.

### 5. Deploy to ReadTheDocs

Services like [ReadTheDocs.org](https://readthedocs.org/) automatically:

- Host your documentation online
- Rebuild it when you push code changes
- Support multiple versions
- Provide beautiful hosting

Just connect your GitHub repository!

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Real-World Documentation Examples

Study how major projects use Sphinx:

### Django (https://docs.djangoproject.com/)

- Multiple versions (latest, older versions)
- Search across all documentation
- Professional theme
- Hundreds of pages of content
- Includes tutorials, guides, and API reference

### NumPy (https://numpy.org/doc/stable/)

- Mathematical notation support
- Code examples with output
- Multiple language versions
- Complex API for scientific computing
- Well-organized for both users and developers

### Sphinx itself (https://www.sphinx-doc.org/)

- Self-documenting (documentation of the documentation tool!)
- Shows all Sphinx features in practice
- Excellent examples of best practices
- Multiple output formats

Notice the common patterns:

1. Clear structure (Getting Started → Guides → API)
2. Professional appearance (good theme)
3. Multiple perspectives (user guides + API reference)
4. Good search and navigation
5. Version tracking

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Summary

In this tutorial you:

1. ✅ Understood advanced Sphinx configuration options
2. ✅ Structured documentation for multiple audiences (beginners and advanced users)
3. ✅ Created multiple documentation pages (guides, API, FAQ, contributing)
4. ✅ Learned about Sphinx extensions and their purposes
5. ✅ Built a professional, multi-page documentation site
6. ✅ Studied real-world examples from major Python projects
7. ✅ Understood the relationship between good code and good documentation

## Key Insights

**Professional documentation is not just API reference:**

- Users need getting started guides
- Developers need troubleshooting help
- Contributors need setup instructions
- Everyone benefits from examples and FAQs

**Documentation quality reflects code quality:**

- Projects with excellent documentation are trusted more
- Clear documentation makes code easier to use
- Documentation catches design issues (if it's hard to document, it's probably hard to use)

**Sphinx enables world-class documentation:**

- Keeps documentation in sync with code
- Generates beautiful HTML automatically
- Supports multiple output formats
- Scales to thousands of pages
- Used by most professional Python projects

This is why every Python programmer should learn Sphinx - it's the industry standard for creating professional documentation!

**Congratulations!** You've completed all three tutorials on Sphinx. You now have the skills to document Python projects professionally like Django, NumPy, and other major projects use.
