
def move_disk(from_peg, to_peg):
    print(f"Move disk from {from_peg} to {to_peg}")

def solve_towers_of_hanoi(n, from_peg, to_peg, aux_peg):
    if n == 1:
        move_disk(from_peg, to_peg)
        return
    solve_towers_of_hanoi(n - 1, from_peg, aux_peg, to_peg)
    move_disk(from_peg, to_peg)
    solve_towers_of_hanoi(n - 1, aux_peg, to_peg, from_peg)


num_disks = 5
solve_towers_of_hanoi(num_disks,'A','C','B')