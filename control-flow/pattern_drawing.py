size = int(input('Enter the size of the pattern: '))

for i in range(size):          # Outer loop for rows
    for j in range(size):      # Inner loop for columns
        print('*', end='')     # Print each star without newline
    print()                    # New line after each row