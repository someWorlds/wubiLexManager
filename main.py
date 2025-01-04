#! c:/Program Files/Python310/python.exe
# author: someWorlds
# encoding: UTF-8

import time


def read_msWubiLex():
    msWubiLex = []
    with open("./refWubiCodes/msWubiLex.yaml", 'r', encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                msWubiLex.append(line.split())
    return msWubiLex


def read_cjkv_bsc_and_a_and_cmp():
    cjkv_bsc_and_a_and_cmp = []
    with open("./refWubiCodes/cjkv_bsc.yaml", 'r', encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                cjkv_bsc_and_a_and_cmp.append(line.split()[1])
    with open("./refWubiCodes/cjkv_a.yaml", 'r', encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                cjkv_bsc_and_a_and_cmp.append(line.split()[1])
    with open("./refWubiCodes/cjkv_cmp.yaml", 'r', encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                cjkv_bsc_and_a_and_cmp.append(line.split()[1])
    return cjkv_bsc_and_a_and_cmp


def compare_msWubiChars_with_cjkv_bsc_and_a_and_cmp():
    msWubiLex = read_msWubiLex()
    msWubiChars = []
    for i in range(len(msWubiLex)):
        if len(msWubiLex[i][1]) == 1:
            msWubiChars.append(msWubiLex[i][1])
    cjkv_bsc_and_a_and_cmp = read_cjkv_bsc_and_a_and_cmp()
    with open('./msWubiChars_not_in_cjkv_bsc_and_a_and_cmp.txt',
              'w',
              encoding='utf-8') as file:
        for i in range(len(msWubiChars)):
            if msWubiChars[i] not in cjkv_bsc_and_a_and_cmp:
                file.write(msWubiChars[i] + '\n')


def compare_cjkv_bsc_and_a_and_cmp_with_msWubiChars():
    msWubiLex = read_msWubiLex()
    msWubiChars = []
    for i in range(len(msWubiLex)):
        if len(msWubiLex[i][1]) == 1:
            msWubiChars.append(msWubiLex[i][1])
    cjkv_bsc_and_a_and_cmp = read_cjkv_bsc_and_a_and_cmp()
    with open('./cjkv_bsc_and_a_and_cmp_not_in_msWubiChars.txt',
              'w',
              encoding='utf-8') as file:
        for i in range(len(cjkv_bsc_and_a_and_cmp)):
            if cjkv_bsc_and_a_and_cmp[i] not in msWubiChars:
                file.write(cjkv_bsc_and_a_and_cmp[i] + '\n')

def generate_sogou_pinyin_custom_phrases():
    # 生成导入搜狗拼音自定义短语的txt文件


if __name__ == "__main__":
    startTime = time.time()
    compare_cjkv_bsc_and_a_and_cmp_with_msWubiChars()
    compare_msWubiChars_with_cjkv_bsc_and_a_and_cmp()
    endTime = time.time()
    print('{}'.format(endTime - startTime))
