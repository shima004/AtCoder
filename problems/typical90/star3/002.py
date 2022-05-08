N = int(input())
bin = 0b0
for i in range(2 ** N):
    ans = ""
    count = 0
    for j in range(N-1, -1, -1):
        if bin >> j & 1:
            ans += ")"
        else:
            ans += "("
    for j in range(N):
        if ans[j] == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            break
        if count == 0 and j == N-1:
            print(ans)
    bin += 1
