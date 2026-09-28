from src.lib.matrix_utils import validate_mat

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

def row_sums(mat: list[list[float | int]]) -> list[float]:
    validate_mat(mat)

    result = []

    for row in mat:
        row_sum = sum(row)
        result.append(row_sum)
    return result

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

if __name__ == "__main__":

    print(transpose([[1, 2, 3]]))
    print(transpose([[1], [2], [3]]))
    print(transpose([[1, 2], [3, 4]]))
    print(transpose([]))
    print(transpose([[1, 2], [3]]))

    # print(row_sums([[1, 2, 3], [4, 5, 6]]))
    # print(row_sums([[-1, 1], [10, -10]]))
    # print(row_sums([[0, 0], [0, 0]]))
    # print(row_sums([[1, 2], [3]]))

    # print(col_sums([[1, 2, 3], [4, 5, 6]]))
    # print(col_sums([[-1, 1], [10, -10]]))
    # print(col_sums([[0, 0], [0, 0]]))
    # print(col_sums([[1, 2], [3]]))