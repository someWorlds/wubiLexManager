#! c:/Program Files/Python310/python.exe
# author: someWorlds
# encoding: UTF-8
# 词库的汉字的范围：cjkv_bsc + cjkv_a + cjkv_cmp(〇)

import time


class wubiLexManager:

    def __init__(self, withPi: bool = False):
        self.withPi = withPi  # 默认无私人信息
        self.msWubiLex = self.read_msWubiLex()
        self.chars_cjkv = self.read_cjkv()
        self.chars_1keySim = self.read_chars_1keySim()
        self.chars_2keySim = self.read_chars_2keySim()
        self.chars_3keySim = self.read_chars_3keySim()
        self.chars_3keyFull = self.read_chars_3keyFull()
        self.chars_4keyFull = self.read_chars_4keyFull()
        self.words_1keySim = self.read_words_1keySim()
        self.words_2keySim = self.read_words_2keySim()
        self.words_3keySim = self.read_words_3keySim()
        self.words_4keyFull = self.read_words_4keyFull()
        self.words_pi = self.read_words_pi()
        self.syms = self.read_syms()
        self.syms_pi = self.read_syms_pi()
        self.chars2incFreq_1or2keySim = self.read_chars2incFreq_1or2keySim()
        self.chars2incFreq_3keySim = self.read_chars2incFreq_3keySim()
        self.custWubiLex = self.get_custWubiLex()

    inputLines = []
    Freq = {
        'word_new': '30000',  # 自添加但是ms中没有的词，用该频率
        'char_inc': '50700',  # 对于一些简码字，将其除最简码外的频率增加到50700档位
        'syms': '50800',  # 符号类的自定义短语，将其频率设置到50800档位。一些字词容错码也按短语处理。
        # 'cjkv_b': '51000',  # cjkv的其它字，频率档位更高，
        # 'cjkv_c': '52000',  # 目前未添加cjkv_b及以下的字符。
        # 'cjkv_d': '53000',
        # 'cjkv_e': '54000',
        # 'cjkv_f': '55000',
        # 'cjkv_g': '56000',
        # 'cjkv_h': '57000',
        # 'cjkv_i': '58000',
    }
    msFreqMax = '50646'  # 微软五笔词库的最大频率

    def read_msWubiLex(self):
        msWubiLex = []
        with open("./refWubiLex/msWubiLex.yaml", 'r',
                  encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                if line[0] != '#' and line[0] != '\n':
                    msWubiLex.append(line.split())
        return msWubiLex

    def read_cjkv(self):
        # 字范围：cjkv_bsc + a + cmp
        chars_cjkv = []
        with open("./refWubiLex/cjkv_bsc.yaml", 'r', encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                if line[0] != '#' and line[0] != '\n':
                    temp = line.split()
                    chars_cjkv.append([temp[2], temp[1]])
        with open("./refWubiLex/cjkv_a.yaml", 'r', encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                if line[0] != '#' and line[0] != '\n':
                    temp = line.split()
                    chars_cjkv.append([temp[2], temp[1]])
        with open("./refWubiLex/cjkv_cmp.yaml", 'r', encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                if line[0] != '#' and line[0] != '\n':
                    temp = line.split()
                    chars_cjkv.append([temp[2], temp[1]])
        return chars_cjkv

    def read_chars_1keySim(self):
        chars_1keySim = []
        with open("./custWubiLex/chars_1keySim.yaml", 'r',
                  encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                if line[0] != '#' and line[0] != '\n':
                    chars_1keySim.append(line.split())
        return chars_1keySim

    def read_chars_2keySim(self):
        chars_2keySim = []
        with open("./custWubiLex/chars_2keySim.yaml", 'r',
                  encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                if line[0] != '#' and line[0] != '\n':
                    chars_2keySim.append(line.split())
        return chars_2keySim

    def read_chars_3keySim(self):
        chars_3keySim = []
        with open("./custWubiLex/chars_3keySim.yaml", 'r',
                  encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                if line[0] != '#' and line[0] != '\n':
                    chars_3keySim.append(line.split())
        return chars_3keySim

    def read_chars_3keyFull(self):
        chars_3keyFull = []
        with open("./custWubiLex/chars_3keyFull.yaml", 'r',
                  encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                if line[0] != '#' and line[0] != '\n':
                    chars_3keyFull.append(line.split())
        return chars_3keyFull

    def read_chars_4keyFull(self):
        chars_4keyFull = []
        with open("./custWubiLex/chars_4keyFull.yaml", 'r',
                  encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                if line[0] != '#' and line[0] != '\n':
                    chars_4keyFull.append(line.split())
        return chars_4keyFull

    def read_words_1keySim(self):
        words_1keySim = []
        try:
            with open("./custWubiLex/words_1keySim.yaml",
                      'r',
                      encoding='utf-8') as file:
                data = file.readlines()
                for line in data:
                    if line[0] != '#' and line[0] != '\n':
                        words_1keySim.append(line.split())
        except FileNotFoundError:
            None
        return words_1keySim

    def read_words_2keySim(self):
        words_2keySim = []
        try:
            with open("./custWubiLex/words_2keySim.yaml",
                      'r',
                      encoding='utf-8') as file:
                data = file.readlines()
                for line in data:
                    if line[0] != '#' and line[0] != '\n':
                        words_2keySim.append(line.split())
        except FileNotFoundError:
            None
        return words_2keySim

    def read_words_3keySim(self):
        words_3keySim = []
        try:
            with open("./custWubiLex/words_3keySim.yaml",
                      'r',
                      encoding='utf-8') as file:
                data = file.readlines()
                for line in data:
                    if line[0] != '#' and line[0] != '\n':
                        words_3keySim.append(line.split())
        except FileNotFoundError:
            None
        return words_3keySim

    def read_words_4keyFull(self):
        words_4keyFull = []
        with open("./custWubiLex/words_4keyFull.yaml", 'r',
                  encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                if line[0] != '#' and line[0] != '\n':
                    words_4keyFull.append(line.split())
        return words_4keyFull

    def read_words_pi(self):
        words_pi = []
        if not self.withPi:
            return words_pi
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

    def read_syms(self):
        symbols = []
        try:
            with open("./custWubiLex/syms.yaml", 'r',
                      encoding='utf-8') as file:
                data = file.readlines()
                for line in data:
                    if line[0] != '#' and line[0] != '\n':
                        symbols.append(line.split())
        except FileNotFoundError:
            None
        return symbols

    def read_syms_pi(self):
        syms_pi = []
        if not self.withPi:
            return syms_pi
        try:
            with open("./custWubiLex/syms_pi.yaml", 'r',
                      encoding='utf-8') as file:
                data = file.readlines()
                for line in data:
                    if line[0] != '#' and line[0] != '\n':
                        syms_pi.append(line.split())
        except FileNotFoundError:
            None
        return syms_pi

    def read_chars2incFreq_1or2keySim(self):
        chars2incFreq_1or2keySim = []
        try:
            with open("./custWubiLex/chars2incFreq_1or2keySim.yaml",
                      'r',
                      encoding='utf-8') as file:
                data = file.readlines()
                for line in data:
                    if line[0] != '#' and line[0] != '\n':
                        chars2incFreq_1or2keySim.append(line.split()[0])
        except FileNotFoundError:
            None
        return chars2incFreq_1or2keySim

    def read_chars2incFreq_3keySim(self):
        chars2incFreq_3keySim = []
        try:
            with open("./custWubiLex/chars2incFreq_3keySim.yaml",
                      'r',
                      encoding='utf-8') as file:
                data = file.readlines()
                for line in data:
                    if line[0] != '#' and line[0] != '\n':
                        chars2incFreq_3keySim.append(line.split()[0])
        except FileNotFoundError:
            None
        return chars2incFreq_3keySim

    def sortLex_by_Freq_and_code(self, lex: list):
        lex.sort(key=lambda x: int(x[2]))
        lex.sort(key=lambda x: x[0])
        return lex

    def write_lexFile(self):
        lexFile = [
            'chars_1keySim', 'chars_2keySim', 'chars_3keySim',
            'chars_3keyFull', 'chars_4keyFull', 'words_1keySim',
            'words_2keySim', 'words_3keySim', 'words_4keyFull', 'words_pi',
            'syms', 'syms_pi'
        ]
        if not self.withPi:
            lexFile.pop(lexFile.index('words_pi'))
            lexFile.pop(lexFile.index('syms_pi'))
        for fileName in lexFile:
            filePath = './custWubiLex/' + fileName + '.yaml'
            intro = []
            try:
                with open(filePath, 'r', encoding='utf-8') as file:
                    data = file.readlines()
                    for line in data:
                        if line[0] == '#':
                            intro.append(line)
            except FileNotFoundError:
                None
            with open(filePath, 'w', encoding='utf-8') as file:
                for term in intro:
                    file.write(term)
                file.write('\n')
                lex = eval('self.' + fileName)
                for term in lex:
                    file.write(term[0] + '    ' + term[1] + '    ' + term[2] +
                               '\n')

    def get_custWubiLex(self):
        temp = []
        temp.append(self.chars_1keySim)
        temp.append(self.chars_2keySim)
        temp.append(self.chars_3keySim)
        temp.append(self.chars_3keyFull)
        temp.append(self.chars_4keyFull)
        temp.append(self.words_1keySim)
        temp.append(self.words_2keySim)
        temp.append(self.words_3keySim)
        temp.append(self.words_4keyFull)
        temp.append(self.words_pi)
        temp.append(self.syms)
        temp.append(self.syms_pi)
        custWubiLex = []
        for i in range(len(temp)):
            if temp[i]:
                custWubiLex.extend(temp[i])
        if custWubiLex:
            custWubiLex = self.sortLex_by_Freq_and_code(custWubiLex)
        return custWubiLex

    def update_custWubiLex(self):
        self.custWubiLex = self.get_custWubiLex()

    def get_custWubiLex_chars(self):
        temp = []
        temp.append(self.chars_1keySim)
        temp.append(self.chars_2keySim)
        temp.append(self.chars_3keySim)
        temp.append(self.chars_3keyFull)
        temp.append(self.chars_4keyFull)
        custWubiLex_chars = []
        for i in range(len(temp)):
            if temp[i]:
                custWubiLex_chars.extend(temp[i])
        if custWubiLex_chars:
            custWubiLex_chars = self.sortLex_by_Freq_and_code(
                custWubiLex_chars)
        return custWubiLex_chars

    def get_custWubiLex_words(self, onMobile: bool = False):
        temp = []
        temp.append(self.words_4keyFull)
        if self.withPi:
            temp.append(self.words_pi)
        if onMobile:
            temp.append(self.words_1keySim)
            temp.append(self.words_2keySim)
            temp.append(self.words_3keySim)
        custWubiLex_words = []
        for i in range(len(temp)):
            if temp[i]:
                custWubiLex_words.extend(temp[i])
        if custWubiLex_words:
            custWubiLex_words = self.sortLex_by_Freq_and_code(
                custWubiLex_words)
        return custWubiLex_words

    def get_custWubiLex_phrases(self, onMobile: bool = False):
        temp = []
        if self.syms:
            temp.append(self.syms)
        if self.withPi:
            temp.append(self.syms_pi)
        if not onMobile:
            temp.append(self.words_1keySim)
            temp.append(self.words_2keySim)
            temp.append(self.words_3keySim)
        custWubiLex_phrases = []
        for i in range(len(temp)):
            if temp[i]:
                custWubiLex_phrases.extend(temp[i])
        if custWubiLex_phrases:
            custWubiLex_phrases = self.sortLex_by_Freq_and_code(
                custWubiLex_phrases)
        return custWubiLex_phrases

    def output_files_sgPy(self):
        # 生成导入PC搜狗拼音自定义短语的txt文件
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
        if self.withPi:
            filepath = "./outputFiles/sgPy_custPhrases_withPi.txt"
        else:
            filepath = "./outputFiles/sgPy_custPhrases.txt"
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(default_statement)
            num = 0
            for i in range(len(self.custWubiLex)):
                num += 1
                if 0 == i:
                    file.write(self.custWubiLex[i][0] + ',' + str(num) + '=' +
                               self.custWubiLex[i][1] + '\n')
                elif self.custWubiLex[i][0] == self.custWubiLex[i - 1][0]:
                    file.write(self.custWubiLex[i][0] + ',' + str(num) + '=' +
                               self.custWubiLex[i][1] + '\n')
                else:
                    num = 1
                    file.write(self.custWubiLex[i][0] + ',' + str(num) + '=' +
                               self.custWubiLex[i][1] + '\n')

    def output_files_mSg(self):
        # 生成导入手机搜狗输入法的自定义五笔方案的txt文件，以及常用语的csv文件
        if self.withPi:
            filepath = './outputFiles/mSg_custScheme_withPi.txt'
        else:
            filepath = './outputFiles/mSg_custScheme.txt'
        with open(filepath, 'w', encoding='utf-8') as file:
            temp = []
            temp.append(self.get_custWubiLex_chars())
            temp.append(self.get_custWubiLex_words(onMobile=True))
            custScheme = []
            for i in range(len(temp)):
                if temp[i]:
                    custScheme.extend(temp[i])
            custScheme = self.sortLex_by_Freq_and_code(custScheme)
            for i in range(len(custScheme)):
                file.write(custScheme[i][0] + '\t' + custScheme[i][1] + '\n')
        if self.withPi:
            filepath = './outputFiles/mSg_custPhrases_withPi.csv'
        else:
            filepath = './outputFiles/mSg_custPhrases.csv'
        with open(filepath, 'w', encoding='utf-8') as file:
            custPhrases = self.get_custWubiLex_phrases(onMobile=True)
            if custPhrases:
                custPhrases = self.sortLex_by_Freq_and_code(custPhrases)
            for term in custPhrases:
                file.write(term[0] + ',' + term[1] + '\n')

    def output_files_sgWb(self):
        # 生成导入PC搜狗五笔的自定义单字码表的txt文件、用户词库的txt文件、自定义短语的txt文件
        with open('./outputFiles/sgWb_custChars.txt', 'w',
                  encoding='utf-8') as file:
            custChars = self.get_custWubiLex_chars()
            for term in custChars:
                file.write(term[0] + '\t' + term[1] + '\n')
        if self.withPi:
            filepath = './outputFiles/sgWb_custWords_withPi.txt'
        else:
            filepath = './outputFiles/sgWb_custWords.txt'
        with open(filepath, 'w', encoding='utf-8') as file:
            custWords = self.get_custWubiLex_words()
            for term in custWords:
                file.write(term[0] + '\t' + term[1] + '\n')
        if self.withPi:
            filepath = './outputFiles/sgWb_custPhrases_withPi.txt'
        else:
            filepath = './outputFiles/sgWb_custPhrases.txt'
        with open(filepath, 'w', encoding='utf-8') as file:
            custPhrases = self.get_custWubiLex_phrases()
            for term in custPhrases:
                file.write(term[0] + '\t' + term[1] + '\n')

    def is_gbk(self, s):
        try:
            # 将字符串编码为字节序列
            bytes_data = s.encode()
            # 尝试用 GBK 进行解码
            bytes_data.decode('gbk')
            return bytes_data
        except UnicodeDecodeError:
            return False

    def contain_a_z(self, string: str):
        # 判断是否包含纯英文字母
        for char in string:
            if ord(char) in range(ord('a'), ord('z') + 1):
                return True
        return False

    def output_files_mBd_mi(self):
        # 生成导入手机百度输入法小米版的自定义方案的gbk格式的txt文件
        if self.withPi:
            filePath = './outputFiles/mBd_custScheme_mi_withPi.txt'
        else:
            filePath = './outputFiles/mBd_custScheme_mi.txt'
        with open(filePath, 'w', encoding='gbk') as file:
            for term in self.custWubiLex:
                try:
                    if not self.contain_a_z(term[1]):
                        file.write(term[1] + term[0] + '\n')
                except BaseException:
                    continue

    def output_files_mBd(self):
        # 生成导入手机百度输入法的自定义方案的txt文件
        if self.withPi:
            filePath = './outputFiles/mBd_custScheme_withPi.txt'
        else:
            filePath = './outputFiles/mBd_custScheme.txt'
        with open(filePath, 'w', encoding='utf-8') as file:
            line = self.custWubiLex[0][0] + '    ' + self.custWubiLex[0][1]
            code = self.custWubiLex[0][0]
            for term in self.custWubiLex[1:len(self.custWubiLex)]:
                if term[0] == code:
                    line += '    ' + term[1]
                else:
                    line += '\n'
                    file.write(line)
                    line = term[0] + '    ' + term[1]
                    code = term[0]
            if line[-1] != '\n':
                line += '\n'
                file.write(line)

    def generate_outputFiles(self):
        self.output_files_sgPy()
        self.output_files_mSg()
        self.output_files_sgWb()
        self.output_files_mBd_mi()
        self.output_files_mBd()

    def read_multi_line_input(self):
        print("""请输入多行词条:
示例: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
五笔      2
输入法
没        1   2
问题      2   2
五笔nice  1   n
五笔good  g
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
请输入===>>>>>>>(输入空行结束)>>>>>>>""")
        while True:
            line = input()
            if line == "":
                break
            self.inputLines.append(line.split())

    def is_cjkv(self, inputString: str):
        # 判断范围限于cjkv_bsc + cjkv_a + cjkv_cmp(〇)范围
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

    def find_in_lex(self,
                    code_and_string: list = [],
                    lex: list = [],
                    string: str = '',
                    code: str = ''):
        res = []
        if (lex == self.chars2incFreq_1or2keySim) or (
                lex == self.chars2incFreq_3keySim):
            if string in lex:
                res.append(string)
        elif lex:
            if string:  # 查找字词短语对应项
                res = list(filter(lambda x: x[1] == string, lex))
            elif code_and_string:  # 查找编码与字词短语都对应的项
                res = list(
                    filter(
                        lambda x: x[0] == code_and_string[0] and x[1] ==
                        code_and_string[1], lex))
            elif code:
                res = list(filter(lambda x: x[0] == code, lex))
        return res

    def del_in_lex(self, term_src: list = [], lex: list = []):
        if term_src and lex:
            lex.pop(lex.index(term_src))

    def add_in_lex(self, term_dst: list = [], lex: list = []):
        if term_dst:
            lex.append(term_dst)
            lex = self.sortLex_by_Freq_and_code(lex)

    def modify_in_lex(self,
                      term_src: list = [],
                      term_dst: list = [],
                      lex: list = []):
        self.del_in_lex(term_src, lex)
        self.add_in_lex(term_dst, lex)

    def calcCode(self, word: str, is_char_1keySim: bool = False):
        code = ''
        charList = []
        for char in word:
            res = self.find_in_lex(string=char, lex=self.chars_cjkv)
            if res:
                charList.append(res[-1])
        if charList:
            if len(word) == 1:  # 单字返回全码
                code += charList[0][0]
            elif len(word) == 2:  # 二字词
                code += charList[0][0][0:2] + charList[1][0][0:2]
            elif len(word) == 3:  # 三字词
                code = charList[0][0][0] + charList[1][0][0] + charList[2][0][
                    0:2]
            else:  # 四字及以上词
                code = charList[0][0][0] + charList[1][0][0] + charList[2][0][
                    0] + charList[-1][0][0]
        if is_char_1keySim:
            char_1keySim_err = {
                '我': 'q',
                '有': 'e',
                '不': 'i',
                '为': 'o',
                '这': 'p',
                '以': 'c',
                '发': 'v',
            }
            code = code[0]
            if word in char_1keySim_err.keys():
                code = char_1keySim_err[word]
        return code

    def is_0_9(self, string: str):
        # 判断是否是单个数字字符
        if len(string) == 1 and string.isdigit():
            return True
        else:
            return False

    def is_1_4(self, string: str):
        # 判断是否是1到4的单个数字字符
        if string in ['1', '2', '3', '4']:
            return True
        else:
            return False

    def is_a_z(self, string: str):
        # 判断是否是纯英文小写字母字符串
        for char in string:
            if ord(char) not in range(ord('a'), ord('z') + 1):
                return False
        return True

    def is_char_inc(self, lexName: str, char: str):
        if lexName == 'chars_3keySim':
            res = self.find_in_lex(string=char,
                                   lex=self.chars2incFreq_1or2keySim)
        elif lexName == 'chars_3keyFull':
            res = self.find_in_lex(string=char,
                                   lex=self.chars2incFreq_1or2keySim)
        elif lexName == 'chars_4keyFull':
            res = self.find_in_lex(string=char,
                                   lex=self.chars2incFreq_1or2keySim)
            if not res:
                res = self.find_in_lex(string=char,
                                       lex=self.chars2incFreq_3keySim)
        else:
            res = []
        return res

    def judge_termType(self, term_src: list):
        # term_src = [code, string, ...]
        termType = []
        if not self.is_cjkv(term_src[1]) or len(term_src[0]) > 4:
            termType.append('syms')
            termType.append(self.Freq['syms'])
            if self.find_in_lex(code_and_string=term_src, lex=self.syms_pi):
                termType[0] = 'syms_pi'
        else:
            code = self.calcCode(term_src[1])
            if code == term_src[0]:
                if len(term_src[1]) == 1:
                    if len(term_src[0]) == 3:
                        termType.append('chars_3keyFull')
                    else:
                        termType.append('chars_4keyFull')
                else:
                    termType.append('words_4keyFull')
                    if self.find_in_lex(code_and_string=term_src,
                                        lex=self.words_pi):
                        termType[0] = 'words_pi'
            elif code[0:2] == term_src[0]:
                if len(term_src[1]) == 1:
                    termType.append('chars_2keySim')
                else:
                    termType.append('words_2keySim')
            elif code[0:3] == term_src[0]:
                if len(term_src[1]) == 1:
                    termType.append('chars_3keySim')
                else:
                    termType.append('words_3keySim')
            elif self.find_in_lex(code_and_string=term_src,
                                  lex=self.chars_1keySim):
                termType.append('chars_1keySim')
            elif self.find_in_lex(code_and_string=term_src,
                                  lex=self.words_1keySim):
                termType.append('words_1keySim')
            else:
                termType.append('syms')
                if self.find_in_lex(code_and_string=term_src,
                                    lex=self.syms_pi):
                    termType[0] = 'syms_pi'
            res = self.find_in_lex(code_and_string=term_src,
                                   lex=self.msWubiLex)
            if not res:
                res = self.find_in_lex(string=term_src[1], lex=self.msWubiLex)
            if res:
                termType.append(res[-1][2])
            else:
                termType.append(self.Freq['word_new'])
            if termType[0] == 'syms' or termType[0] == 'syms_pi':
                termType[1] = (self.Freq['syms'])
            elif self.is_char_inc(lexName=termType[0], char=term_src[1]):
                termType[1] = self.Freq['char_inc']
        return termType

    def calcFreq(self, term_src: list, order: str = '9'):
        # term_src = [code, string, msFreq/self.Freq]
        freq = term_src[2]
        temp = self.find_in_lex(code=term_src[0], lex=self.custWubiLex)
        if temp:
            res = []
            for term in temp:
                res.append(term[:])
            res1 = self.find_in_lex(code_and_string=term_src,
                                    lex=self.custWubiLex)
            if res1:
                res.pop(res.index(res1[-1]))
            term_src.append(term_src[2])
            if order != '9':  # 直接用排序给目标项做位次标记
                term_src.append(int(order))
            else:  # 排序为'9'时，位次标记至少大于同等级词条
                maxFreq = 0
                if term_src[2] in self.Freq.values():
                    if term_src[2] == self.Freq['word_new']:
                        maxFreq = int(self.msFreqMax) + 20  # ms词的最大的频率
                    else:
                        maxFreq = int(term_src[2]) + 20
                else:
                    maxFreq = int(self.msFreqMax) + 20  # 增加20冗余量，以放到最后
                term_src.append(0.5)
                for i in range(len(res)):
                    if int(res[i][2]) <= maxFreq:
                        term_src[4] = i + 1.5
            mark = 1
            for i in range(len(res)):
                if i + 1 == int(order):
                    mark += 1
                termType = self.judge_termType(res[i])
                res[i].append(termType[1])  # 获取初始的频率
                res[i].append(i + mark)  # 给各项做位次标记
                res[i].append(termType[0])  # 标记需要很修改的码表名
            res.append(term_src)
            res.sort(key=lambda x: x[4])  # 按位次标记排序
            withMsFreq = -1  # 标记最后一个ms频率位置
            withCustFreq = -1  # 标记最后一个cust频率位置
            for i in range(len(res)):  # 将所有的ms频率项理顺
                if res[i][3] in self.Freq.values():
                    withCustFreq = i
                    continue
                withMsFreq = i
                for j in range(i + 1, len(res)):
                    if res[j][3] in self.Freq.values():
                        continue
                    else:
                        withMsFreq = j
                        break
                if withMsFreq != i and int(
                        res[i][3]) > int(res[withMsFreq][3]) - (j - i):
                    res[withMsFreq][3] = str(int(res[i][3]) + (j - i))
            if withCustFreq != -1:
                if withMsFreq != -1:
                    # 同时含ms和cust频率项时，根据ms频率项，将cust频率项理顺
                    for i in range(len(res)):
                        if res[i][3] in self.Freq.values():
                            withMsFreq = -1
                            for j in range(i + 1, len(res)):
                                if res[j][3] not in self.Freq.values():
                                    withMsFreq = j
                                    break
                            if withMsFreq != -1:
                                if int(res[i][3]) > int(
                                        res[withMsFreq][3]) - (withMsFreq - i):
                                    res[i][3] = str(
                                        int(res[withMsFreq][3]) -
                                        (withMsFreq - i))
                            if i > 0:
                                while int(res[i - 1][3]) >= int(res[i][3]):
                                    # 逆向频率变动为1
                                    res[i][3] = str(int(res[i][3]) + 1)
                else:  # 只含cust频率项时，直接理顺，频率增幅为1
                    for i in range(1, len(res)):
                        if int(res[i - 1][3]) >= int(res[i][3]):
                            res[i][3] = str(int(res[i - 1][3]) + 1)
            for term in res:
                if len(term) == 5:
                    freq = term[3]
                    continue
                elif term[2] != term[3]:
                    term_src = term[0:3]
                    term_dst = [term[0], term[1], term[3]]
                    lex = eval('self.' + term[5])
                    self.modify_in_lex(term_src=term_src,
                                       term_dst=term_dst,
                                       lex=lex)
        return freq

    def chgLex_by_line(self, line: list):
        if 1 == len(line):  # 输入只有一列
            if self.is_cjkv(line[0]):
                code = self.calcCode(line[0])
                res = self.find_in_lex(code_and_string=[code, line[0]],
                                       lex=self.custWubiLex)
                if res:  # 已存在，忽略
                    print('已存在该字词: {}'.format(line[0]))
                    return None
                res = self.find_in_lex(string=line[0], lex=self.msWubiLex)
                if res:
                    freq = res[-1][2]
                else:
                    freq = self.Freq['word_new']
                if len(line[0]) == 1:
                    if len(code) == 3:
                        lex = 'chars_3keyFull'
                    else:
                        lex = 'chars_4keyFull'
                else:
                    lex = 'words_4keyFull'
                if self.is_char_inc(lexName=lex, char=line[0]):
                    freq = self.Freq['char_inc']
                term_dst = [code, line[0], freq]
                self.add_in_lex(term_dst=term_dst, lex=eval('self.' + lex))
            else:
                print('非法输入: {}'.format(line[0]))
                return None
        elif 2 == len(line):  # 输入有两列，字+排序，词+排序，短语+排序，短语+编码
            if self.is_a_z(line[1]):  # 短语+编码
                res = self.find_in_lex(code_and_string=[line[1], line[0]],
                                       lex=self.custWubiLex)
                if res:  # 短语已存在
                    return None
                else:  # 短语，添加
                    term_dst = [line[1], line[0], self.Freq['syms']]
                    self.add_in_lex(term_dst=term_dst, lex=self.syms)
            elif self.is_0_9(line[1]):  # 字/词/短语+排序
                res = self.find_in_lex(string=line[0], lex=self.syms)
                if not res:
                    res = self.find_in_lex(string=line[0], lex=self.syms_pi)
                if res:  # 对存在的短语进行操作
                    term_src = res[-1]
                    code = res[-1][0]
                    Freq = self.Freq['syms']
                    lex = 'syms'
                elif not self.is_cjkv(line[0]):  # 短语不存在时，报错，缺少编码
                    print('输入缺少编码: {}'.format(line[0] + '\t' + line[1]))
                    return None
                else:  # 其它情况按全码字词处理
                    code = self.calcCode(line[0])
                    res = self.find_in_lex(code_and_string=[code, line[0]],
                                           lex=self.custWubiLex)
                    if not res and line[1] == '0':  # 全码不存在，删除则报错
                        print('字词全码不存在: {}'.format(line[0] + '\t' + line[1]))
                        return None
                    elif res:
                        term_src = res[-1]
                    else:
                        term_src = []
                    res = self.find_in_lex(code_and_string=[code, line[0]],
                                           lex=self.msWubiLex)
                    if not res:
                        res = self.find_in_lex(string=line[0],
                                               lex=self.msWubiLex)
                    if res:
                        Freq = res[-1][2]
                    else:
                        Freq = self.Freq['word_new']
                    if len(line[0]) == 1:
                        if len(code) == 3:
                            lex = 'chars_3keyFull'
                        else:
                            lex = 'chars_4keyFull'
                    else:
                        lex = 'words_4keyFull'
                    if self.is_char_inc(lexName=lex, char=line[0]):
                        Freq = self.Freq['char_inc']
                if line[1] == '0':
                    term_dst = []
                else:
                    freq = self.calcFreq(term_src=[code, line[0], Freq],
                                         order=line[1])
                    term_dst = [code, line[0], freq]
                try:
                    self.modify_in_lex(term_src=term_src,
                                       term_dst=term_dst,
                                       lex=eval('self.' + lex))
                except ValueError:
                    try:
                        self.modify_in_lex(term_src=term_src,
                                           term_dst=term_dst,
                                           lex=self.words_pi)
                    except ValueError:
                        self.modify_in_lex(term_src=term_src,
                                           term_dst=term_dst,
                                           lex=self.syms_pi)
            else:
                print('非法输入: {}'.format(line[0] + '\t' + line[1]))
                return None
        elif 3 == len(line):  # 输入有三列，字+排序+码数，词+排序+码数，短语+排序+编码，短语+编码+排序
            if self.is_0_9(line[1]) and self.is_1_4(line[2]):
                if not self.is_cjkv(line[0]):
                    print('非法输入: {}'.format(line[0] + '\t' + line[1] + '\t' +
                                            line[2]))
                    return None
                code1 = self.calcCode(word=line[0])
                code = code1[0:int(line[2])]
                if line[2] == '1' and len(line[0]) == 1:
                    code = self.calcCode(word=line[0], is_char_1keySim=True)
                    lex = 'chars_1keySim'
                elif line[2] == '1':
                    lex = 'words_1keySim'
                elif line[2] == '2':
                    if len(line[0]) == 1:
                        lex = 'chars_2keySim'
                    else:
                        lex = 'words_2keySim'
                elif line[2] == '3':
                    if len(line[0]) == 1:
                        if len(code1) == 3:
                            lex = 'chars_3keyFull'
                        else:
                            lex = 'chars_3keySim'
                    else:
                        lex = 'words_3keySim'
                else:
                    if len(line[0]) == 1:
                        lex = 'chars_4keyFull'
                    else:
                        lex = 'words_4keyFull'
                res = self.find_in_lex(code_and_string=[code, line[0]],
                                       lex=self.custWubiLex)
                if line[1] == '0':
                    if res:
                        term_src = res[-1]
                        term_dst = []
                    else:
                        print('该字词不存在: {}'.format(line[0] + '\t' + line[1] +
                                                  '\t' + line[2]))
                        return None
                else:
                    if res:
                        term_src = res[-1]
                    else:
                        term_src = []
                    res = self.find_in_lex(code_and_string=[code, line[0]],
                                           lex=self.msWubiLex)
                    if not res:
                        res = self.find_in_lex(string=line[0],
                                               lex=self.msWubiLex)
                    if res:
                        Freq = res[-1][2]
                    else:
                        Freq = self.Freq['word_new']
                    if self.is_char_inc(lexName=lex, char=line[0]):
                        Freq = self.Freq['char_inc']
                    freq = self.calcFreq(term_src=[code, line[0], Freq],
                                         order=line[1])
                    term_dst = [code, line[0], freq]
            elif (self.is_0_9(line[1])
                  and self.is_a_z(line[2])) or (self.is_0_9(line[2])
                                                and self.is_a_z(line[1])):
                lex = 'syms'
                if self.is_0_9(line[1]):
                    code = line[2]
                    order = line[1]
                else:
                    code = line[1]
                    order = line[2]
                res = self.find_in_lex(code_and_string=[code, line[0]],
                                       lex=self.custWubiLex)
                if order == '0':
                    if res:
                        term_src = res[-1]
                        term_dst = []
                    else:
                        print('该短语不存在: {}'.format(line[0] + '\t' + line[1] +
                                                  '\t' + line[2]))
                        return None
                else:
                    if res:
                        term_src = res[-1]
                    else:
                        term_src = []
                    Freq = self.Freq['syms']
                    freq = self.calcFreq(term_src=[code, line[0], Freq],
                                         order=order)
                    term_dst = [code, line[0], freq]
            else:
                print('非法输入: {}'.format(line[0] + '\t' + line[1] + '\t' +
                                        line[2]))
                return None
            try:
                self.modify_in_lex(term_src=term_src,
                                   term_dst=term_dst,
                                   lex=eval('self.' + lex))
            except ValueError:
                try:
                    self.modify_in_lex(term_src=term_src,
                                       term_dst=term_dst,
                                       lex=self.words_pi)
                except ValueError:
                    self.modify_in_lex(term_src=term_src,
                                       term_dst=term_dst,
                                       lex=self.syms_pi)

    def process_input(self):
        self.read_multi_line_input()
        for line in self.inputLines:
            self.chgLex_by_line(line=line)
            self.update_custWubiLex()
        self.write_lexFile()
        self.generate_outputFiles()

    def freqInc(self):
        for char in self.chars2incFreq_1or2keySim:
            for term in self.chars_3keySim:
                if term[1] == char:
                    term[2] = self.Freq['char_inc']
            for term in self.chars_3keyFull:
                if term[1] == char:
                    term[2] = self.Freq['char_inc']
            for term in self.chars_4keyFull:
                if term[1] == char:
                    term[2] = self.Freq['char_inc']
        for char in self.chars2incFreq_3keySim:
            for term in self.chars_4keyFull:
                if term[1] == char:
                    term[2] = self.Freq['char_inc']


if __name__ == "__main__":
    startTime = time.time()
    print('{}'.format(startTime))

    # wubi = wubiLexManager(True)
    # wubi.freqInc()
    # wubi.write_lexFile()

    endTime = time.time()
    print('{}'.format(endTime))
    print('{}'.format(endTime - startTime))
