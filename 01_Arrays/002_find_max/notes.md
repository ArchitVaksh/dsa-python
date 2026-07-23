# Find Maximum Element

## Problem

Given an array, return the largest element.

### Example

```python
array = [10, 25, 8, 42, 15]
```

**Output**

```python
42
```

---

## Idea

Assume the first element is the largest and update it whenever a larger element is found.

---

## Algorithm

1. Store the first element as maximum.
2. Traverse the array.
3. Update maximum whenever a larger element is found.
4. Return maximum.

---

## Python Implementation

```python
def find_max(array):
    max_number = array[0]

    for i in range(len(array)):
        if array[i] > max_number:
            max_number = array[i]

    return max_number
```

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(1)**

---

## Key Learning

- Maintaining a running maximum
- One-pass algorithms