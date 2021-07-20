import sympy

from sympy import Matrix
from typing import Union

from sympy.matrices.common import NonInvertibleMatrixError


def make_keys(n: int) -> Union[Matrix, Matrix, int]:
    # n = random.randint(1000, 9999)
    n = 95
    enc_key = sympy.randMatrix(2, 2, 0, n)
    try:
        dec_key = enc_key.inv_mod(n)
    except NonInvertibleMatrixError:
        enc_key, dec_key, n = make_keys(n)

    return enc_key, dec_key, n


def str_to_int(raw_text: str, mode: int) -> Matrix:
    # mode == 1 enc
    # mode == 2 dec
    text_len = len(raw_text)
    text_list = list(raw_text)

    int_list = []

    for i in range(text_len):
        int_list.append(ord(text_list[i]) - 32)
    if mode == 1:
        if text_len % 2 == 0:
            int_list.append(0)
        int_list.append(text_len)

    int_mat = sympy.Matrix(2, int(len(int_list) / 2), int_list)
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


def y_or_n(data: str) -> str:
    if data in ['n', 'N', 'no', 'No', 'NO']:
        return 'n'
    if data in ['', 'y', 'yes', 'Yes', 'YES']:
        return 'y'


