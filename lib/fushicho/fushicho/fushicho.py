#!/Users/shinriyo/fushicho_py/env/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import socket
import re


def read_template(name):
    path_name = "assets/{}.template".format(name)

    with open(path_name, 'r') as f:
        for row in f:
            # print row.strip()
            print row

def crate():
    # 上書き
    with open('test.txt','w') as f:
        f.write('hoge\n')
        f.close()



if __name__ == "__main__":
    argvs = sys.argv  # コマンドライン引数を格納したリストの取得
    argc = len(argvs) # 引数の個数

    # main_search_panel_js
    # main_table_raw_js
    # main_table_js
    # main_form_js
    # main_panel_js
    names = ['main_search_panel_js', 'main_table_raw_js', 'main_table_js',
            'main_form_js', 'main_panel_js']
    for name in names:
        read_template(name)

    # 引数が1つなのは自分自身の.py
    if (argc == 1):
        pass
    elif (argc == 2):
        pass
    else:
        sys.exit('Argments are invalid.')

