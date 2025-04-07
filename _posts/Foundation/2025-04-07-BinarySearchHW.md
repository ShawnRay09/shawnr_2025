---
layout: post
title: Binary Search HW
description: 
type: issues
comments: True
---

## Homework Hack 1

```python
arr = [4, 5, 6, 7, 0, 1, 2]
target = 1

```

```python
def search_rotated_array(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

```python
Output: 5
```

## Homework Hack 2

```python
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
```

```python
def find_first_last(arr, target):
    def find_bound(is_first):
        left, right = 0, len(arr) - 1
        bound = -1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                bound = mid
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return bound

    first = find_bound(True)
    last = find_bound(False)

    return (first, last) if first != -1 else -1
```

```python
Output: (1, 3)
```

## Homework Hack 3

```python
arr = [1, 3, 5, 7, 9, 11]
target = 8
```

```python
def smallest_ge(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            result = arr[mid]
            right = mid - 1
        else:
            left = mid + 1

    return result
```

```python
Output: 9
```