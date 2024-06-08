from mpi4py import MPI
import numpy as np

#Initial data
# SIZE = 6
# JUMP = 3

# ARR = [
#     [1, 5, 45, 87, 34, 87],
#     [7, 13, 75, 18, 63, 34],
#     [87, 45, 96, 13, 8, 6],
#     [24, 98, 45, 87, 36, 7],
#     [5, 6, 17, 54, 24, 98],
#     [4, 8, 87, 87, 678, 974]
#     ]


# ARR = [
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6]
#     ]

SIZE = 24
JUMP = 23

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

    if processes > SIZE:
        print("Too many processes")
        return
    
    if JUMP > SIZE:
        print("Too big jump")
        return

    #Prepare worging array
    row_from_previous_process = np.full((1, SIZE), 0) # last row from previous process in the same block
    data = np.full((SIZE, SIZE), 0) #Dynamic programming array

    # Prepare ranges
    begin_block = int(SIZE/processes*rank)
    block_size = int(SIZE/processes)

    if  (rank == processes - 1) and (block_size * processes != SIZE):
        block_size = SIZE - begin_block
        
    
    current_jump = 0

    print(f"rank {rank}  begin block {begin_block}  block size {block_size}  INDEX: {begin_block + block_size - 1}")

    #Send data by MPI
    while current_jump != SIZE:
        if rank != 0:
            row_from_previous_process = comm.recv(source=rank-1)

        # print(f"ROW: {row_from_previous_process}")

        next_jump = current_jump + JUMP

        if next_jump > SIZE:
            next_jump = SIZE

        #Shortest path in array alghoritm
        for i in range(begin_block, begin_block + block_size):
            for j in range(current_jump, next_jump):

                left = None
                down = None

                if j != 0:
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

        current_jump = next_jump


    if rank == processes - 1:
        print(f"Anwser: {data[SIZE - 1][SIZE - 1]}")





if __name__ == "__main__":
    main()
