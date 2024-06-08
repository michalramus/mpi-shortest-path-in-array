from mpi4py import MPI
import numpy as np

SIZE = 6
JUMP = 2

ARR = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6]
    ]

# data = [
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6]
#     ]

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    processes = comm.Get_size()

    row_from_previous_process = [] # last row from previous process in the same block

    for i in range(0, SIZE):
        row_from_previous_process.append(0)

    data = ARR

    begin_block = int(SIZE/processes*rank)
    block_size = int(SIZE/processes)
    current_jump = 0

    print(f"rank {rank}  begin block {begin_block}  block size sum {block_size + begin_block}")


    while current_jump != SIZE:
        if rank != 0:
            row_from_previous_process = comm.recv(source=rank-1)

        print(f"ROW: {row_from_previous_process}")

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
        
        print("\nrcv")
        print(np.matrix(data))


            # print(f"{i} \n {ARR}\n {data}")
        current_jump = current_jump + JUMP


    if rank == processes - 1:
        print(data[SIZE - 1][SIZE - 1])

            


        # comm.send(data, dest=1, tag=11)




if __name__ == "__main__":
    main()