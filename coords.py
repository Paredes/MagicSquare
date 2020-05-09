
def opposite_coord(coord):
    return coord[::-1]

# get all initial coords possibles that are out of dimensions of matrix
def get_all_init_coords(dimension):
    a = (dimension - 1)//2
    b = dimension + a - 1
    coord_1 = [a,-a]
    coord_2 = [a,b]
    list_coords = []
    for c in [coord_1,coord_2]:
        list_coords.append(c)
        list_coords.append(opposite_coord(c))
    return list_coords





