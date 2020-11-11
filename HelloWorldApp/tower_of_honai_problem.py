
def print_move(fr, to):
    print(f'move from {fr} to {to}')


def start_move(n, fr, to, spare):
    if n == 1:
        print_move(fr,to)
    else:
        start_move(n-1, fr, spare, to)
        start_move(1, fr, to, spare)
        start_move(n-1, spare, to, fr)

# example for calling
# start_move(1, 'p1', 'p2', 'p3')