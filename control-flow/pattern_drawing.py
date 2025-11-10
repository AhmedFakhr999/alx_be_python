size = int(input('Enter the size of the pattern: '))
rows = size

while rows > 0:
    cols = size
    while cols > 0:
        print('*', end='')
        cols -= 1
    print()
    rows -= 1