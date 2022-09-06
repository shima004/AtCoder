H1, H2, H3, W1, W2, W3 = map(int, input().split())

ans = 0
for h1w1 in range(1, H1-1):
    for h2w1 in range(1, H2-1):
        for h1w2 in range(1, H1 - h1w1, ):
            for h2w2 in range(1, H2 - h2w1):
                h1w3 = H1 - h1w1 - h1w2
                h2w3 = H2 - h2w1 - h2w2
                h3w1 = W1 - h1w1 - h2w1
                h3w2 = W2 - h1w2 - h2w2
                h3w3 = W3 - h1w3 - h2w3
                if h3w1 > 0 and h3w2 > 0 and h3w3 > 0 and h3w1 + h3w2 + h3w3 == H3:
                    ans += 1

print(ans)
