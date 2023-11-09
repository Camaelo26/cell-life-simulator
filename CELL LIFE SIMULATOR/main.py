import copy
import argparse
from multiprocessing import Pool
import time
# Record the start time
start_time = time.time()
#argparser = argparse.ArgumentParser()
#argparser.add_argument("-i", type=str, required=True)
#argparser.add_argument("-o", type=str, required=True)
#argparser.add_argument("-p", type=int, default=1)
#args = argparser.parse_args()

def get_neighbor_count(matrix, i, j, row, col):
    count = 0
    neighbor_positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for x_offset, y_offset in neighbor_positions:
        x, y = (i + x_offset) % row, (j + y_offset) % col
        if matrix[x][y] == 'O':
            count += 1

    return count

def new_cell_in_matrix_ruled(args):
    matrix, i, j, row, col = args
    count = get_neighbor_count(matrix, i, j, row, col)

    if matrix[i][j] == 'O' and count in [2, 3, 5, 7]:
        return 'O'
    elif matrix[i][j] == '.' and count in [1, 3, 5, 7]:
        return 'O'
    else:
        return '.'

with open("example1.txt", "r") as file:
    matrix_1 = [list(line.strip()) for line in file.readlines()]

row, col = len(matrix_1), len(matrix_1[0])

for _ in range(100):
    matrix_2 = copy.deepcopy(matrix_1)

    with Pool(2) as pool:
        for i in range(row):
            input_args = [(matrix_1, i, j, row, col) for j in range(col)]
            matrix_2[i] = pool.map(new_cell_in_matrix_ruled, input_args)

    matrix_1 = matrix_2

with open("lopp.txt", "w") as file:
    for line in matrix_1:
        file.write("".join(line) + "\n")



end_time = time.time()

elapsed_time = end_time - start_time

print(f"The code took {elapsed_time} seconds to execute.")