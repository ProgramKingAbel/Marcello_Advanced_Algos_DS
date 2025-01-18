# Arrays

An **array** is an indexed collection of data.

## Arrays as an Abstract Data Type (ADT)

An array, as an ADT, has the following characteristics:

- **Data Storage**: It stores a collection of data elements.
- **Random Access**: Elements can be accessed directly using their index.
- **Non-Sequential Access**: Elements do not have to be accessed in a specific order.

## Static Arrays: A Concrete Implementation of an ADT

### Memory Allocation
- Arrays are allocated in memory as a single, uninterrupted (contiguous) block of memory with sequential locations. This makes them both memory-efficient and time-efficient.

### Type Restriction
- Arrays are restricted to storing data of the same type. This restriction:
  - Optimizes memory allocation by assigning the same size for each element.
  - Allows the compiler or interpreter to quickly calculate the memory address of any element.

### Fixed Size
- The size of an array (i.e., the number of elements it can contain) must be determined at the time of creation and cannot be changed.

## Dynamic Arrays
- Dynamic arrays are a variant of arrays whose size can change at runtime.
- Some languages, such as Python, natively support dynamic arrays (e.g., lists), which can:
  - Dynamically adjust their size.
  - Store elements of any data type.

## Array Initialization

### 1. Declaration Without Initialization
- Declaring an array without initializing it means no values are explicitly assigned to its elements.
- **Are elements empty in this case?**
  - There is no true concept of "empty." When an array is declared, the compiler must assign a value to each element.
  - The default value depends on the programming language and the array type:
    - In **Java**, an array of `int` will have all elements set to `0`.
    - Some languages assign special values to represent emptiness:
      - **Python**: `None`
      - **Java**: `null`
      - **JavaScript**: `null`

#### Examples of Declaration Without Initialization

##### Java
```java
int[] array = new int[5]; // Array of size 5, all elements initialized to 0
```

##### Python
```python
array = [None] * 5 # Array of size 5, all elements initialized to None
```

##### JavaScript
```javascript
let array = new Array(5); // Array of size 5, all elements initialized to undefined
```

### 2. Declaration with Initialization
- **Initialization**: Assigning values to all elements of the array at the same time it is declared.
- During initialization:
  - The compiler allocates memory for the array.
  - The memory is filled with the specified values during compilation, before moving on to subsequent instructions.

### Example of Initialization

#### Java
```java
int[] array = {1, 2, 3, 4, 5};
```

#### Python
```python
array = [1, 2, 3, 4, 5]
```

#### JavaScript
```javascript
let array = [1, 2, 3, 4, 5];
```
