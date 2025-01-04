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


def read_chars_1keySim():
    chars_1keySim = []
    with open("./custWubiCodes/chars_1keySim.yaml", 'r',
              encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                chars_1keySim.append(line.split())
    return chars_1keySim


def read_chars_2keySim():
    chars_2keySim = []
    with open("./custWubiCodes/chars_2keySim.yaml", 'r',
              encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                chars_2keySim.append(line.split())
    return chars_2keySim


def read_chars_3keySim():
    chars_3keySim = []
    with open("./custWubiCodes/chars_3keySim.yaml", 'r',
              encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                chars_3keySim.append(line.split())
    return chars_3keySim


def read_chars_3keyFull():
    chars_3keyFull = []
    with open("./custWubiCodes/chars_3keyFull.yaml", 'r',
              encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                chars_3keyFull.append(line.split())
    return chars_3keyFull


def read_chars_4keyFull():
    chars_4keyFull = []
    with open("./custWubiCodes/chars_4keyFull.yaml", 'r',
              encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                chars_4keyFull.append(line.split())
    return chars_4keyFull


def read_syms_pi():
    syms_pi = []
    with open("./custWubiCodes/syms_pi.yaml", 'r', encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                syms_pi.append(line.split())
    return syms_pi


def read_syms():
    symbols = []
    with open("./custWubiCodes/syms.yaml", 'r', encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                symbols.append(line.split())
    return symbols


def read_words_2keySim():
    words_2keySim = []
    with open("./custWubiCodes/words_2keySim.yaml", 'r',
              encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                words_2keySim.append(line.split())
    return words_2keySim


def read_words_4keyFull():
    words_4keyFull = []
    with open("./custWubiCodes/words_4keyFull.yaml", 'r',
              encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                words_4keyFull.append(line.split())
    return words_4keyFull


def read_words_pi():
    words_pi = []
    with open("./custWubiCodes/words_pi.yaml", 'r', encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                words_pi.append(line.split())
    return words_pi


def get_custWubiCodes(withPi: bool = False):
    custWubiCodes = []
    custWubiCodes.extend(read_chars_1keySim())
    custWubiCodes.extend(read_chars_2keySim())
    custWubiCodes.extend(read_chars_3keySim())
    custWubiCodes.extend(read_chars_3keyFull())
    custWubiCodes.extend(read_chars_4keyFull())
    custWubiCodes.extend(read_syms())
    custWubiCodes.extend(read_words_2keySim())
    custWubiCodes.extend(read_words_4keyFull())
    if withPi is True:
        custWubiCodes.extend(read_syms_pi())
        custWubiCodes.extend(read_words_pi())
    custWubiCodes.sort(key=lambda x: int(x[2]))
    custWubiCodes.sort(key=lambda x: x[0])
    return custWubiCodes


def get_custWubiCodes_chars():
    custWubiCodes_chars = []
    custWubiCodes_chars.extend(read_chars_1keySim())
    custWubiCodes_chars.extend(read_chars_2keySim())
    custWubiCodes_chars.extend(read_chars_3keySim())
    custWubiCodes_chars.extend(read_chars_3keyFull())
    custWubiCodes_chars.extend(read_chars_4keyFull())
    custWubiCodes_chars.sort(key=lambda x: int(x[2]))
    custWubiCodes_chars.sort(key=lambda x: x[0])
    return custWubiCodes_chars


def get_custWubiCodes_words(withPi: bool = False, onMobile: bool = False):
    custWubiCodes_words = []
    custWubiCodes_words.extend(read_words_4keyFull())
    if withPi is True:
        custWubiCodes_words.extend(read_words_pi())
    if onMobile is True:
        custWubiCodes_words.extend(read_words_2keySim())
    custWubiCodes_words.sort(key=lambda x: int(x[2]))
    custWubiCodes_words.sort(key=lambda x: x[0])
    return custWubiCodes_words


def get_custWubiCodes_phrases(withPi: bool = False, onMobile: bool = False):
    custWubiCodes_phrases = []
    custWubiCodes_phrases.extend(read_syms())
    if withPi is True:
        custWubiCodes_phrases.extend(read_syms_pi())
    if onMobile is False:
        custWubiCodes_phrases.extend(read_words_2keySim())
    custWubiCodes_phrases.sort(key=lambda x: int(x[2]))
    custWubiCodes_phrases.sort(key=lambda x: x[0])
    return custWubiCodes_phrases


def write_custPhrases_sogouPy(
        filepath: str = './outputFiles/custPhrases_sogouPy.txt',
        custWubiCodes: list = []):
    default_statement = """;  搜狗输入法--自定义短语配置文件

;  自定义短语说明：
;  1、自定义短语支持多行、空格、指定位置。
;  2、每条自定义短语最多支持30000个汉字，总共支持100000条自定义短语。
;  3、自定义短语的格式如下：

;  单行的格式：
;  字符串+英文逗号+数字（指定排序位置）=短语

;  多行的格式：
;  字符串+英文逗号+数字（指定排序位置）=
;  多行短语

;  具体格式可以参考下面的实例。
;  4、最多支持100000行自定义短语。
;  5、自定义短语的用途有：快捷输入手机号、邮箱、诗词、小短文等，大家可以自由发挥。
;  6、时间函数功能。具体定义格式如下：;  字符串+英文逗号+数字（ 指定排序位置）=#表达式
;  注意：表达式以英文#开头，后面的表达式中的每一个函数的前面都包含有英文$。
;  函数表如下：
;  函数         含义            举例
;  $year        年(4位)         2006、2008
;  $year_yy     年(2位)         06、08
;  $month       月              12、8、3
;  $month_mm    月              12、08、03              //此函数在输入法3.1版之后（含）有效
;  $day         日              3、13、22
;  $day_dd      日             03、13、22       //此函数在输入法3.1版之后（含）有效
;  $weekday     星期            0、1、2、5、6
;  $fullhour    时(24小时制)    2、8、13、23
;  $fullhour_hh 时(24小时制)    02、08、13、23          //此函数在输入法3.1版之后（含）有效
;  $halfhour    时(12小时制)    2、8、10、11
;  $halfhour_hh 时(12小时制)    02、08、10、11          //此函数在输入法3.1版之后（含）有效
;  $ampm        AM、PM(英)      AM、PM（大写）
;  $minute      分              02、08、15、28
;  $second      秒              02、08、15、28
;  $year_cn     年(中文4位)     二〇〇六
;  $year_yy_cn  年(中文2位)     〇六
;  $month_cn    月(中文)        十二、八、三
;  $day_cn      日(中文)        三、十三、二十二
;  $weekday_cn  星期(中文)      日、一、二、五、六
;  $fullhour_cn 时(中文24时制)  二、八、十三、二十三
;  $halfhour_cn 时(中文12时制)  二、八、一、十一
;  $ampm_cn     上午下午(中文)  上午、下午
;  $minute_cn   分(中文)        零二、零八、十五、二十八
;  $second_cn   秒(中文)        零二、零八、十五、二十八
;  具体你可以参考这个文件最下面的例子，实际体验一下就明白了。
;  你可以用自定义短语来做一个带动态时间的多行回信落款。
;  ss,1=#$year年$month月$day_dd日 $fullhour:$minute:$second

"""
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(default_statement)
        num = 0
        for i in range(len(custWubiCodes)):
            num += 1
            if 0 == i or custWubiCodes[i][0] == custWubiCodes[i - 1][0]:
                file.write(custWubiCodes[i][0] + ',' + str(num) + '=' +
                           custWubiCodes[i][1] + '\n')
            else:
                num = 1
                file.write(custWubiCodes[i][0] + ',' + str(num) + '=' +
                           custWubiCodes[i][1] + '\n')


def generate_custCodes_sogouPy():
    # 生成导入PC搜狗拼音自定义短语的txt文件
    filepath = [
        "./outputFiles/custPhrases_sogouPy.txt",
        "./outputFiles/custPhrases_sogouPy_withPi.txt"
    ]
    try:
        for i in range(len(filepath)):
            write_custPhrases_sogouPy(
                filepath=filepath[i],
                custWubiCodes=get_custWubiCodes(withPi=bool(i)))
    except FileNotFoundError:
        return None


def generate_custCodes_mobileSogou():
    # 生成导入手机搜狗输入法的自定义五笔方案的txt文件，以及常用语的csv文件
    filepaths = [
        './outputFiles/custScheme_mobileSogou.txt',
        './outputFiles/custScheme_mobileSogou_withPi.txt'
    ]
    try:
        for i in range(len(filepaths)):
            with open(filepaths[i], 'w', encoding='utf-8') as file:
                custWubiCodes = get_custWubiCodes_chars()
                custWubiCodes.extend(
                    get_custWubiCodes_words(withPi=bool(i), onMobile=True))
                custWubiCodes.sort(key=lambda x: int(x[2]))
                custWubiCodes.sort(key=lambda x: x[0])
                for i in range(len(custWubiCodes)):
                    file.write(custWubiCodes[i][0] + '\t' +
                               custWubiCodes[i][1] + '\n')
    except FileNotFoundError:
        None
    filepaths = [
        './outputFiles/custPhrases_mobileSogou.csv',
        './outputFiles/custPhrases_mobileSogou_withPi.csv'
    ]
    try:
        for i in range(len(filepaths)):
            with open(filepaths[i], 'w', encoding='utf-8') as file:
                custWubiCodes = get_custWubiCodes_phrases(withPi=bool(i),
                                                          onMobile=True)
                custWubiCodes.sort(key=lambda x: int(x[2]))
                custWubiCodes.sort(key=lambda x: x[0])
                for i in range(len(custWubiCodes)):
                    custWubiCodes[i].pop(2)
                    file.writelines(','.join(map(str, custWubiCodes[i])) +
                                    '\n')
    except FileNotFoundError:
        None


def generate_custCodes_sogouWb():
    # 生成导入PC搜狗五笔的自定义单字码表的txt文件、用户词库的txt文件、自定义短语的txt文件
    filepaths = [
        './outputFiles/custChars_sogouWb.txt',
        './outputFiles/custWords_sogouWb.txt',
        './outputFiles/custPhrases_sogouWb.txt',
        './outputFiles/custWords_sogouWb_withPi.txt',
        './outputFiles/custPhrases_sogouWb_withPi.txt',
    ]
    try:
        for i in range(len(filepaths)):
            with open(filepaths[i], 'w', encoding='utf-8') as file:
                if i == 0:
                    custWubiCodes = get_custWubiCodes_chars()
                else:
                    custWubiCodes = get_custWubiCodes_words(withPi=bool(
                        (i - 1) // 2),
                                                            onMobile=False)
                for i in range(len(custWubiCodes)):
                    file.write(custWubiCodes[i][0] + '\t' +
                               custWubiCodes[i][1] + '\n')
    except FileNotFoundError:
        None


def generate_outputFiles():
    generate_custCodes_sogouPy()
    generate_custCodes_mobileSogou()
    generate_custCodes_sogouWb()
    return None


def read_multi_line_input():
    print("请输入多行字符串（输入空行结束）：")
    print("输入示例1：您好          # 无数字时，根据微软五笔码表计算频率，自动生成排序")
    print("输入示例2：你好     1    # 数字0-9指定候选词排列位置，中间用空格或制表符隔开")
    print("输入示例3：它好     0    # 0表示要删除该词")
    print("输入示例4：饱       9    # 9表示排序置后")
    print("输入示例5：完全乱写  sb   # 自定义短语，后面需要输入字母编码，默认排序置后，")
    print("输入示例5：完全乱写  sb 2 # 也可再加入控制排序的数字0-9")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line.split())
    return lines


def judge_inputString_in_cjkv_bsc_and_a_and_cmp(inputString: str):
    for char in inputString:
        if ord(char) >= ord('㐀') and ord(char) <= ord('䶿'):
            continue
        elif ord(char) >= ord('一') and ord(char) <= ord('鿿'):
            continue
        elif ord(char) == ord('〇'):
            continue
        else:
            return False
    return True


def changeFreq_custWubiCodes():
    lines = read_multi_line_input()
    chars_to_change = []
    words_to_change = []
    phrases_to_change = []
    for i in range(len(lines)):
        if len(lines[i]) == 1:
            if judge_inputString_in_cjkv_bsc_and_a_and_cmp(
                    lines[i][0]) is True:
                chars_to_change.append(lines[i])
            else:
                phrases_to_change.append(lines[i])
        elif len(lines[i]) > 1:
            if judge_inputString_in_cjkv_bsc_and_a_and_cmp(
                    lines[i][0]) is True:
                words_to_change.append(lines[i])
            else:
                phrases_to_change.append(lines[i])

    return None


if __name__ == "__main__":
    startTime = time.time()
    print('{}'.format(startTime))

    generate_outputFiles()

    endTime = time.time()
    print('{}'.format(endTime))
    print('{}'.format(endTime - startTime))
