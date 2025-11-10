size = int(input('Enter the size of the pattern: '))
pattern = size
while size > 0:
    print('*' * pattern)  # Use 'pattern' (constant) instead of 'size' (decreasing)
    size -= 1