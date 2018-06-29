
import pprint

def isFull(square):
    for value in square:
        if 0 in value:
            return False
    return True


acum = 2
cont = 1

posibilities = [[-2, 1], [-2, -1], [-1, -2], [-1, 2], [2, 1], [2, -1], [1, 2], [1, -2]]



def valid_positions(square, x, y):
    base2 = {}
    basefinal = {}

    temp = []

    for value in posibilities:
        x_c = value[0]
        y_c = value[1]


        if (x + x_c >= 0 and x + x_c <= 7) and (y + y_c >= 0 and y + y_c <= 7) and square[x + x_c][y + y_c] == 0:

            temp.append([x + x_c, y + y_c ])

        base2[(x,y)] =  {'positions' : temp,
                         'number': len(temp)}

    return base2





def make_movement(square, x, y):
    global acum
    global cont

    if (x - 2 >= 0 and x - 2 <= 7) and (y + 1 >= 0 and y + 1 <= 7) and square[x - 2][y + 1] == 0:
        square[x - 2][y + 1] = acum
        acum = acum + 1

        row = square.index(square[x - 2])
        column = square[x - 2].index(square[x - 2][y + 1])

        cont = cont + 1
        make_movement(square, row, column)

    if (x - 2 >= 0 and x - 2 <= 7) and (y - 1 >= 0 and y - 1 <= 7) and square[x - 2][y - 1] == 0:
        square[x - 2][y - 1] = acum
        acum = acum + 1

        row = square.index(square[x - 2])
        column = square[x - 2].index(square[x - 2][y - 1])

        cont = cont + 1
        make_movement(square, row, column)

    if (x - 1 >= 0 and x - 1 <= 7) and (y + 2 >= 0 and y + 2 <= 7) and square[x - 1][y + 2] == 0:
        square[x - 1][y + 2] = acum
        acum = acum + 1
        cont = cont + 1
        row = square.index(square[x - 1])
        column = square[x - 1].index(square[x - 1][y + 2])

        make_movement(square, row, column)

    if (x - 1 >= 0 and x - 1 <= 7) and (y - 2 >= 0 and y - 2 <= 7) and square[x - 1][y - 2] == 0:
        square[x - 1][y - 2] = acum
        acum = acum + 1
        cont = cont + 1
        row = square.index(square[x - 1])
        column = square[x - 1].index(square[x - 1][y - 2])

        make_movement(square, row, column)

    if (x + 1 >= 0 and x + 1 <= 7) and (y - 2 >= 0 and y - 2 <= 7) and square[x + 1][y - 2] == 0:
        square[x + 1][y - 2] = acum
        acum = acum + 1
        cont = cont + 1
        row = square.index(square[x + 1])
        column = square[x + 1].index(square[x + 1][y - 2])

        make_movement(square, row, column)

    if (x + 1 >= 0 and x + 1 <= 7) and (y + 2 >= 0 and y + 2 <= 7) and square[x + 1][y + 2] == 0:
        square[x + 1][y + 2] = acum
        acum = acum + 1
        cont = cont + 1
        row = square.index(square[x + 1])
        column = square[x + 1].index(square[x + 1][y + 2])

        make_movement(square, row, column)
    if (x + 2 >= 0 and x + 2 <= 7) and (y + 1 >= 0 and y + 1 <= 7) and square[x + 2][y + 1] == 0:
        square[x + 2][y + 1] = acum
        acum = acum + 1
        cont = cont + 1
        row = square.index(square[x + 2])
        column = square[x + 2].index(square[x + 2][y + 1])

        make_movement(square, row, column)

    if (x + 2 >= 0 and x + 2 <= 7) and (y - 1 >= 0 and y - 1 <= 7) and square[x + 2][y - 1] == 0:
        square[x + 2][y - 1] = acum
        acum = acum + 1
        cont = cont + 1
        row = square.index(square[x + 2])
        column = square[x + 2].index(square[x + 2][y - 1])

        make_movement(square, row, column)

    return square





def validate_number(x,y,square):
    base2 = valid_positions(square, x, y)

    temp2 = []
    for coorde, numbers in base2.items():
        for array in numbers['positions']:
            temp2.append(valid_positions(square, array[0], array[1]))

    pprint.pprint(temp2)
    # print(validate_number(square,x,y,a))


if '__main__' == __name__:

    num = 8
    square = []

    for a in range(0, num):
        square.append([])

    for val in square:
        for a in range(0, num):
            val.append(0)


    # INSERTE LAS COORDENADAS
    x = 4
    y = 4

    square[x][y] = 1




    square = make_movement(square, x, y)

    for val in square:
        print(val)

    print("Numero de movimientos:", cont)
    

    """
    validate_number(x,y,square)

    for val in square:
        print(val)
        
    """




