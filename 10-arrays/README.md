https://neetcode.io/practice

# Arrays & Hasing
## contains duplicate
https://leetcode.com/problems/contains-duplicate/description/

### contains_duplicate1.py
--- solution provided by leetcode

List[int] does not enforce the type of the elements in the list by itself.

Type hints in Python are primarily used for static type checking by tools like mypy or for documentation purposes. They provide guidance to developers and tools about the expected types of variables, function parameters, and return values, but they do not enforce these types at runtime.

Here's what List[int] does:

Documentation and Readability:

The type hint List[int] indicates to developers that the parameter nums should be a list containing integers.
It improves code readability and serves as a form of documentation, making it clear to other developers what kind of input is expected.
Static Type Checking:

Static type checkers like mypy can use type hints to analyze your code and detect potential type-related errors.
If you run mypy on your code, it will raise a type error if you pass a list containing non-integer elements to a function expecting List[int].
No Runtime Enforcement:

However, Python itself does not enforce type hints at runtime. You can still pass lists containing elements of any type to functions expecting List[int], and Python will not raise any errors during execution.
It's up to the developer to add runtime type checking if strict enforcement of types is necessary for the correctness of the program.
In summary, while List[int] provides valuable information about the expected types, it's ultimately the responsibility of the developer to ensure that the code behaves correctly with respect to types, either by adding runtime checks or by relying on static type checkers during development.

### runs on leetcode

#### run 1
Runtime 428 ms (Beats 28.20% of users with Python3)
Memory 31.96 MB (Beats 65.46% of users with Python3)

#### run 2
Runtime: 399 ms (Beats 96.67% of users with Python3)
Memory: 31.26 MB (Beats 91.39% of users with Python3)

#### run 3
Runtime: 416 ms (Beats 61.34% of users with Python3)
Memory: 31.77 MB (Beats 90.80% of users with Python3)

#### run 4
Runtime: 424 ms (Beats 36.99% of users with Python3)
Memory: 31.86 MB (Beats 86.56% of users with Python3)

#### run 5
Runtime: 410 ms (Beats 79.35% of users with Python3)
Memory: 31.80 MB (Beats 90.80% of users with Python3)

