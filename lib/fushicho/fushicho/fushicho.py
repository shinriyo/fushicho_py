#!/Users/shinriyo/fushicho_py/env/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import socket
import re


def read_model():
    path_name = "assets/models.py"


    # フィールドごとに型チェック用
    fields = ['AutoField',
    'BigIntegerField',
    'BooleanField',
    'CharField',
    'CommaSeparatedIntegerField',
    'DateField',
    'DateTimeField',
    'DecimalField',
    'EmailField',
    'FileField',
    'FileField'
    'FieldFile',
    'FilePathField',
    'FloatField',
    'ImageField',
    'IntegerField',
    'IPAddressField',
    'GenericIPAddressField',
    'NullBooleanField',
    'PositiveIntegerField',
    'PositiveSmallIntegerField',
    'SlugField',
    'SmallIntegerField',
    'TextField',
    'TimeField',
    'URLField',
    'XMLField']

    with open(path_name, 'r') as f:
        for row in f:
            # title', 'models.CharField'を取得する
            m = re.match(r" *([a-zA-Z0-9]+) *= *([\.a-zA-Z0-9]+)", row)
            # m = re.match(r" +(\S) = (\S)", row)
            if m > 1:
                groups = m.groups()
                name = groups[0]
                # 変数名
                print("variable:{}".format(name))
                type = groups[1]
                # models.CharFieldを分割
                types = type.split(".")
                if(len(types) > 1):
                    # 型系
                    # 使わない print(types[0])
                    type = types[1]
                    print("type:{}".format(type))
                else:
                    print(types)



def read_template(name, info):
    path_name = "assets/{}.template".format(name)

    with open(path_name, 'r') as f:
        print f.format(info)
        for row in f:
            # print row.strip()
            print row


def crate():
    # 上書き
    with open('test.txt','w') as f:
        f.write('hoge\n')
        f.close()

def message():
    install = ""
    print(install)


class TemplateInfo:
    def __init__(self):
        self.name = ''
        # 複数形
        self.plural = ''

        # 大文字開始
        self.capitalized = ''

        # 大文字複数形
        self.capitalized_plural = ''

if __name__ == "__main__":
    argvs = sys.argv  # コマンドライン引数を格納したリストの取得
    argc = len(argvs) # 引数の個数

    read_model()

    # TODO:
    arg_name = 'book'
    # TODO: 複数形はsをつけただけなので今後対応
    plural = "{}s".format(arg_name)
    capitalized = arg_name.capitalize()
    capitalized_plural = plural.capitalize()

    # main_js.templateが完成形なので消さないこと
    # 以下が実施に利用
    # main_search_panel_js
    # main_table_raw_js
    # main_table_js
    # main_form_js
    # main_panel_js
    names = ['main_search_panel_js', 'main_table_raw_js', 'main_table_js',
            'main_form_js', 'main_panel_js']

    info = TemplateInfo()
    info.name = arg_name
    info.plural = plural
    info.capitalized = capitalized
    info.capitalized_plural = capitalized_plural

    # for name in names:
    #     read_template(name, info)

    # 引数が1つなのは自分自身の.py
    if (argc == 1):
        pass
    elif (argc == 2):
        # 引数2番目が名前
        pass
    else:
        sys.exit('Argments are invalid.')

