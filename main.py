# 情報数学 行列で暗号やる
import utils
import traceback

import copy
import math


import sympy

from typing import Union
from sympy import Matrix


def main() -> None:
    enc_key, dec_key, n = mode1(1)
    # enc_key = Matrix([[47, 69], [38, 73]])
    # dec_key = Matrix([[17, 49], [38, 63]])
    # n = 95
    p_text = ""

    while True:
        try:
            mode = input('\n動作モードを選択してください。\n(鍵生成:1, 暗号化:2, 複合化:3, 現在の値を確認:4, 終了:5)>> ')
            if mode == '1':
                enc_key, dec_key, n = mode1(0)
            elif mode == '2':
                crypt = mode2(enc_key, n)
            elif mode == '3':
                p_text = mode3(dec_key, n)
            elif mode == '4':
                mode4(enc_key, dec_key, n)
            elif mode == '5':
                break
            else:
                raise ValueError
        except ValueError:
            print('入力値が不正です')


def mode1(mode: int) -> Union[Matrix, Matrix, int]:
    while True:
        try:
            if mode == 1:
                key_gen_mode = utils.y_or_n(input("鍵の自動生成を行いますか？[Y/n]>> "))
            else:
                key_gen_mode = 'y'

            if key_gen_mode == 'y':
                enc_key, dec_key, n = utils.make_keys()
                break
            elif key_gen_mode == 'n':
                n = int(input("n を入力してください。\n>> "))
                print("[[1, 2], [3, 4]] の順で入力してください。")
                key_list = utils.input_s(4)
                enc_key = sympy.Matrix(2, 2, key_list)
                dec_key = enc_key.inv_mod(n)
                break
            else:
                # raise Exception
                raise ValueError("input error!")
        # except ValueError as e:
        except ValueError as e:
            print(e)

    print(F"enc_key\n{enc_key}\ndec_key\n{dec_key}\nn\n{n}")
    return enc_key, dec_key, n


def mode2(enc_key: Matrix, n: int) -> str:
    while True:
        try:
            mode = utils.y_or_n(input("前回生成した鍵を利用しますか？[Y/n]>> "))
            if mode == 'n':
                n = int(input("n を入力してください。\n>> "))
                print("[[1, 2], [3, 4]] の順で入力してください。")
                key_list = utils.input_s(4)
                enc_key = sympy.Matrix(2, 2, key_list)
            elif mode == 'y':
                pass
            else:
                raise ValueError("input error!")

            p_int_mat = utils.str_to_int(input("暗号化する平文を入力してください。\n>> "), 1)
            print("計算します。")
            print(F"C ≡　{enc_key} * {p_int_mat} (mod{n})")
            c_int_mat = (enc_key * p_int_mat) % n
            # print(F"c ≡ {c_int_mat}(mod{n})")
            c_text = utils.int_to_str(c_int_mat)
            # print(F"Crypt\n{c_int_mat}")
            print(F"Crypt\n{c_text}")
            break
        except ValueError as e:
            print(e)

    return c_text


def mode3(dec_key: Matrix, n: int) -> str:
    while True:
        try:
            mode = utils.y_or_n(input("前回生成した鍵を利用しますか？[Y/n]"))
            if mode == 'n':
                n = int(input("n を入力してください。\n>> "))
                print("[[1, 2], [3, 4]] の順で入力してください。")
                key_list = utils.input_s(4)
                dec_key = sympy.Matrix(2, 2, key_list)
            elif mode == 'y':
                pass
            else:
                raise ValueError("input error!")

            c_int_mat = utils.str_to_int(input("複合化する暗号文を入力してください。\n>> "), 2)
            print(F"c_int_mat\n{c_int_mat}")
            print("計算します。")
            print(F"P ≡　{dec_key} * {c_int_mat} (mod{n})")
            p_int_mat = (dec_key * c_int_mat) % n
            # print(F"c ≡ {c_int_mat}(mod{n})")
            p_text = utils.int_to_str(p_int_mat)
            print(F"Decrypt!!\n{p_text}")
            break
        except ValueError as e:
            print(e)

    return p_text


def mode4(enc_key: Matrix, dec_key: Matrix, n: int):
    print("現在の鍵を表示します。")
    print(F"enc_key\n{enc_key}\ndec_key\n{dec_key}\nn\n{n}")
    return None


"""
    table = [1, 2, 3, 4]
    for i in range(2):
    for j in range(2):
        key[i][j] = table[i * j]
"""

"""
n, e, lcm, d = utils.make_keys(key_len, e)
print(F'n: {n}\ne: {e}\nd: {d}')
return n, e, d
"""





if __name__ == "__main__":
    main()
    data = Matrix([
        [65, 66, 67, 68, 69],
        [70, 71, 72,  0,  8]
    ])
    # utils.int_to_str(data)
    # utils.str_to_int("abcdefg")
    # mode1(1)



