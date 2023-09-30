def main():
    # 入力の取得
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    b = [input() for _ in range(h)]

    # 初期状態と一致する場合
    if a == b:
        print("Yes")
        return

    for i in range(h):
        for j in range(w):
            flag = True
            for k in range(h):
                for l in range(w):
                    if a[(k + i) % h][(l + j) % w] != b[k][l]:
                        flag = False
                        break
            if flag:
                print("Yes")
                return
    print("No")


if __name__ == "__main__":
    main()
