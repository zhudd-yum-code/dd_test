#!/usr/bin/python
#encoding:utf-8
""" 这是一个创建文件的程序
文件存在则重新输入
并向文件里添加内容 """

import os

def get_fname():
    while True:
        fname = input('请输入文件名：')
        if not os.path.exists(fname):
            break
        print('文件已存在，请重试')

    return fname

def get_content():
    content = []
    print('请输入内容，输入end结束输入：')
    while True:
        line = input('(end to quit) > ')
        if line == 'end':
            break
        content.append(line + '\n')

    return content


def w_file(fname, content):
    with open(fname, 'w') as fobj:
        fobj.writelines(content)

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    w_file(fname, content)
