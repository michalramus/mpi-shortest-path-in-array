from mpi4py import MPI
import numpy as np

#Initial data
# SIZE = 6
# JUMP = 6

# ARR = [
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6]
#     ]


SIZE = 24
JUMP = 4

ARR = [
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 1454],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 234],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 34],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 97],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 23],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 45],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 56],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 1454],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 234],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 34],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 97],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 23],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 45],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 56],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 1454],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 234],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 34],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 1454],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 234],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 34],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 97],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 23],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 45],
    [1, 2, 3, 4, 5, 6, 10, 67, 45, 96, 24, 236, 975, 35684, 85, 1357,86, 3568, 0, 45, 345, 12, 7654, 56]
    ]


def main():
    #Initialize MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    processes = comm.Get_size()

    if int(SIZE/processes) * processes != SIZE:
        print("Incorrect processes count!!!")
        return

    if int(SIZE/JUMP) * JUMP != SIZE:
        print("Incorrect jump count!!!")
        return

    #Prepare worging array
    row_from_previous_process = np.full((1, SIZE), None) # last row from previous process in the same block
    data = np.full((SIZE, SIZE), None) #Dynamic programming array

    # Prepare ranges
    begin_block = int(SIZE/processes*rank)
    block_size = int(SIZE/processes)
    current_jump = 0

    print(f"rank {rank}  begin block {begin_block}  block size {block_size}  INDEX: {begin_block + block_size - 1}")

    #Send data by MPI
    while current_jump != SIZE:
        if rank != 0:
            row_from_previous_process = comm.recv(source=rank-1)

        # print(f"ROW: {row_from_previous_process}")

        #Shortest path in array alghoritm
        for i in range(begin_block, begin_block + block_size):
            for j in range(current_jump, current_jump + JUMP):

                left = None
                down = None

                if i != 0:
                    left = data[i][j - 1]

                if i == 0:
                    down = None
                elif i == begin_block:
                    down = row_from_previous_process[j]
                else:
                    down = data[i - 1][j]


                if (left == None) and (down == None):
                    data[i][j] = ARR[i][j]

                elif left == None:
                    data[i][j] = ARR[i][j] + down

                elif down == None:
                    data[i][j] = ARR[i][j] + left
                
                else:
                    data[i][j] = ARR[i][j] + min(left, down)

        if rank != processes - 1:
            comm.send(obj=data[begin_block + block_size - 1], dest=rank+1)
        
        # print("\nrcv")
        # print(np.matrix(data))

        current_jump = current_jump + JUMP


    if rank == processes - 1:
        print(f"Anwser: {data[SIZE - 1][SIZE - 1]}")





if __name__ == "__main__":
    main()
