# CS101 Python Documentation

Activity 06: Introduction to Sphinx Documentation Library

## Assigned and Due

- **Assigned**: Friday, 27 Feb 2026 at 9:00am
- **Due and Expiration**: Monday, 9 March 2026 at 9:00am (after the break)

Note: the expiration date is the last date you can submit your work for a grade.

<center>

![--- --- --- --- --- --- --- --- ---](graphics/sphinx_400x400.png)

</center>

## Table of Contents
- [CS101 Python Documentation](#cs101-python-documentation)
  - [Assigned and Due](#assigned-and-due)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Learning Objectives](#learning-objectives)
  - [Project Goals](#project-goals)
  - [Instructions](#instructions)
  - [Deliverable](#deliverable)
  - [Submission](#submission)
  - [GatorGrade](#gatorgrade)
  - [Seeking Assistance](#seeking-assistance)

## Overview

In this activity you will complete three tutorials that introduce **Sphinx**, the industry-standard documentation generator for Python projects. Sphinx allows you to write documentation in a simple format (reStructuredText or Markdown) and automatically generates professional HTML documentation from your Python docstrings.

You will use the UV package manager to create project environments and work with Sphinx to:
- Document a simple Python module with docstrings
- Build HTML output from those docstrings
- Extend documentation across multiple modules
- Customize documentation with themes and configuration

By the end of this activity, you will understand why professional teams use Sphinx to maintain clear, organized, and beautiful documentation for their Python projects.

![--- --- --- --- --- --- --- --- ---](graphics/div_bar.png)

## Learning Objectives

By completing this activity, you will be able to:

1. **Understand the importance of source code documentation** and recognize how professional Python projects document their code systematically
2. **Write effective Python docstrings** using standard conventions that Sphinx can parse and render
3. **Build and customize Sphinx projects** to generate professional HTML documentation from Python source code
4. **Configure Sphinx settings** to control documentation appearance, theme selection, and extension behavior
5. **Recognize real-world documentation workflows** by studying how mature Python projects maintain their documentation

![--- --- --- --- --- --- --- --- ---](graphics/div_bar.png)

## Project Goals

This activity guides you through three progressive tutorials:

**Tutorial 1: Introduction to Sphinx and Docstrings**

- [Tutorial_01](sphinx_intro/tutorial_01.md)
  - Learn what Sphinx is and why it matters
  - Write basic docstrings in NumPy format
  - Build your first Sphinx project and generate HTML

**Tutorial 2: Documenting Modules with Multiple Functions**

- [Tutorial_02](sphinx_modules/tutorial_02.md)
  - Extend a Python project with multiple modules
  - Document different types of functions and their parameters
  - Use Sphinx's autodoc extension to automatically include Python docstrings
  - Navigate and understand multi-module documentation

**Tutorial 3: Advanced Sphinx Features**

- [Tutorial_03](sphinx_advanced/tutorial_03.md)
  - Customize themes and appearance
  - Add additional documentation content (guides, examples)
  - Configure advanced Sphinx extensions
  - Build polished, professional documentation

![--- --- --- --- --- --- --- --- ---](graphics/div_bar.png)

## Instructions

1. **Read** each tutorial document ( [Tutorial_01](sphinx_intro/tutorial_01.md), [Tutorial_02](sphinx_modules/tutorial_02.md), [Tutorial_03](sphinx_advanced/tutorial_03.md)) carefully
2. **Follow** the step-by-step instructions in each tutorial
3. **Complete** the TODO items marked in the Python code files
4. **Build** Sphinx documentation and verify the HTML output
5. **Modify** the code and documentation to see how changes affect the output
6. **Answer** the reflection questions in writing/reflection.md

## Deliverable

You will submit:
- Completed Python files with all TODOs resolved for each tutorial
- Built HTML documentation (build/html directories) for each tutorial
- Completed reflection.md with answers to all reflection questions

## Submission

Please submit this assignment by pushing your work to your GitHub repository. Ensure that all code runs correctly and documentation builds successfully.

## GatorGrade

This assignment will be evaluated using GatorGrade. You can check your progress using:

```bash
gatorgrade --config config/gatorgrade.yml
```

## Seeking Assistance

If you have questions or encounter issues:
1. Review the tutorial materials carefully
2. Check Sphinx documentation at https://www.sphinx-doc.org/
3. Consult with your instructor during office hours
4. Post questions in the course discussion forum

---

**Important**: This is your first experience with documentation generators. Take time to understand not just *how* to use Sphinx, but *why* professional developers use tools like this. Good documentation is a sign of professional, maintainable code.
