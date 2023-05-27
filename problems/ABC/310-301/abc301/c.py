s = input()
t = input()
s_alpha = [0] * 26
t_alpha = [0] * 26

s_a = s.count("@")
t_a = t.count("@")
s = s.replace("@", "")
t = t.replace("@", "")

replacable = [ord("a"), ord("t"), ord("c"), ord("o"), ord("d"), ord("e"), ord("r")]
for i in range(len(replacable)):
    replacable[i] -= ord("a")

for i in range(len(s)):
    s_alpha[ord(s[i]) - ord("a")] += 1

for i in range(len(t)):
    t_alpha[ord(t[i]) - ord("a")] += 1

diff = [0] * 26
for i in range(26):
    diff[i] = s_alpha[i] - t_alpha[i]


flag = True
for i in range(26):
    if i in replacable:
        continue
    if diff[i] != 0:
        flag = False
        break

if not flag:
    print("No")
else:
    s_replace = 0
    t_replace = 0
    for i in replacable:
        if diff[i] < 0:
            s_replace += abs(diff[i])
        elif diff[i] > 0:
            t_replace += abs(diff[i])

    if s_replace > s_a or t_replace > t_a:
        print("No")
    else:
        print("Yes")
