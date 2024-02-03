def main(s):
    remain = [1] * len(s)
    st = 0
    end = -1
    f = False
    while True:
        try:
            print(
                "".join([s[i] if remain[i] == 1 else " " for i in range(len(s))]),
                st,
                end,
                f,
            )
            if f and end >= 0:
                if (
                    end - 1 >= 0
                    and s[end - 1] == "A"
                    and s[end] == "B"
                    and s[st] == "C"
                ):
                    remain[end - 1] = 0
                    remain[end] = 0
                    remain[st] = 0
                    st += 1
                    end -= 2
                    f = True
                elif s[end] == "A" and s[st] == "B" and s[st + 1] == "C":
                    remain[end] = 0
                    remain[st] = 0
                    remain[st + 1] = 0
                    st += 2
                    end -= 1
                    f = True
                else:
                    f = False
            else:
                if s[st] == "A" and s[st + 1] == "B" and s[st + 2] == "C":
                    remain[st] = 0
                    remain[st + 1] = 0
                    remain[st + 2] = 0
                    st += 3
                    if end == -1:
                        end = st - 4
                    f = True
                else:
                    st += 1
        except IndexError:
            break
    return "".join([s[i] if remain[i] == 1 else "" for i in range(len(s))])


def check(s):
    for i in range(len(s) - 2):
        if s[i] == "A" and s[i + 1] == "B" and s[i + 2] == "C":
            print(i)
            return True
    return False


def randTest():
    import random

    s = ""
    for i in range(25):
        s += random.choice(["A", "B", "C"])
    return s


def test():
    for i in range(10000):
        t = randTest()
        a = main(t)
        if check(a):
            print(a, i, t)
            break


print(main("CAAACBAACCABABCAACBAABCBC"))
# test()
