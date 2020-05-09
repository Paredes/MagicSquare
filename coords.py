
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

# up_right = -1,1 up_left = -1,-1 down_right = 1,1 down_left = 1,-1
def get_directions(
        dim, init_coord):
    directions = [[-1,1], [-1,-1], [1,1], [1,-1]]
    if init_coord in get_all_init_coords(dim):
        if init_coord[0] < 0:
            return [c for c in directions if c[0] == 1]
        elif init_coord[1] < 0:
            return [c for c in directions if c[1] == 1]
        elif init_coord[0] < init_coord[1]:
            return [c for c in directions if c[1] == -1]
        elif init_coord[0] > init_coord[1]:
            return [c for c in directions if c[0] == -1]
        else:
            return []
    else:
        return []

t = get_all_init_coords(5)
print(t[0])
print(get_directions(5,t[0]))




