# Python-Utils
A couple of functions that are must-haves in Python.

# Clear
Clear the entire console, optimized for Windows, Linux, Mac, and PyCharm terminal.

```python
from Python-Utils.Clear import clear
```

```python
clear()        # uses os.system("cls"/"clear")
clear(space=20) # PyCharm fallback: prints N blank lines instead
```

# Math Functions
A collection of helpful mathematical functions.

```python
from Python-Utils.MathFuncs import *
```

### `factorial(n: int) -> int`
Computes n! = 1 × 2 × ... × n iteratively.

### `T(n: int) -> int`
Returns the n-th triangular number: T(n) = Σᵢ₌₁ⁿ i = n(n+1)/2.

### `root(n, type=2)`
Computes the `type`-th root of `n`, i.e. n^(1/type). Type defaults to 2 (square root).

### `average(nums: list) -> float`
Returns the arithmetic mean of a list of numbers: (Σ nums) / len(nums).

### `median(nums: list)`
Returns the middle element of the list by index. Note: list should be
sorted beforehand for a statistically correct median.

# Random String
A random string generator.

```python
from Python-Utils.RandomStrings import rand_strings_generator
```

```python
rand_strings_generator(length) # length is an integer
```

# Change Int System
Convert integers between numeral systems using the generic `to_system()` converter.

```python
from Python-Utils.changeIntSystem import *
```

### `to_system(sys: int, n: int) -> str`
Converts decimal integer `n` to base `sys`, returning it as a string.

### `from_system(sys: int, n: str) -> int`
Converts a base-`sys` string representation back to a decimal integer
using Horner's method in O(k) where k = len(n).

## Examples
```python
to_system(2, 10)        # "1010"
to_system(3, 10)        # "101"
from_system(2, "1010")  # 10
```
