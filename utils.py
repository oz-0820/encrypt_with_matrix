import utils

import sympy
from sympy import Matrix
from typing import Union


def make_keys():
    e = sympy.Matrix([
        [sympy.randint(0, 99), sympy.randint(0, 99)],
        [sympy.randint(0, 99), sympy.randint(0, 99)]
    ])
    # sympy.randMatrix(2, 2, 0, 999)
    return e


def make_p(text_list: list) -> None:
    target_len = len(text_list) // 2


"""
def make_keys(key_len: int, e: int) -> Union[int, int, int, int]:
    p1_len = (key_len // 2) + 1
    p2_len = key_len - p1_len
    prime1 = sympy.randprime(pow(2, p1_len-1), pow(2, p1_len)-1)
    prime2 = sympy.randprime(pow(2, p2_len-1), pow(2, p2_len)-1)

    if prime1 == prime2:
        while prime1 == prime2:
            prime2 = sympy.randprime(pow(2, p2_len - 1), pow(2, p2_len) - 1)

    n = prime1 * prime2
    lcm = sympy.lcm(prime1-1, prime2-1)
    d, a, b = sympy.gcdex(e, lcm)
    d = int(d % lcm)

    return n, e, lcm, d
"""


def e_input() -> int:
    e = input('eの値を選択してください。(a~g)\na: 3，\nb: 5,\nc: 17,\nd: 257,\ne: 65537,(推奨)\nf: 131073,\ng: 262145,\n>> ')
    if e == 'a':
        return 3
    elif e == 'b':
        return 5
    elif e == 'c':
        return 17
    elif e == 'd':
        return 257
    elif e == 'e':
        return 65537
    elif e == 'f':
        return 131073
    elif e == 'g':
        return 262145
    else:
        print('入力エラー')
        return e_input()


def str_to_int(raw_text: str) -> Matrix:
    text_list = list(raw_text)
    int_list = [[], []]
    if len(text_list) % 2 == 0:
        target_len = len(text_list) // 2
    else:
        target_len = len(text_list) // 2 + 1

    for i in range(target_len):
        int_list[0].append(ord(text_list[i]) - 32)

    if len(text_list) % 2 != 0:
        int_list[1].append(0)
    data = sympy.Matrix(int_list)
    return data  #[[1, 2, 3], [4, 5, 6]]
# [[1, 3, 5], [2, 4, 6]]

def int_to_char(int_list: list) -> str:
    text_list = []
    for i in range(len(int_list[0]) * 2):
        text_list.append(chr(int_list[i % 2][i // 2] + 32))
    raw_text = "".join(text_list)
    return raw_text





