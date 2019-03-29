COLOR_ON_FACE = 9
COLOR_CENTER = 4
RAW_SIZE = 3

face_1 = ['R', 'B', 'Y', 'B', 'Y', 'Y', 'O', 'Y', 'R']
face_2 = ['W', 'Y', 'B', 'O', 'R', 'R', 'W', 'W', 'W']
face_3 = ['Y', 'O', 'G', 'B', 'G', 'R', 'O', 'B', 'O']
face_4 = ['Y', 'G', 'B', 'Y', 'O', 'W', 'W', 'R', 'Y']
face_5 = ['B', 'W', 'G', 'G', 'W', 'W', 'R', 'G', 'G']
face_6 = ['G', 'R', 'O', 'G', 'B', 'O', 'B', 'O', 'R']


cube = [face_1, face_2, face_3, face_4, face_5, face_6]


def show_face(face):
    """ Print a face of the cube """
    row = ''
    for (counter, color) in enumerate(face, 1):
        row += color + ' '
        if counter % 3 == 0:
            row += '\n'
    print(row)
    

def show_cube(cube):
    counter = 1
    for face in cube:
        print('--' + str(counter) + '--')
        show_face(face)
        counter += 1


def rotate_faces_to_swap(face_to_rotate, amount):
    """ Change the order of faces (last elements become first) """
    return face_to_rotate[-amount:] + face_to_rotate[:-amount]


def move_bottom(cube, amount):
    cube_aux = cube[:] # slicing obligatoire pour éviter certaines particularités de python
    face_to_swap = [0, 3, 4, 5]
    new_faces = rotate_faces_to_swap(face_to_swap, amount)
    for i in range(len(face_to_swap)):
        cube[face_to_swap[i]] = cube_aux[new_faces[i]]     
    cube[1] = move_clockwise(cube[1], amount)
    cube[3] = move_inverse_clockwise(cube[3], amount)    
    return cube


def move_top(cube, amount):
    return move_bottom(cube, 4 - amount % 4)


def move_right(cube, amount):
    cube_aux = cube[:]
    face_to_swap = [1, 2, 3, 5]   
    new_faces = rotate_faces_to_swap(face_to_swap, amount)   
    if amount != 0:
        cube_aux[5] = move_clockwise(cube_aux[5], 2)    
    for i in range(len(face_to_swap)):
        if i == 3:
            cube[face_to_swap[i]] = move_clockwise(cube_aux[new_faces[i]], 2)
        cube[face_to_swap[i]] = cube_aux[new_faces[i]] 
    cube[0] = move_inverse_clockwise(cube[0], amount)
    cube[4] = move_clockwise(cube[4], amount)   
    return cube


def move_left(cube, amount):
    return move_right(cube, 4 - amount)
    

def move_clockwise(face, amount):
    face_aux = face[:]
    for n in range(amount):
        for i in range(len(face_aux) // 3):
            ray = face_aux[i::3]        
            ray.reverse()
            face[i * 3:(i + 1) * 3] = ray
        face_aux = face[:]
    return face

        
def move_inverse_clockwise(face, amount):
    return move_clockwise(face, 4 - amount)

# Code of all Rubick's cube move (Name of them : https://www.rubiks.com/uploads/blog_entries/8.png)
            
def find_neighboring_slices_face4(cube, neighboring_slices):
    all_slice = []
    for number in neighboring_slices:
        slice_in_face = []
        for i in range(len(cube[int(number) - 1])):
            if (i + 1) % 3 == 0:
                slice_in_face += [cube[int(number) - 1][i]]     
        all_slice += [slice_in_face]
    return all_slice

    
def swap_neighboring_slices_face4_clockwise(cube, neighboring_slices, amount):
    slices_to_swap = find_neighboring_slices_face4(cube, neighboring_slices)
    news_slices = []
    news_slices_end = []
    for (counter, element) in enumerate(slices_to_swap):
        if counter < amount:
            news_slices_end += [element]
        else:
            news_slices += [element]
    return news_slices + news_slices_end


def r(cube, amount):
    neighboring_slices = [0, 2, 4, 5]
    slices_to_change = swap_neighboring_slices_face4_clockwise(cube, neighboring_slices, amount)
    slices_to_change_counter = 0
    for number in neighboring_slices:
        for (counter, i) in enumerate(range(2, len(cube[int(number) - 1]), 3)):
            cube[int(number) - 1][i] = slices_to_change[slices_to_change_counter][counter]
        slices_to_change_counter += 1   
    cube[3] =  move_clockwise(cube[3], amount) 
    return cube


def ri(cube, amount):
    return r(cube, 4 - amount)


def l(cube, amount):
    move_right(cube, 2)
    r(cube, amount)
    move_left(cube, 2)
    return cube


def li(cube, amount):
    move_right(cube, 2)
    ri(cube, amount)
    move_left(cube, 2)
    return cube


def b(cube, amount):
    move_left(cube, 1)
    r(cube, amount)
    move_right(cube, 1)
    return cube


def bi(cube, amount):
    move_left(cube, 1)
    ri(cube, amount)
    move_right(cube, 1)
    return cube


def d(cube, amount):
    move_top(cube, 1)
    move_right(cube, 1)
    r(cube, amount)
    move_left(cube, 1)
    move_bottom(cube, 1)
    return cube


def di(cube, amount):
    move_top(cube, 1)
    move_right(cube, 1)
    ri(cube, amount)
    move_left(cube, 1)
    move_bottom(cube, 1)
    return cube


def f(cube, amount):
    move_right(cube, 1)
    r(cube, amount)
    move_left(cube, 1)
    return cube


def fi(cube, amount):
    move_right(cube, 1)
    ri(cube, amount)
    move_left(cube, 1)
    return cube


def u(cube, amount):
    move_bottom(cube, 1)
    move_right(cube, 1)
    r(cube, amount)
    move_left(cube, 1)
    move_top(cube, 1)
    return cube


def ui(cube, amount):
    move_bottom(cube, 1)
    move_right(cube, 1)
    ri(cube, amount)
    move_left(cube, 1)
    move_top(cube, 1)
    return cube