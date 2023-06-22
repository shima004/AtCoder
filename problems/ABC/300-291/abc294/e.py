l, n_1, n_2 = map(int, input().split())
v_1, l_1 = [], []
v_2, l_2 = [], []
for i in range(n_1):
    v, _l = map(int, input().split())
    v_1.append(v)
    l_1.append(_l)

for i in range(n_2):
    v, _l = map(int, input().split())
    v_2.append(v)
    l_2.append(_l)

i_1, i_2 = 0, 0
r_1, r_2 = l_1[0], l_2[0]
ans = 0
while True:
    m = min(r_1, r_2)
    if v_1[i_1] == v_2[i_2]:
        ans += max(r_1, r_2) - m
    if r_1 == r_2 and r_1 == l:
        break
    if m == r_1:
        i_1 += 1
        r_1 += l_1[i_1]

    else:
        i_2 += 1
        r_2 += l_2[i_2]


print(ans)
