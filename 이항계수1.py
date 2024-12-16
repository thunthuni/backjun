import sys

N, K = map(int, sys.stdin.readline().split())

# n! / (n-k)!*k!

n_fact = 1
k_fact = 1
nk_fact = 1
for i in range(N, 0, -1):

    if i <= K:
        k_fact = k_fact * i
    if i <= N-K:
        nk_fact = nk_fact * i

    n_fact = n_fact * i

if K == 0:
    k_fact = 1
    nk_fact = n_fact
print(n_fact//(nk_fact*k_fact))
