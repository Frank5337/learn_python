for i in range(5):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(5):
    for _ in range(4 - i):
        print(' ', end='')
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(5):
    for _ in range(4 - i):
        print(' ', end='')
    for _ in range((i + 1) * 2 - 1):
        print('*', end='')
    print()

for i in range(5):
    print(' ' * (4 - i), end='')
    print('*' * ((i + 1) * 2 - 1), end='')
    print()
