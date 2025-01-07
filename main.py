#! c:/Program Files/Python310/python.exe
# author: someWorlds
# encoding: UTF-8

import time


def Freq(stringType: str):
    freq_default = {
        'word_max': '50646',  # cjkv_bsc、a和cmp范围的字词，最大频率设为50646
        'char_max': '50700',  # 对于一些简码字，将其除最简码外的频率增加到50700档位
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
    return freq_default[stringType]


def read_msWubiLex():
    msWubiLex = []
    with open("./refWubiLex/msWubiLex.yaml", 'r', encoding='utf-8') as file:
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
    with open("./custWubiLex/chars_1keySim.yaml", 'r',
              encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                chars_1keySim.append(line.split())
    return chars_1keySim


def read_chars_2keySim():
    chars_2keySim = []
    with open("./custWubiLex/chars_2keySim.yaml", 'r',
              encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                chars_2keySim.append(line.split())
    return chars_2keySim


def read_chars_3keySim():
    chars_3keySim = []
    with open("./custWubiLex/chars_3keySim.yaml", 'r',
              encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                chars_3keySim.append(line.split())
    return chars_3keySim


def read_chars_3keyFull():
    chars_3keyFull = []
    with open("./custWubiLex/chars_3keyFull.yaml", 'r',
              encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                chars_3keyFull.append(line.split())
    return chars_3keyFull


def read_chars_4keyFull():
    chars_4keyFull = []
    with open("./custWubiLex/chars_4keyFull.yaml", 'r',
              encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                chars_4keyFull.append(line.split())
    return chars_4keyFull


def read_syms_pi():
    syms_pi = []
    try:
        with open("./custWubiLex/syms_pi.yaml", 'r', encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                if line[0] != '#' and line[0] != '\n':
                    syms_pi.append(line.split())
    except FileNotFoundError:
        None
    return syms_pi


def read_syms():
    symbols = []
    try:
        with open("./custWubiLex/syms.yaml", 'r', encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                if line[0] != '#' and line[0] != '\n':
                    symbols.append(line.split())
    except FileNotFoundError:
        None
    return symbols


def read_words_2keySim():
    words_2keySim = []
    try:
        with open("./custWubiLex/words_2keySim.yaml", 'r',
                  encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                if line[0] != '#' and line[0] != '\n':
                    words_2keySim.append(line.split())
    except FileNotFoundError:
        None
    return words_2keySim


def read_words_4keyFull():
    words_4keyFull = []
    with open("./custWubiLex/words_4keyFull.yaml", 'r',
              encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line[0] != '#' and line[0] != '\n':
                words_4keyFull.append(line.split())
    return words_4keyFull


def read_words_pi():
    words_pi = []
    try:
        with open("./custWubiLex/words_pi.yaml", 'r',
                  encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                if line[0] != '#' and line[0] != '\n':
                    words_pi.append(line.split())
    except FileNotFoundError:
        None
    return words_pi


def get_custWubiLex(withPi: bool = False):
    custWubiLex = []
    custWubiLex.extend(read_chars_1keySim())
    custWubiLex.extend(read_chars_2keySim())
    custWubiLex.extend(read_chars_3keySim())
    custWubiLex.extend(read_chars_3keyFull())
    custWubiLex.extend(read_chars_4keyFull())
    symbols = read_syms()
    if symbols is not []:
        custWubiLex.extend(symbols)
    words_2keySim = read_words_2keySim()
    if words_2keySim is not []:
        custWubiLex.extend(words_2keySim)
    custWubiLex.extend(read_words_4keyFull())
    if withPi is True:
        syms_pi = read_syms_pi()
        if syms_pi is not []:
            custWubiLex.extend(syms_pi)
        words_pi = read_words_pi()
        if words_pi is not []:
            custWubiLex.extend(words_pi)
    custWubiLex.sort(key=lambda x: int(x[2]))
    custWubiLex.sort(key=lambda x: x[0])
    return custWubiLex


def get_custWubiLex_chars():
    custWubiLex_chars = []
    custWubiLex_chars.extend(read_chars_1keySim())
    custWubiLex_chars.extend(read_chars_2keySim())
    custWubiLex_chars.extend(read_chars_3keySim())
    custWubiLex_chars.extend(read_chars_3keyFull())
    custWubiLex_chars.extend(read_chars_4keyFull())
    custWubiLex_chars.sort(key=lambda x: int(x[2]))
    custWubiLex_chars.sort(key=lambda x: x[0])
    return custWubiLex_chars


def get_custWubiLex_words(withPi: bool = False, onMobile: bool = False):
    custWubiLex_words = []
    custWubiLex_words.extend(read_words_4keyFull())
    if withPi is True:
        words_pi = read_words_pi()
        if words_pi is not []:
            custWubiLex_words.extend(words_pi)
    if onMobile is True:
        words_2keySim = read_words_2keySim()
        if words_2keySim is not []:
            custWubiLex_words.extend(words_2keySim)
    custWubiLex_words.sort(key=lambda x: int(x[2]))
    custWubiLex_words.sort(key=lambda x: x[0])
    return custWubiLex_words


def get_custWubiLex_phrases(withPi: bool = False, onMobile: bool = False):
    custWubiLex_phrases = []
    symbols = read_syms()
    if symbols is not []:
        custWubiLex_phrases.extend(symbols)
    if withPi is True:
        syms_pi = read_syms_pi()
        if syms_pi is not []:
            custWubiLex_phrases.extend(syms_pi)
    if onMobile is False:
        words_2keySim = read_words_2keySim()
        if words_2keySim is not []:
            custWubiLex_phrases.extend(words_2keySim)
    custWubiLex_phrases.sort(key=lambda x: int(x[2]))
    custWubiLex_phrases.sort(key=lambda x: x[0])
    return custWubiLex_phrases


def output_files_sogouPy():
    # 生成导入PC搜狗拼音自定义短语的txt文件
    filepath = [
        "./outputFiles/custPhrases_sogouPy.txt",
        "./outputFiles/custPhrases_sogouPy_withPi.txt"
    ]
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
    for i in range(len(filepath)):
        custWubiLex = get_custWubiLex(withPi=bool(i))
        with open(filepath[i], 'w', encoding='utf-8') as file:
            file.write(default_statement)
            num = 0
            for i in range(len(custWubiLex)):
                num += 1
                if 0 == i or custWubiLex[i][0] == custWubiLex[i - 1][0]:
                    file.write(custWubiLex[i][0] + ',' + str(num) + '=' +
                               custWubiLex[i][1] + '\n')
                else:
                    num = 1
                    file.write(custWubiLex[i][0] + ',' + str(num) + '=' +
                               custWubiLex[i][1] + '\n')


def output_files_mobileSogou():
    # 生成导入手机搜狗输入法的自定义五笔方案的txt文件，以及常用语的csv文件
    filepaths = [
        './outputFiles/custScheme_mobileSogou.txt',
        './outputFiles/custScheme_mobileSogou_withPi.txt'
    ]
    for i in range(len(filepaths)):
        with open(filepaths[i], 'w', encoding='utf-8') as file:
            custWubiLex = get_custWubiLex_chars()
            custWubiLex.extend(
                get_custWubiLex_words(withPi=bool(i), onMobile=True))
            custWubiLex.sort(key=lambda x: int(x[2]))
            custWubiLex.sort(key=lambda x: x[0])
            for i in range(len(custWubiLex)):
                file.write(custWubiLex[i][0] + '\t' + custWubiLex[i][1] + '\n')
    filepaths = [
        './outputFiles/custPhrases_mobileSogou.csv',
        './outputFiles/custPhrases_mobileSogou_withPi.csv'
    ]
    for i in range(len(filepaths)):
        with open(filepaths[i], 'w', encoding='utf-8') as file:
            custWubiLex = get_custWubiLex_phrases(withPi=bool(i),
                                                  onMobile=True)
            custWubiLex.sort(key=lambda x: int(x[2]))
            custWubiLex.sort(key=lambda x: x[0])
            for i in range(len(custWubiLex)):
                custWubiLex[i].pop(2)
                file.writelines(','.join(map(str, custWubiLex[i])) + '\n')


def output_files_sogouWb():
    # 生成导入PC搜狗五笔的自定义单字码表的txt文件、用户词库的txt文件、自定义短语的txt文件
    filepaths = [
        './outputFiles/custChars_sogouWb.txt',
        './outputFiles/custWords_sogouWb.txt',
        './outputFiles/custPhrases_sogouWb.txt',
        './outputFiles/custWords_sogouWb_withPi.txt',
        './outputFiles/custPhrases_sogouWb_withPi.txt',
    ]
    for i in range(len(filepaths)):
        with open(filepaths[i], 'w', encoding='utf-8') as file:
            if i == 0:
                custWubiLex = get_custWubiLex_chars()
            else:
                custWubiLex = get_custWubiLex_words(withPi=bool((i - 1) // 2),
                                                    onMobile=False)
            for i in range(len(custWubiLex)):
                file.write(custWubiLex[i][0] + '\t' + custWubiLex[i][1] + '\n')


def generate_outputFiles():
    output_files_sogouPy()
    output_files_mobileSogou()
    output_files_sogouWb()
    return None


def read_multi_line_input():
    print("""
        请输入多行字符串（输入空行结束）：
        示例1：您好              # 根据微软五笔码表，添加全码，生成频率和排序
        示例2：您好    2         # 指定全码排在候选第2位
        示例4：它好    0         # 删除全码
        示例5：饱      9         # 全码排序置后
        示例6：我#*m@  sb        # 添加自定义短语，默认排序置后
        示例7：我#*m@  sb  2     # 添加自定义短语，指定排序第2位
        示例8：我#*m@  2   sb    # 添加自定义短语，指定排序第2位
        示例9：我#*m@  2         # 更改自定义短语排序至第2位，无词条则报错
        示例3：其实    1   2     # 指定二码排在候选第1位
        """)
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


def find_inputLine_in_lex(inputLine: list, wubiLex: list, matchType: int = 1):
    """matchType值控制匹配类型：0，精确匹配词条，以及其编码；
    1，精确匹配词条，只返回第一个匹配结果；2，精确匹配词条，返回所有结果；
    3，模糊匹配含有词条的项。"""
    matchRes = []
    if 1 == matchType:
        for i in range(len(wubiLex)):
            if inputLine[0] == wubiLex[i][1]:
                matchRes.append(wubiLex[i])
                return matchRes
    elif 0 == matchType:
        for i in range(len(wubiLex)):
            if inputLine[0] == wubiLex[i][1] and int(inputLine[2]) == len(
                    wubiLex[i][0]):
                matchRes.append(wubiLex[i])
    elif 2 == matchType:
        for i in range(len(wubiLex)):
            if inputLine[0] == wubiLex[i][1]:
                matchRes.append(wubiLex[i])
    elif 3 == matchType:
        for i in range(len(wubiLex)):
            if inputLine[0] in wubiLex[i][1]:
                matchRes.append(wubiLex[i])
    return matchRes


def find_inputLine_in_cjkv(inputLine: list):
    matchRes = []
    return matchRes

def find_inputLine_in_chars_full(inputLine: list):
    matchRes = []
    return matchRes


def write_custLexFile(custLexName: str, code: str, inputString: str,
                      freq: str):
    filePath = './custWubiLex/' + custLexName + '.yaml'
    with open(filePath, 'w+', encoding='utf-8') as file:
        custLex = [line.split() for line in file.readlines()]
        custLex.append([code, inputString, freq])
        custLex.sort(key=lambda x: int(x[2]))
        custLex.sort(key=lambda x: x[0])
        for i in range(len(custLex)):
            file.writelines(custLex[i][0] + '    ' + custLex[i][1] + '    ' +
                            custLex[i][2])


def change_custWubiLex(inputLines: list, custWubiLex: list, msWubiLex: list):
    inputLines = read_multi_line_input()
    for i in range(len(inputLines)):
        if judge_inputString_in_cjkv_bsc_and_a_and_cmp(
                inputLines[i][0]) is True:
            if len(inputLines[i]) == 1:
                if find_inputLine_in_lex(inputLine=inputLines[i],
                                         wubiLex=custWubiLex,
                                         matchType=1) is not []:
                    continue
                elif len(inputLines[i][0]) == 1:
                    matchRes = find_inputLine_in_cjkv(inputLines[i])
                    write_custLexFile(custLexName='chars_4keyFull',
                                      code=matchRes[0][0],
                                      inputString=inputLines[i][0],
                                      freq=matchRes[0][2])

                else:
                    matchRes = find_inputLine_in_lex(inputLine=inputLines[i],
                                                     wubiLex=msWubiLex,
                                                     matchType=1)
                    if matchRes is []:
                        freq = Freq('word_max')
                        code = creat_code_by_chars_full(inputLines[i][0])
                    else:
                        freq = matchRes[0][2]
                        code = matchRes[0][0]
                    write_custLexFile(custLexName='words_4keyFull',
                                      code=code,
                                      inputString=inputLines[i][0],
                                      freq=freq)
            elif 2 == len(inputLines[i]):
                if '0' == inputLines[i][1]:
                    del_custLexFile(inputLines[i][0])
                elif len(inputLines[i][0]) == 1:
                    if '9'==inputLines[i][1]:
                        matchRes = find_inputLine_in_chars_full(inputLine=inputLines[i])
                        
                    else:
                else:
                    if '9'==inputLines[i][1]:
                    else:

            elif 3==len(inputLines[i]):
                matchRes = find_inputLine_in_lex(inputLine=inputLines[i],
                                                wubiLex=custWubiLex,
                                                matchType=0)
                if inputLines[i][2] == '1':
                    custLexName = 'chars_1keySim'
                elif inputLines[i][2] == '2':
                    custLexName = 'chars_2keySim'
                elif inputLines[i][2] == '3':
                    custLexName = 'chars_3keySim'
                freq = calc_freq
            else:
                matchRes = find_inputLine_in_cjkv(inputLine=inputLines[i])
                if len(matchRes[0][0]) == 3:
                    custLexName = 'chars_3keyFull'
                else:
                    custLexName = 'chars_4keyFull'

                if len(inputLines[i][0]) == 1:
                    custLexName = 'chars_4keyFull'
                else:
                    custLexName = 'words_4keyFull'
                write_custLexFile(custLexName=custLexName, code=g)
        else:
            None

    return None


if __name__ == "__main__":
    startTime = time.time()
    print('{}'.format(startTime))

    generate_outputFiles()

    endTime = time.time()
    print('{}'.format(endTime))
    print('{}'.format(endTime - startTime))
