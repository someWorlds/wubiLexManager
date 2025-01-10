#! c:/Program Files/Python310/python.exe
# author: someWorlds
# encoding: UTF-8

import time


def read_msWubiLex_org():
    msWubiLex = []
    with open("./refWubiLex/msWubiLex_org.yaml", 'r',
              encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                msWubiLex.append(line.split())
    return msWubiLex


def read_cjkv_bsc_and_a_and_cmp():
    cjkv_bsc_and_a_and_cmp = []
    with open("./refWubiLex/cjkv_bsc.yaml", 'r', encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                cjkv_bsc_and_a_and_cmp.append(line.split()[1])
    with open("./refWubiLex/cjkv_a.yaml", 'r', encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                cjkv_bsc_and_a_and_cmp.append(line.split()[1])
    with open("./refWubiLex/cjkv_cmp.yaml", 'r', encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                cjkv_bsc_and_a_and_cmp.append(line.split()[1])
    return cjkv_bsc_and_a_and_cmp


def compare_msWubiChars_with_cjkv_bsc_and_a_and_cmp():
    msWubiLex = read_msWubiLex_org()
    msWubiChars = []
    for i in range(len(msWubiLex)):
        if len(msWubiLex[i][1]) == 1:
            msWubiChars.append(msWubiLex[i][1])
    cjkv_bsc_and_a_and_cmp = read_cjkv_bsc_and_a_and_cmp()
    with open('./refWubiLex/msWubiChars_not_in_cjkv_bsc_and_a_and_cmp.txt',
              'w',
              encoding='utf-8') as file:
        for i in range(len(msWubiChars)):
            if msWubiChars[i] not in cjkv_bsc_and_a_and_cmp:
                file.write(msWubiChars[i] + '\n')


def compare_cjkv_bsc_and_a_and_cmp_with_msWubiChars():
    msWubiLex = read_msWubiLex_org()
    msWubiChars = []
    for i in range(len(msWubiLex)):
        if len(msWubiLex[i][1]) == 1:
            msWubiChars.append(msWubiLex[i][1])
    cjkv_bsc_and_a_and_cmp = read_cjkv_bsc_and_a_and_cmp()
    with open('./refWubiLex/cjkv_bsc_and_a_and_cmp_not_in_msWubiChars.txt',
              'w',
              encoding='utf-8') as file:
        for i in range(len(cjkv_bsc_and_a_and_cmp)):
            if cjkv_bsc_and_a_and_cmp[i] not in msWubiChars:
                file.write(cjkv_bsc_and_a_and_cmp[i] + '\n')


def refine_msWubilex_by_cjkv():
    msWubiLex = read_msWubiLex_org()
    cjkv_bsc_and_a_and_cmp = []
    with open("./refWubiLex/cjkv_bsc.yaml", 'r', encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                term = line.split()
                cjkv_bsc_and_a_and_cmp.append([term[2], term[1]])
    with open("./refWubiLex/cjkv_a.yaml", 'r', encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                term = line.split()
                cjkv_bsc_and_a_and_cmp.append([term[2], term[1]])
    with open("./refWubiLex/cjkv_cmp.yaml", 'r', encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                term = line.split()
                cjkv_bsc_and_a_and_cmp.append([term[2], term[1]])
    msWubiLex_char = []
    msWubiLex_word = []
    for term in msWubiLex:
        if len(term[1]) == 1:
            res = list(
                filter(lambda x: x[1] == term[1], cjkv_bsc_and_a_and_cmp))
            if res:
                msWubiLex_char.append(term)
        else:
            msWubiLex_word.append(term)
    for term in cjkv_bsc_and_a_and_cmp:
        res = list(filter(lambda x: x[1] == term[1], msWubiLex_char))
        if not res:
            msWubiLex_char.append([term[0], term[1], '50646'])
    msWubiLex = []
    msWubiLex.extend(msWubiLex_word)
    msWubiLex.extend(msWubiLex_char)
    msWubiLex.sort(key=lambda x: int(x[2]))
    msWubiLex.sort(key=lambda x: x[0])
    with open("./refWubiLex/msWubiLex.yaml", 'w', encoding='utf-8') as file:
        intro = """# win11系统自带微软五笔编码, 根据cjkv_bsc + a + cmp修正版
# 提取时间: 2024-07-26
# 编码数: 534021, 其中去除错误及无用字符192，增加缺少的字符100
# encoding: utf-8
# 微软词汇的频率权重越小越靠前，最大频率权重为50646
# columns: 五笔编码    词汇    ms频率"""
        file.write(intro + '\n\n')
        for term in msWubiLex:
            file.write(term[0] + '    ' + term[1] + '    ' + term[2] + '\n')


if __name__ == "__main__":
    startTime = time.time()
    print('{}'.format(startTime))

    # compare_cjkv_bsc_and_a_and_cmp_with_msWubiChars()
    # compare_msWubiChars_with_cjkv_bsc_and_a_and_cmp()
    # refine_msWubilex_by_cjkv()

    endTime = time.time()
    print('{}'.format(endTime))
    print('{}'.format(endTime - startTime))
