import sympy

import utils

from typing import Union
from sympy import Matrix


def main() -> None:
    enc_key, dec_key, n = mode1(1)

    while True:
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
            print('入力値が不正です')


def mode1(mode: int) -> Union[Matrix, Matrix, int]:
    while True:

        if mode == 1:
            key_gen_mode = utils.y_or_n(input("鍵の自動生成を行いますか？[Y/n]>> "), True)
        else:
            key_gen_mode = True

        if key_gen_mode:
            enc_key, dec_key, n = utils.make_keys(0)
            break
        else:
            try:
                n = int(input("n を入力してください。\n>> "))
            except ValueError:
                print("input error!")
            else:
                print("[[1, 2], [3, 4]] の順で入力してください。")
                key_list = utils.input_s(4)
                enc_key = sympy.Matrix(2, 2, key_list)
                dec_key = enc_key.inv_mod(n)
                break

    print(F"enc_key\n{enc_key}\ndec_key\n{dec_key}\nn\n{n}")
    return enc_key, dec_key, n


def mode2(enc_key: Matrix, n: int) -> str:
    while True:
        mode = utils.y_or_n(input("前回生成した鍵を利用しますか？[Y/n]>> "), True)
        if not mode:
            try:
                n = int(input("n を入力してください。\n>> "))
            except ValueError:
                print("input error!")
            else:
                print("[[1, 2], [3, 4]] の順で入力してください。")
                key_list = utils.input_s(4)
                enc_key = sympy.Matrix(2, 2, key_list)
        p_int_mat = utils.str_to_int(input("暗号化する平文を入力してください。\n>> "), 1)
        print(F"C ≡　{enc_key} * {p_int_mat} (mod{n})")
        c_int_mat = (enc_key * p_int_mat) % n
        c_text = utils.int_to_str(c_int_mat)
        print(F"Crypt\n{c_text}")
        break

    return c_text


def mode3(dec_key: Matrix, n: int) -> str:
    mode = utils.y_or_n(input("前回生成した鍵を利用しますか？[Y/n]"), True)
    if not mode:
        try:
            n = int(input("n を入力してください。\n>> "))
        except ValueError:
            print("input error!")
        else:
            print("[[1, 2], [3, 4]] の順で入力してください。")
            key_list = utils.input_s(4)
            dec_key = sympy.Matrix(2, 2, key_list)

    c_int_mat = utils.str_to_int(input("複合化する暗号文を入力してください。\n>> "), 2)
    print(F"P ≡　{dec_key} * {c_int_mat} (mod{n})")
    p_int_mat = (dec_key * c_int_mat) % n
    p_text = utils.int_to_str(p_int_mat)
    print(F"Decrypt!!\n{p_text}")

    return p_text


def mode4(enc_key: Matrix, dec_key: Matrix, n: int):
    print("現在の鍵を表示します。")
    print(F"enc_key\n{enc_key}\ndec_key\n{dec_key}\nn\n{n}")
    return None


if __name__ == "__main__":
    main()

