# A, B, V = map(int, input().split())

# if A == V:
#     print(1)
#
# else:
#     calc = (V - A) // (A - B)
#     if (V-A) <= (A-B):
#         calc += 2
#     else:
#         calc += 1
#     print(calc)

# result = 0
#
# if V % (A - B) == 0:
#     result = V // (A-B) - 1
# else:
#     result = V // (A-B) + 1
#
# print(result)

A, B, V = map(int, input().split())
x = (V-B)/(A-B)
if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)