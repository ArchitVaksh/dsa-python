# Check if Array is Sorted

## Problem

Determine whether an array is sorted in non-decreasing order.

### Example

```python
array = [1,2,3,4]
```

Output

```python
True
```

---

## Idea

Compare every element with its next element. If any element is larger than the next one, the array is not sorted.

---

## Algorithm

1. Traverse until the second last element.
2. Compare adjacent elements.
3. Return `False` if any pair is out of order.
4. Otherwise return `True`.

---

## Python Implementation

```python
def is_sorted(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True
```

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(1)**

---

## Key Learning

- Adjacent comparisons
- Early termination