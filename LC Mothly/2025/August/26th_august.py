# Maximum Area of Longest Diagoal rectangle LC 3000

dimensions=[[9,3],[8,6]]

def areaOfMaxDiagonal(dimensions):
    max_diagonal_length=0
    max_area=0
    for arr in dimensions:
        length,width=arr
        diagonal_length=(length**2 +width**2)**0.5
        if diagonal_length>max_diagonal_length or (diagonal_length==max_diagonal_length and length*width>max_area):
            max_diagonal_length=diagonal_length
            max_area=length*width
    return max_area


print(areaOfMaxDiagonal(dimensions))