#! c:/Program Files/Python310/python.exe
# author: someWorlds
# encoding: UTF-8

import time
from fontTools.ttLib import TTFont
import wubiLexManager

Freq = {
    'word_new': '30000',  # 自添加但是ms中没有的词，用该频率
    'char_inc': '50700',  # 对于一些简码字，将其除最简码外的频率增加到50700档位
    'char_err': '50750',  # 字的容错码频率设置到50750档
    'syms': '50800',  # 符号类的自定义短语，将其频率设置到50800档位
    'cjkv_b': '51000',  # cjkv的其它字，频率档位更高
    'cjkv_c': '52000',
    'cjkv_d': '53000',
    'cjkv_e': '54000',
    'cjkv_f': '55000',
    'cjkv_g': '56000',
    'cjkv_h': '57000',
    'cjkv_i': '58000',
}


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


def find_repFreq():
    # 查看自定义的频率Freq是否与ms的频率冲突
    msWubiLex = []
    with open("./refWubiLex/msWubiLex.yaml", 'r', encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                msWubiLex.append(line.split())
    with open('find_freq.yaml', 'w', encoding='utf-8') as file:
        for term in msWubiLex:
            if term[2] in Freq.values():
                file.write(term[0] + '    ' + term[1] + '    ' + term[2] +
                           '\n')


def get_unicode_map_from_ttf(font_file):
    """
    获取ttf文件中所有字符及其对应的Unicode值

    参数:
        font_file (str): ttf字体文件路径

    返回:
        dict: 键为整数形式表示的Unicode码位；值为相应字符
    """
    f_obj = TTFont(font_file)
    cmap = f_obj.getBestCmap()

    # 将键转换成十进制表示法，并构建新的字典结构
    unicode_map = {ch_unicode: chr(ch_unicode) for ch_unicode in cmap.keys()}
    return unicode_map


def get_unicode_file_form_ttf(filePath_ttf: str):
    # 从ttf文件中获取所有字符的unicode值，生成txt文件
    with open('char_unicode.txt', 'w', encoding='utf-8') as file:
        unicode_mapping = get_unicode_map_from_ttf(filePath_ttf)
        for codepoint, character in list(unicode_mapping.items())[:]:
            file.write(f'U+{codepoint:X}' + '    ' + character + '\n')


if __name__ == "__main__":
    startTime = time.time()
    print('{}'.format(startTime))

    # compare_cjkv_bsc_and_a_and_cmp_with_msWubiChars()
    # compare_msWubiChars_with_cjkv_bsc_and_a_and_cmp()
    # refine_msWubilex_by_cjkv()

    # find_repFreq()

    wubi = wubiLexManager.wubiLexManager(True)
    wubi.process_input()
    wubi = wubiLexManager.wubiLexManager(False)
    wubi.generate_outputFiles()

    endTime = time.time()
    print('{}'.format(endTime))
    print('{}'.format(endTime - startTime))
