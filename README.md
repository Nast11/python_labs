# Лабораторная работа 2
## Задание 1
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError

    minimum = min(nums)
    maximum = max(nums)

    return minimum, maximum
```
![скрин 1](images/lab02/img1.1.png)

```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:

    result = sorted(set(nums))

    return result
```
![скрин 2](images/lab02/img1.2.png)

```python
def flatten(mat: list[list | tuple]) -> list:

    result = []

    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError

        result.extend(row)

    return result
```
![скрин 3](images/lab02/img1.3.png)

## Задание 2
```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    validate_mat(mat)

    if len(mat) == 0:
        return []
    
    result = []

    row_count = len(mat)
    column_count = len(mat[0])

    for i in range(column_count):
        new_row = []
        for j in range(row_count):
            element = mat[j][i]
            new_row.append(element)
        result.append(new_row)
    return result
```
![скрин 1](images/lab02/img2.1.png)

```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    validate_mat(mat)

    result = []

    for row in mat:
        row_sum = sum(row)
        result.append(row_sum)
    return result
```
![скрин 2](images/lab02/img2.2.png)

```python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    validate_mat(mat)

    if len(mat) == 0:
        return []

    result = []

    column_count = len(mat[0])

    for column_index in range(column_count):
        column_sum = 0
        for row in mat:
            column_sum += row[column_index]
        result.append(column_sum)
    return result
```
![скрин 3](images/lab02/img2.3.png)




