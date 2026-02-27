# Tutorial 2: Documenting Modules with Multiple Functions

## Overview

In this tutorial, you will extend your skills to document a **multi-module project**. Real Python projects typically have:

- Multiple Python files (modules)
- Functions organized by purpose across these modules
- Complex documentation that must show how different modules relate to each other

You will build a project with separate modules for data processing and analysis, then use Sphinx's **autodoc extension** to automatically document all of them together in one organized HTML documentation site.

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## What Are Python Modules?

A **module** in Python is simply a .py file. When projects grow large, they organize code into multiple modules, each handling a specific purpose.

### Example Structure

Instead of putting all code in one file:

```
project/
  main.py (1000 lines - hard to navigate!)
```

Professional projects organize like this:

```
project/
  data_processing.py    (handles loading and cleaning data)
  analysis.py          (handles statistical analysis)
  visualizations.py    (handles creating charts)
  main.py              (coordinates everything)
```

### Benefits

- **Clear organization**: You know where to find specific functionality
- **Team collaboration**: Different team members can work on different modules
- **Code reuse**: Other projects can import and use specific modules
- **Easier testing**: You can test each module independently

### Sphinx Advantage

Sphinx can automatically generate documentation for an entire multi-module project:

- Discovers all Python modules
- Reads all docstrings from all files
- Creates cross-references between modules
- Generates a searchable index across all documentation

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 1: Create the Project Environment

Move into the project folder:

```bash
cd sphinx_modules/
```

Initialize the project with UV:

```bash
uv init
```

Install required packages:

```bash
uv add sphinx sphinx-rtd-theme
```

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 2: Review the Multi-Module Structure

This tutorial has multiple Python modules. Open each file:

### [data_processing.py](../sphinx_modules/data_processing.py)

This module handles loading and processing data. It has:

- A module-level docstring (TODO)
- `load_csv_data()` function with docstring (TODO)
- `clean_data()` function with docstring (TODO)
- `filter_outliers()` function with docstring (TODO)

### [analysis.py](../sphinx_modules/analysis.py)

This module performs analysis on processed data. It has:

- A module-level docstring (TODO)
- `calculate_correlation()` function with docstring (TODO)
- `group_by_category()` function with docstring (TODO)
- `rank_items()` function with docstring (TODO)

### [main.py](../sphinx_modules/main.py)

This is the main entry point that imports and uses the other modules. It has:

- A module-level docstring (TODO)
- Example functions showing how to use the other modules
- The `main()` function with docstring (TODO)

### Your Tasks

For each module, complete the TODO items:

1. **Write module-level docstrings** (at the top of each file)
   - Briefly describe what the module does
   - Explain when you would use it

2. **Write function docstrings** following NumPy format
   - One-line summary
   - Longer description
   - Parameters section
   - Returns section
   - Examples section (where appropriate)

### Hints for Each Module

**For data_processing.py:**

- `load_csv_data()`: Loads data from a CSV file, returns a dictionary
- `clean_data()`: Removes empty values, returns cleaned data
- `filter_outliers()`: Removes values far from the mean, returns filtered data

**For analysis.py:**

- `calculate_correlation()`: Measures relationship between two columns
- `group_by_category()`: Groups data by a column value
- `rank_items()`: Ranks items by a score

**For main.py:**

- Module description: "Main entry point for the data analysis pipeline"
- `main()`: Orchestrates data loading, processing, and analysis

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 3: Create the Sphinx Project

Initialize Sphinx from the sphinx_modules directory:

```bash
uv run sphinx-quickstart -q -p "Data Analysis Pipeline" -a "Your Name" -r "2.0.0" docs
```

Now configure Sphinx to document multiple modules. Edit `docs/conf.py`:

### Step 1: Add Extensions

Find the `extensions = []` line and update it:

```python
extensions = [
    'sphinx.ext.autodoc',        # Read docstrings from Python code
    'sphinx.ext.viewcode',       # Show source code in documentation
    'sphinx.ext.intersphinx',    # Link to other project documentation
]
```

These extensions make Sphinx more powerful:

- `autodoc`: Reads Python docstrings automatically
- `viewcode`: Lets readers click to see the actual Python source code
- `intersphinx`: Can link to other projects' documentation (like Python standard library)

### Step 2: Set the Theme

Find the `html_theme` line and set it:

```python
html_theme = 'sphinx_rtd_theme'
```

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 4: Build Documentation for Multiple Modules

Edit `docs/index.rst` to document all three modules. Replace the entire content with:

```restructuredtext
Data Analysis Pipeline
======================

This project provides a pipeline for loading, processing, and analyzing data
in CSV format. The pipeline is organized into separate modules, each handling
a specific stage of the process.

..............

Data Processing Module
----------------------

Functions for loading and cleaning data from CSV files.

.. automodule:: data_processing
   :members:
   :undoc-members:
   :show-inheritance:

Analysis Module
---------------

Functions for analyzing processed data.

.. automodule:: analysis
   :members:
   :undoc-members:
   :show-inheritance:

Main Entry Point
----------------

The main module that coordinates the entire pipeline.

.. automodule:: main
   :members:
   :undoc-members:
   :show-inheritance:

Table of Functions
-------------------

.. autosummary::
   :toctree: api
   
   data_processing.load_csv_data
   data_processing.clean_data
   data_processing.filter_outliers
   analysis.calculate_correlation
   analysis.group_by_category
   analysis.rank_items
   main.main
```

### Understanding the Directives

- `.. automodule::` - Sphinx instruction to auto-document a module
  - `module_name`: The name of the Python module to document
  - `:members:`: Include all functions and classes
  - `:undoc-members:`: Include members even if not documented
  - `:show-inheritance:`: Show class inheritance (for classes)

- `.. autosummary::` - Creates a summary table of all documented items
  - `:toctree: api`: Create a folder for individual API pages

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 5: Build the Documentation

From the `sphinx_modules` directory:

```bash
cd docs
uv run sphinx-build -b html . _build/html
```

If you see errors, check:

1. Are all docstrings properly formatted?
2. Are module and function names spelled correctly in index.rst?
3. Do all Python files have module-level docstrings?

### Step-by-Step Troubleshooting

If the build fails with messages about missing functions:

1. Check that function names in `index.rst` match actual function names in Python files
2. Verify that all functions have docstrings (even test functions)
3. Make sure the Python module name is correct (filename without `.py`)

If the build doesn't include a function you documented:

1. Verify the function is spelled correctly
2. Check that the module and function are listed in `index.rst`
3. Try running the build again; sometimes caching causes issues

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 6: View and Explore the Documentation

Open `docs/_build/html/index.html` in your browser.

You now have a professional documentation site with:

### Features You'll See

1. **Module Pages**: Separate pages for each module (data_processing, analysis, main)
2. **Function Documentation**: Each function with full docstring content
3. **Cross-References**: Links to related functions in other modules
4. **Parameter Tables**: Formatted lists of parameters for each function
5. **Source Code Links**: Click "View Source" to see the actual Python code
6. **Summary Table**: Quick reference showing all functions

### Navigation

The documentation is organized hierarchically:
```
Main Page (index.rst)
├── Data Processing Module
│   ├── load_csv_data()
│   ├── clean_data()
│   └── filter_outliers()
├── Analysis Module
│   ├── calculate_correlation()
│   ├── group_by_category()
│   └── rank_items()
└── Main Entry Point
    └── main()
```

### Try This

1. Click on a function to see its full documentation
2. Click "View Source" to see the actual Python code
3. Search for a function using the search box
4. Notice how the documentation is automatically generated from your docstrings

**This is the power of Sphinx**: Write good docstrings in your code, and Sphinx automatically creates a beautiful, searchable, cross-referenced documentation site!

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Part 7: Experiment with Changes

Try these experiments to see how Sphinx responds:

### Experiment 1: Add a New Function

1. Add a new function to `data_processing.py` with a complete docstring
2. Add the function to the `index.rst` file
3. Rebuild the documentation
4. The new function automatically appears!

### Experiment 2: Modify Documentation

1. Change the docstring of a function in `analysis.py`
2. Rebuild the documentation
3. The changes appear immediately

### Experiment 3: Add Code Examples

1. Add an Examples section to a docstring with real code
2. Rebuild and view the documentation
3. Notice how examples are formatted nicely

### Experiment 4: Team Collaboration

Imagine different people work on different modules:

- Person A: Documents data_processing.py
- Person B: Documents analysis.py
- Person C: Assembles all documentation in index.rst

Sphinx automatically combines their work into one coherent documentation site!

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Understanding automodule Directives

The directives in `index.rst` are powerful:

```restructuredtext
.. automodule:: data_processing
   :members:
   :undoc-members:
   :show-inheritance:
```

**What this means:**

- `automodule:: data_processing`: Read the module named `data_processing`
- `:members:`: Include all functions and classes (not just the module docstring)
- `:undoc-members:`: Even if a function has no docstring, still document it
- `:show-inheritance:`: For classes, show what they inherit from

**Why this matters:**

Without Sphinx's automodule:

- You'd have to manually copy docstrings into documentation
- Documentation would get out of sync when code changes
- Managing large projects would be impossible

With Sphinx's automodule:

- Documentation stays perfectly in sync with code
- Changes to code automatically update documentation
- Project can have hundreds of functions with maintained documentation

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Real-World Example: Django

The [Django web framework](https://docs.djangoproject.com/) uses this exact approach:

- Hundreds of Python modules organized in packages
- Each module carefully documented with NumPy/Google-style docstrings
- Sphinx automatically generates the full API reference
- Developers trust the documentation is current and accurate

Django project structure is similar to this tutorial:

```
django/
  db/              (database modules)
  forms/           (form handling modules)
  http/            (HTTP handling modules)
  template/        (template rendering modules)
  ...
```

And the Django documentation website shows all of this automatically through Sphinx!

![--- --- --- --- --- --- --- --- ---](../graphics/div_bar.png)

## Summary

In this tutorial you:

1. ✅ Learned why multi-module projects are organized the way they are
2. ✅ Documented multiple Python modules using docstrings
3. ✅ Configured Sphinx to read multiple modules automatically
4. ✅ Generated unified documentation for an entire project
5. ✅ Understood the `automodule` directive and how it powers modern Python documentation
6. ✅ Explored real-world multi-module projects

**Key Insight**: As Python projects grow, Sphinx's ability to automatically assemble documentation from distributed docstrings becomes invaluable. Professional teams rely on this to keep documentation in sync with code.

**Next Step**: Move on to Tutorial 3 to learn advanced customization and professional documentation features!
