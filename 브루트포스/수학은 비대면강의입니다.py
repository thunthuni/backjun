a, b, c, d, e, f = map(int, input().split())

denominator = a * e - b * d

x = (c * e - b * f) / denominator
y = (a * f - c * d) / denominator

print(int(x), int(y))

# y = (c*(d/a) - f) / (b*(d/a) - e)
# x = (c - b*y)/a
# print(int(x), int(y))

# ax + by = c
# d + e = f
# ax + by = c
# ax = c - by
# x = (c - by) /a
# a*(d/a) + b*(d/a) = c*(d/a)
# d + e = f

# b*(d/a) - e = c*(d/a) - f
