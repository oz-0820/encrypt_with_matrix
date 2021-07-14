import random

import sympy
from sympy import Matrix
from typing import Union


def make_keys() -> Union[Matrix, Matrix, int]:
    try:
        # n = random.randint(1000, 9999)
        n = 95
        enc_key = sympy.randMatrix(2, 2, 0, n)
        # print(F"{enc_key}, {(enc_key[0] * enc_key[3]) - (enc_key[1] * enc_key[2])}")
        dec_key = enc_key.inv_mod(n)
    except sympy.matrices.common.NonInvertibleMatrixError:
        enc_key, dec_key, n = make_keys()
    return enc_key, dec_key, n


def str_to_int(raw_text: str, mode: int) -> Matrix:
    # mode == 1 enc
    # mode == 2 dec
    text_len = len(raw_text)
    text_list = list(raw_text)
    if mode == 1:
        target_len = text_len // 2 + 1
    if mode == 2:
        target_len = text_len // 2

    int_list = []

    if mode == 1:
        for i in range(text_len):
            int_list.append(ord(text_list[i]) - 32)
        if target_len * 2 != text_len + 1:
            int_list.append(0)
        int_list.append(text_len)
        int_mat = sympy.Matrix(2, target_len, int_list)
    if mode == 2:
        for i in range(text_len):
            int_list.append(ord(text_list[i]) - 32)
        int_mat = sympy.Matrix(2, target_len, int_list)
    print(int_mat)
    return int_mat
# in    'abcde'
# out   [[1, 2, 3], [4, 5, 5]]
# in    'abcdef'
# out   [[1, 2, 3, 4], [5, 6, 0, 6]]


def int_to_str(int_mat: Matrix) -> str:
    mat_len = len(int_mat)
    text_len = min(int_mat[mat_len - 1], mat_len)

    text_list = []
    for i in range(text_len):
        text_list.append(chr(int_mat[i] + 32))
    raw_text = "".join(text_list)
    return raw_text


def input_s(count: int) -> list:
    data = []
    for i in range(count):
        data.append(input(F"{i + 1}>>"))
    return data



