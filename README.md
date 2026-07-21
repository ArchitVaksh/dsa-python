# Arrays

This folder contains my implementations of fundamental array algorithms in Python. These problems are helping me build a strong foundation in Data Structures and Algorithms.

---

# Algorithms Completed

- Linear Search
- Find Maximum Element
- Find Minimum Element
- Check if Array is Sorted

---

# 1. Linear Search

## Idea

Traverse the array one element at a time until the target is found.

## Algorithm

1. Start from the first element.
2. Compare each element with the target.
3. If found, return its index.
4. If the loop ends, return `-1`.

### Time Complexity

- Best Case: **O(1)**
- Average Case: **O(n)**
- Worst Case: **O(n)**

### Space Complexity

- **O(1)**

---

# 2. Find Maximum Element

## Idea

Assume the first element is the maximum, then compare it with every other element.

## Algorithm

1. Assume the first element is the maximum.
2. Traverse the array.
3. If a larger element is found, update the maximum.
4. Return the maximum element.

### Time Complexity

- Best Case: **O(n)**
- Average Case: **O(n)**
- Worst Case: **O(n)**

### Space Complexity

- **O(1)**

---

# 3. Find Minimum Element

## Idea

Assume the first element is the minimum, then compare it with every other element.

## Algorithm

1. Assume the first element is the minimum.
2. Traverse the array.
3. If a smaller element is found, update the minimum.
4. Return the minimum element.

### Time Complexity

- Best Case: **O(n)**
- Average Case: **O(n)**
- Worst Case: **O(n)**

### Space Complexity

- **O(1)**

---

# 4. Check if Array is Sorted

## Idea

Compare every element with its next element. If any element is greater than the next one, the array is not sorted.

## Algorithm

1. Traverse the array from the first element to the second last element.
2. Compare the current element with the next element.
3. If the current element is greater than the next one, return `False`.
4. If the loop finishes without finding any violation, return `True`.

### Time Complexity

- Best Case: **O(1)** *(when the first pair is unsorted)*
- Average Case: **O(n)**
- Worst Case: **O(n)**

### Space Complexity

- **O(1)**

---

# 5. Reverse an Array

## Idea

Use two pointers: one starting from the beginning of the array and the other from the end. Swap the elements at both pointers and move them toward each other until they meet.

## Algorithm

1. Initialize `left` to the first index.
2. Initialize `right` to the last index.
3. Swap the elements at `left` and `right`.
4. Increment `left` and decrement `right`.
5. Repeat until `left` is greater than or equal to `right`.
6. Return the reversed array.

### Time Complexity

- Best Case: **O(n)**
- Average Case: **O(n)**
- Worst Case: **O(n)**

### Space Complexity

- **O(1)**

---

# 6. Second Largest Element

## Problem

Given an array of integers, find the **second largest distinct element**.

### Example

```python
array = [10, 5, 20, 8, 15]
```

**Output:**

```python
15
```

Another example:

```python
array = [5, 5, 3, 2]
```

**Output:**

```python
3
```

---

## Idea

Traverse the array only once while maintaining two variables:

- `largest` – Stores the largest element found so far.
- `second_largest` – Stores the second largest distinct element found so far.

Whenever a new largest element is found:
- The previous largest becomes the second largest.
- The current element becomes the new largest.

Otherwise, if the current element is greater than the second largest but different from the largest, update the second largest.

---

## Algorithm

1. Initialize `largest` and `second_largest` to negative infinity.
2. Traverse each element of the array.
3. If the current element is greater than `largest`:
   - Assign `largest` to `second_largest`.
   - Update `largest` with the current element.
4. Otherwise, if the current element is different from `largest` and greater than `second_largest`:
   - Update `second_largest`.
5. Return `second_largest`.
6. If no distinct second largest element exists, return `None`.

---

## Time Complexity

**O(n)**

The array is traversed only once.

---

## Space Complexity

**O(1)**

Only two extra variables are used regardless of the size of the array.

# 7. Move All Zeros to the End

## Problem

Given an array, move all the `0`s to the end while maintaining the relative order of the non-zero elements.

### Example

```python
array = [0, 1, 0, 3, 12]
```

**Output:**

```python
[1, 3, 12, 0, 0]
```

---

## Idea

Use two pointers:

- `index` keeps track of the position where the next non-zero element should be placed.
- Traverse the array from left to right.
- Whenever a non-zero element is found, swap it with the element at `index` and increment `index`.

This moves all non-zero elements to the front while naturally shifting all zeros to the end.

---

## Algorithm

1. Initialize `index` to `0`.
2. Traverse the array.
3. If the current element is not `0`:
   - Swap it with `array[index]`.
   - Increment `index`.
4. Continue until all elements are processed.
5. Return the modified array.

---

## Time Complexity

**O(n)**

The array is traversed only once.

---

## Space Complexity

**O(1)**

The array is modified in place without using any extra data structures.