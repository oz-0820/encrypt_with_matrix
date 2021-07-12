# 情報数学 行列で暗号やる

import utils

from typing import Union

def main() -> None:
    print('まず鍵を作ります')
    n, e, d = mode1()
    crypt = 0
    while True:
        try:
            print('\n動作モードを選択してください。\n(鍵生成:1, 暗号化:2, 複合化:3, 現在の値を確認:4, 終了:5)')
            mode = input('mode: ')
            if mode == '1':
                n, e, d = mode1()
            elif mode == '2':
                crypt = mode2(n, e)
            elif mode == '3':
                mode3(crypt, n, d)
            elif mode == '4':
                mode4(n, e, d, crypt)
            elif mode == '5':
                break
            else:
                raise ValueError
        except ValueError:
            print('入力値が不正です')


def mode1() -> Union[int, int, int]:
    key_len = int(input('4096bit以下を推奨。ただし、あまりにも小さいとエラーが出ます。\n鍵の長さ(bit): '))
    e = utils.e_input()

    n, e, lcm, d = utils.make_keys(key_len, e)
    print(F'n: {n}\ne: {e}\nd: {d}')
    return n, e, d


def mode2():
    pass


if __name__ == "__main__":
    # main()
    utils.str_to_int("abcdefg")



