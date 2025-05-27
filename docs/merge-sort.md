# Merge Sort

## Problem Description
Merge Sort is a divide-and-conquer algorithm that divides the input array into two halves, recursively sorts them, and then merges the sorted halves.

### Input
- A list of numbers to be sorted
- Constraints: Can handle any valid list of comparable elements

### Output
- A sorted list of numbers in ascending order

## Algorithm Design

### Approach: Recursive Merge Sort
#### Process
1. Divide the unsorted list into two sublists of about half the size
2. Recursively sort each sublist
3. Merge the two sorted sublists back into one sorted list

#### Complexity Analysis
- Time Complexity: O(n log n)
  - Dividing the array takes O(1) time
  - We divide the array log n times (depth of recursion tree)
  - Merging takes O(n) time at each level
  - Total: O(n log n)
- Space Complexity: O(n)
  - We need O(n) extra space for the temporary arrays during merging

## Examples
```
Input: [3, 2, 1, 5, 4]
Output: [1, 2, 3, 4, 5]

Input: []
Output: []

Input: [42]
Output: [42]

Input: [3, -1, 0, 2, -2, 1]
Output: [-2, -1, 0, 1, 2, 3]
```

## Implementation Notes
- The implementation creates a copy of the input list to avoid modifying the original
- The main function delegates to helper functions that implement the recursive algorithm
- The merge operation uses temporary arrays to store the two halves being merged

## References
- [Merge Sort - Wikipedia](https://en.wikipedia.org/wiki/Merge_sort)
- Time Complexity: O(n log n) in all cases (best, average, worst)
- Space Complexity: O(n)
