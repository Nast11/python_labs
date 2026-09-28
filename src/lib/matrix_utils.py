def validate_mat(mat: list[list[float | int]]) -> None:
    if len(mat) == 0:
        return 

    for row in mat:
        if len(row) != len(mat[0]):
            raise ValueError