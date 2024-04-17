N = int(input())
for i in range(1, 2*N, 2):
    print(' '*(N-i//2-1), end='')
    print('*'*i)
for j in range(2*N-3, 0, -2):
    print(' ' * (N - j // 2 - 1), end='')
    print('*' * j)