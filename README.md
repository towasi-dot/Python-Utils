# Python-Utils
A couple of functions that are must-haves in Python.

# Clear
Just clear the entire console by using this function (optimazed for Windows, Linux, Mac, and PyCharm terminal).

Just type 
```Python
from Python-Utils.Clear import clear
```
and then 
```Python
clear()
```
to use it

# Math Functions
It's exactly what you think, a couple of helpfull mathematical functions:
1. Factorial (`factorial(n)`) - normal factorial.
2. `T(n)` - triangular numbers.
3. Root (`root(n, type)`, type is 2 by default) - root.
4. Average (`average(numbers)`, numbers should be a list of intigers) - it just counts the arythmetical average of all numbers in list.

Just type
```Python
from Python-Utils.MathFuncs import *
```
and then run the chosen function

# Random string
It is just a random string generator 

Just type 
```Python
from Python-Utils.RandomStrings import rand_strings_generator
```
and to run just type 
```Python
rand_strings_generator(lenght) # lenght is an intiger so choose lenght
```
# Change Int System
Convert integers between numeral systems using the generic `to_system()` converter.

## Usage
```python
from Python-Utils.changeIntSystem import *
```

## Functions

### `to_system(sys: int, n: int) -> str`
Converts decimal integer `n` to base `sys`, returning it as a string.

### `from_system(sys: int, n: str) -> int`
Converts a base-`sys` string representation back to a decimal integer
using Horner's method in O(k) where k = len(n).
