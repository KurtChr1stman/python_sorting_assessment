# Package Sorting System

This is my solution for the Thoughtful robotic automation factory challenge.

## What it does

The program sorts packages into three stacks based on size and weight:

* **STANDARD**: Normal packages
* **SPECIAL**: Heavy OR bulky packages
* **REJECTED**: Both heavy AND bulky packages

A package is considered:
- **Bulky**: Volume ≥ 1,000,000 cm³ or any dimension ≥ 150 cm
- **Heavy**: Mass ≥ 20 kg

## Files

- `package_sorting.py`: Main sorting function
- `test_package_sorting.py`: Tests to verify everything works

## How to use it

```python
from package_sorting import sort

# Example: A normal package
sort(50, 50, 50, 10)  # Returns "STANDARD"

# Example: A heavy package
sort(50, 50, 50, 25)  # Returns "SPECIAL"
```

## Running tests

```
py -m unittest test_package_sorting.py
```

I made sure to handle edge cases like packages that are exactly at the threshold values.
