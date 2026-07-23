# Remove Duplicates from Sorted Array

## Problem

Given a sorted array, remove the duplicates in-place such that each unique element appears only once.

Return the number of unique elements (`k`).

Only the first `k` elements of the array are considered valid.

---

## Approach

Since the array is already sorted, duplicate elements will always be adjacent.

I used the Two Pointer technique:

- One pointer (`i`) traverses the array.
- Another pointer (`k`) keeps track of the position where the next unique element should be placed.
- Whenever a new unique element is found, it is written at index `k`.
- Increment `k`.

---

## Algorithm

1. Handle the empty array.
2. Initialize `k = 1`.
3. Traverse the array.
4. Compare adjacent elements.
5. If they are different:
   - Place the new element at index `k`.
   - Increment `k`.
6. Return `k`.

---

## Time Complexity

O(n)

One traversal of the array.

---

## Space Complexity

O(1)

No extra array is used.

---

## Concepts Learned

- Two Pointer Technique
- In-place Array Modification
- Difference between modifying an object and returning a value
- Why the problem only cares about the first `k` elements

---

## Mistakes Made

Initially I thought duplicate elements had to be physically removed from the array.

Later I realized that only the first `k` elements matter, so overwriting duplicates is enough.

I also learned that Python lists are mutable, so modifying a list inside a function also changes the original list.