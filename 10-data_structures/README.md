# 1. **Built-in Data Structures**
  
## a. **Lists**
- **Description**: Ordered, mutable collections of elements.
- **Syntax**: `my_list = [1, "hello", 3.14, [2, 3]]`
- **Use Cases**: Storing sequences of items, maintaining order, allowing duplicates.

## b. **Tuples**
- **Description**: Ordered, immutable collections of elements.
- **Syntax**: `my_tuple = (1, "hello", 3.14, [2, 3])`
- **Use Cases**: Storing fixed collections of items, ensuring immutability.


Tuples are a good fit for createing test cases.

### 1. **Immutability**
   - Tuples are immutable, meaning they can’t be accidentally changed. This is useful in test cases because the inputs and expected outputs should remain constant throughout the test.

### 2. **Memory Efficiency**
   - Tuples use less memory compared to lists, so if you have a large number of test cases, using tuples is slightly more efficient.

### 3. **Fixed Structure**
   - Since each test case has exactly three elements (`nums`, `expected_k`, and `expected_nums`), a tuple clearly represents this fixed structure. It signals that the structure of each test case is not intended to vary, which aligns with the immutability property.

### 4. **Convenient Unpacking**
   - Tuples allow for easy unpacking in a loop, like so:

     ```python
    test_cases = [
            # Format: (input array, expected unique count, expected modified array)
            ([1, 1, 2], 2, [1, 2, "_"])
    ]
     for nums, expected_k, expected_nums in test_cases:
         # Run assertions
     ```

This unpacking is especially convenient in tests, as it keeps the code concise and avoids the need for indexing or dictionary keys. 

Of course, you could use lists or dictionaries if you wanted additional flexibility, but tuples are often a simple and effective choice for this structured, fixed data.


#### Important Note

While the tuple itself is immutable, any mutable elements it contains (like lists) can still be modified:

```python
my_tuple[3].append(4)
print(my_tuple)  # Output: (1, 'hello', 3.14, [2, 3, 4])
```

However, attempting to modify the tuple structure itself will raise an error:

```python
my_tuple[0] = 2  # Raises TypeError: 'tuple' object does not support item assignment
```



|                 | **List**       | **Tuple**      |
| --------------- | ---------------| ---------------|
| **Mutability**   | Mutable        | Immutable      |
| **Syntax**       | `[]`           | `()`           |
| **Element types**| Mixed          | Mixed          |


#### c. **Sets**
- **Description**: Unordered collections of unique elements.
- **Syntax**: `my_set = {1, 2, 3}`
- **Use Cases**: Removing duplicates, membership testing, mathematical set operations (union, intersection).

#### d. **Dictionaries**
- **Description**: Unordered collections of key-value pairs.
- **Syntax**: `my_dict = {'a': 1, 'b': 2}`
- **Use Cases**: Associating keys with values, fast lookups by key.

In Python, dictionaries (`dict`) use a hash table to store key-value pairs, allowing for efficient retrieval of values based on their keys. Here’s a breakdown of how hashing works within a Python dictionary:

1. **Hashing the Key**:
   When a key-value pair is added to a dictionary, Python computes a hash value for the key using Python's built-in `hash()` function. This hash is an integer that uniquely identifies the key within the dictionary. The hash value determines where the key-value pair will be stored in the dictionary’s internal structure.

2. **Determining the Index**:
   The dictionary uses the hash value to find an index (or "bucket") in its internal hash table where the key-value pair can be stored. The hash value is converted into an index by applying a modulo operation (e.g., `hash % table_size`). This maps the hash value to a specific slot in the underlying table.

3. **Handling Collisions**:
   If two keys have the same hash or map to the same index, this is called a "collision." Python handles collisions using "open addressing" with a method called "probing." When a collision occurs, the dictionary tries the next available slot in the hash table until it finds an empty one. This ensures each key remains unique within the dictionary.

4. **Retrieving Values**:
   When a value is accessed, the dictionary computes the hash of the given key, uses it to locate the index, and retrieves the value associated with that key. If there’s a collision, the dictionary checks subsequent slots as needed.

5. **Rehashing for Growth**:
   As more entries are added and the hash table fills up, Python will automatically resize and rehash the dictionary to maintain efficient access times.

```python
d = {"key1": "value1", "key2": "value2"}
```
Python will compute the hash values for `"key1"` and `"key2"`, map them to specific locations in the internal table, and store `"value1"` and `"value2"` accordingly. When you access `d["key1"]`, Python recomputes the hash of `"key1"`, finds its position in the table, and returns `"value1"`.

# 2. **Additional Data Structures**

#### a. **Strings**
- **Description**: Immutable sequences of characters.
- **Syntax**: `my_string = "Hello, World!"`
- **Use Cases**: Text manipulation, storing character data.

### 3. **Data Structures from the `collections` Module**
Python’s `collections` module provides additional data structures that enhance the capabilities of built-in types:

#### a. **NamedTuple**
- **Description**: Like a tuple, but with named fields.
- **Use Cases**: Creating simple classes for storing data without the boilerplate of a full class definition.

#### b. **deque**
- **Description**: A double-ended queue that allows append and pop operations from both ends.
- **Syntax**: `from collections import deque; my_deque = deque([1, 2, 3])`
- **Use Cases**: Implementing queues and stacks efficiently.

#### c. **Counter**
- **Description**: A dictionary subclass for counting hashable objects.
- **Syntax**: `from collections import Counter; my_counter = Counter(['a', 'b', 'a'])`
- **Use Cases**: Counting occurrences of elements.

#### d. **OrderedDict**
- **Description**: A dictionary that maintains the order of keys based on insertion.
- **Use Cases**: When the order of entries is important.

#### e. **defaultdict**
- **Description**: A dictionary that provides a default value for non-existent keys.
- **Syntax**: `from collections import defaultdict; my_defaultdict = defaultdict(int)`
- **Use Cases**: Simplifying code that needs to initialize keys with default values.

### 4. **Array**
While not built-in, you can use the `array` module for creating arrays of numeric types.
- **Syntax**: `from array import array; my_array = array('i', [1, 2, 3])`
- **Use Cases**: Efficiently storing large arrays of numeric data.

### 5. **Custom Data Structures**
You can create your own data structures using classes and other built-in types to suit specific needs, such as linked lists, stacks, queues, trees, and graphs.

### Conclusion
Python’s built-in data structures provide flexibility and efficiency for a wide range of programming tasks. Choosing the appropriate data structure is key to optimizing performance and code readability.

## Enumerate

The `enumerate` function in Python is specifically designed for use with **iterable** data structures. While it works with a wide variety of common data types, it does not apply universally to all data structures. Here’s a breakdown of where `enumerate` can be used effectively:

### 1. **Common Iterables Where `enumerate` Works:**
- **Lists**: You can enumerate over lists easily.
    ```python
    my_list = ['a', 'b', 'c']
    for index, value in enumerate(my_list):
        print(index, value)  # Output: (0, 'a'), (1, 'b'), (2, 'c')
    ```

- **Tuples**: Enumerate works the same way with tuples.
    ```python
    my_tuple = (1, 2, 3)
    for index, value in enumerate(my_tuple):
        print(index, value)  # Output: (0, 1), (1, 2), (2, 3)
    ```

- **Strings**: Enumerate can be used with strings, where each character is treated as an element.
    ```python
    my_string = "hello"
    for index, char in enumerate(my_string):
        print(index, char)  # Output: (0, 'h'), (1, 'e'), etc.
    ```

- **Sets**: While sets are unordered collections, you can still use `enumerate`, but the order of elements will be arbitrary.
    ```python
    my_set = {1, 2, 3}
    for index, value in enumerate(my_set):
        print(index, value)  # Order may vary
    ```

- **Dictionaries**: You can enumerate over the keys, values, or items (key-value pairs) of a dictionary.
    ```python
    my_dict = {'a': 1, 'b': 2}
    for index, key in enumerate(my_dict):  # Enumerate over keys
        print(index, key)  # Output: (0, 'a'), (1, 'b')

    for index, (key, value) in enumerate(my_dict.items()):  # Enumerate over items
        print(index, key, value)  # Output: (0, 'a', 1), (1, 'b', 2)
    ```

### 2. **Data Structures Where `enumerate` Cannot Be Used:**
- **Non-iterable Objects**: 
    - Any object that does not implement the iterable protocol (i.e., it does not have `__iter__()` defined) cannot be enumerated.
    - Examples include integer, float, and NoneType.
    ```python
    num = 10
    # This will raise a TypeError
    # for index, value in enumerate(num):
    #     print(index, value)
    ```

### 3. **Custom Objects**:
If you create a custom object, it can be made iterable by defining the `__iter__()` method. Once it is iterable, you can use `enumerate` on it.

```python
class MyIterable:
    def __iter__(self):
        return iter([1, 2, 3, 4])

my_iterable = MyIterable()
for index, value in enumerate(my_iterable):
    print(index, value)  # Output: (0, 1), (1, 2), (2, 3), (3, 4)
```

### Conclusion:
In summary, `enumerate` applies to any **iterable** data structure in Python, including lists, tuples, strings, sets, and dictionaries. It does not apply to non-iterable types (like integers) or custom objects unless they implement the iterable protocol.

Yes, **arrays** are a data structure in Python, but they are not as commonly used as lists. Here’s an overview of arrays in Python:

### 1. **Array Module**
Python provides an `array` module that allows you to create arrays, which are similar to lists but are more efficient for numerical data.

- **Importing the Module**:
  ```python
  from array import array
  ```

- **Creating an Array**:
  You can create an array by specifying the type code, which indicates the type of elements it will hold (e.g., `'i'` for integers, `'f'` for floats).
  ```python
  my_array = array('i', [1, 2, 3, 4])  # 'i' indicates an array of integers
  ```

- **Example**:
  ```python
  from array import array

  # Create an array of integers
  int_array = array('i', [1, 2, 3, 4, 5])
  print(int_array)  # Output: array('i', [1, 2, 3, 4, 5])

  # Accessing elements
  print(int_array[0])  # Output: 1

  # Appending an element
  int_array.append(6)
  print(int_array)  # Output: array('i', [1, 2, 3, 4, 5, 6])
  ```

### 2. **Key Characteristics of Arrays**
- **Type Restriction**: Arrays are homogeneous, meaning they can only contain elements of the same type. This is enforced by the type code you specify.
- **Performance**: Arrays can be more memory-efficient than lists when dealing with large amounts of numerical data, as they store data more compactly.
- **Less Flexible**: Unlike lists, which can store mixed types, arrays are less flexible because they require a specific data type.

### 3. **NumPy Arrays**
For more advanced numerical operations and to handle large datasets efficiently, many Python developers use **NumPy**, a powerful library that provides support for multi-dimensional arrays and matrices.

- **Installing NumPy**:
  You can install NumPy using pip:
  ```bash
  pip install numpy
  ```

- **Creating a NumPy Array**:
  ```python
  import numpy as np

  # Create a NumPy array
  np_array = np.array([1, 2, 3, 4, 5])
  print(np_array)  # Output: [1 2 3 4 5]
  ```

### Conclusion
In summary, arrays are indeed a data structure in Python, primarily available through the `array` module, which is suitable for numerical data. For more extensive and advanced array operations, the NumPy library is often used due to its enhanced capabilities and performance.