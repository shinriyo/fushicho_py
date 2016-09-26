#!/Users/shinriyo/fushicho_py/env/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re

FILE_NAME = 'static/main.js'

class ModelInfo:
    def __init__(self):
        # カラム
        self.columns = []

        # 大文字開始カラム
        self.capitalized_columns = []

        # タイプ
        self.types = []

def check_django():
    static_path_exists = os.path.exists('static')
    return static_path_exists

def read_model():
    path_name = "assets/models.py"

    model_info = ModelInfo()
    # フィールドごとに型チェック用
    fields_dic = {'AutoField':'',
    'BigIntegerField':'',
    'BooleanField':'',
    'CharField':'',
    'CommaSeparatedIntegerField':'',
    'DateField':'',
    'DateTimeField':'',
    'DecimalField':'',
    'EmailField':'',
    'FileField':'',
    'FieldFile':'',
    'FilePathField':'',
    'FloatField':'',
    'ImageField':'',
    'IntegerField':'',
    'IPAddressField':'',
    'GenericIPAddressField':'',
    'NullBooleanField':'',
    'PositiveIntegerField':'',
    'PositiveSmallIntegerField':'',
    'SlugField':'',
    'SmallIntegerField':'',
    'TextField':'',
    'TimeField':'',
    'URLField':'',
    'XMLField':'',}

    with open(path_name, 'r') as f:
        for row in f:
            # title', 'models.CharField'を取得する
            m = re.match(r" *([a-zA-Z0-9]+) *= *([\.a-zA-Z0-9]+)", row)
            # m = re.match(r" +(\S) = (\S)", row)
            if m > 1:
                groups = m.groups()
                name = groups[0]
                # カラム名
                model_info.columns.append(name)
                # 大文字開始カラム名
                model_info.capitalized_columns.append(name.capitalize())

                # 変数名
                # print("variable:{}".format(name))
                type = groups[1]
                # models.CharFieldを分割
                types = type.split(".")
                if(len(types) > 1):
                    # 型系
                    # 使わない print(types[0])
                    type = types[1]
                    if type in fields_dic:
                        print("type:{}, field type:{}".format(type, fields_dic[type]))
                        model_info.types.append(type)
                    else:
                        print('unknown type.')
                else:
                    print(types)

        return model_info


def read_template(name, info):
    path_name = "assets/{}.template".format(name)

    with open(path_name, 'r') as f:
        # ファイルの中をstr
        data = "".join(line for line in f)
        # print data.format(capitalized=info.capitalized)
        # print(data % info)
        contain = data % info
        over_write(contain)
        # for row in f:
        #    print row.strip()

def over_write(contain):
    # 追記
    with open(FILE_NAME,'a') as f:
        f.write(contain)
        # 改行
        f.write('\n')
        f.close()

def message():
    install = ""
    print(install)

if __name__ == "__main__":
    argvs = sys.argv  # コマンドライン引数を格納したリストの取得
    argc = len(argvs) # 引数の個数

    # Djangoのチェック
    if not check_django():
        pass

    # 一旦消す
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)

    # 各カラム
    model_info = read_model()

    # TODO:
    arg_name = 'book'
    # TODO: 複数形はsをつけただけなので今後対応
    plural = "{}s".format(arg_name)
    capitalized = arg_name.capitalize()
    capitalized_plural = plural.capitalize()

    # main_js.templateが完成形なので消さないこと
    # 以下が実施に利用
    # names = ['main_search_panel_js',
    #          'main_table_raw_js',
    #          'main_table_js',
    #          'main_form_js',
    #          'main_panel_js']

    read_template('main_search_panel_js', ())
    read_template('main_table_raw_js', (capitalized))

    # 以下タグ生成
    # <th>Title</th>
    # <th>Category</th>
    # 以下タグも生成
    #<label forHtml='title'>Title</label><input ref='title' name='title' type='text' value={this.props.book.title} onChange={this.onChange}/>
    # 以下jsも生成
    # var title = React.findDOMNode(this.refs.title).value;
    th = []
    labels = []
    js_nodes = []

    for index, column in enumerate(model_info.columns):
        # th tag 大文字開始
        th.append('<th>{}</th>'.format(model_info.capitalized_columns[index]))
        # label tag
        label = "<label forHtml='%s'>%s</label>" \
                "<input ref='%s' name='%s' type='text' value={this.props.%s.%s} onChange={this.onChange}/>" \
            % (column, model_info.capitalized_columns[index], column, column, arg_name, column)
        labels.append(label)
        js_node = "var {column} = React.findDOMNode(this.refs.{column}).value;".format(column=column)
        js_nodes.append(js_node)

    joined_th = ('\n' + ' ' * 24).join(th)
    read_template('main_table_js', (capitalized, plural, arg_name, capitalized, arg_name, arg_name, arg_name, joined_th))

    joined_label = ('\n' + ' ' * 16).join(labels)
    joined_js_nodes = ('\n' + ' ' * 8).join(js_nodes)
    # title, category
    column_args = (', ').join(model_info.columns)
    read_template('main_form_js', (capitalized, joined_label, arg_name, arg_name, arg_name, arg_name, joined_js_nodes, column_args ))

    # 以下js生成
    # title:"",
    init_js = ('\n' + ' ' * 16).join("{}:\"\",".format(line) for line in model_info.columns)

    # 以下js生成
    # title: title,
    editing_js = ('\n' + ' ' * 16).join("{column}: {column},".format(column=line) for line in model_info.columns)

    # 結構長い
    read_template('main_panel_js', (capitalized, plural, capitalized, init_js, capitalized,
                                    plural, plural, capitalized, arg_name, capitalized, capitalized_plural,
                                    capitalized_plural, capitalized_plural, arg_name, plural,
                                    capitalized, arg_name, column_args, capitalized, editing_js, capitalized,
                                    capitalized, capitalized_plural, plural, capitalized, capitalized, capitalized,
                                    arg_name, capitalized_plural, capitalized, arg_name, capitalized_plural, capitalized,
                                    #handleDeleteClick
                                    capitalized, arg_name, capitalized, capitalized_plural,
                                    capitalized, plural
    ))

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

