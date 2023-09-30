from itertools import product


def bit_all_search(n):
    """bit全探索
    n: bit数
    """
    for bits in product([0, 1], repeat=n):
        print(bits)
