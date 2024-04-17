h, m = map(int, input().split())
minute = m - 45
h_ans = 0
m_ans = 0
if minute < 0:
    h_ans = h - 1
    if h_ans == -1:
        h_ans = 23
    m_ans = 60 + minute
else:
    h_ans = h
    m_ans = minute

print(h_ans, m_ans)