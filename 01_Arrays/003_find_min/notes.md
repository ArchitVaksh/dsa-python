# Find Minimum Element

## Problem

Given an array, return the smallest element.

### Example

```python
array = [10, 25, 8, 42, 15]
```

**Output**

```python
8
```

---

## Idea

Assume the first element is the minimum and update it whenever a smaller element is found.

---

## Algorithm

1. Store the first element as minimum.
2. Traverse the array.
3. Update minimum whenever a smaller element is found.
4. Return minimum.

---

## Python Implementation

```python
def find_min(array):
    min_number = array[0]

    for i in range(len(array)):
        if array[i] < min_number:
            min_number = array[i]

    return min_number
```

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(1)**

---

## Key Learning

- Running minimum
- One-pass traversal