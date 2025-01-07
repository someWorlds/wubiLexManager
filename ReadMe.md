# 五笔输入方案管理
## 简介
五笔输入方案管理器，用于编辑五笔码表，并导出特定格式文件挂接到其它软件中，如搜狗拼音自定义短语格式、手机搜狗输入法的五笔的自定义方案格式、搜狗五笔格式等。

> 1. 内含方案为86五笔方案，包含汉字范围为cjkv基本区、扩展a区和标点区补充的“〇”（已校对）。参考码表含其它区汉字（未校对），有需求可自由添加。
> 2. 字根图基于86五笔方案，加入部分繁体字根，并修正错误字根，e.g. 麸 gqfw $\to$ gtfw，囱 tlq $\to$ tlt。
> ![五笔字根表](./images/wubiRadicals_86_加入繁体字根_易读版.jpg)

## 功能
- 添加新编码
- 删除现有编码
- 修改编码候选排序
- 导出码表文件（后缀withPi，表示含个人信息词汇的文件版本）
    - 导入PC搜狗拼音自定义短语格式（custPhrases_sogouPy.txt，custPhrases_sogouPy_withPi.txt）
    - 导入Android搜狗五笔格式
        - 导入自定义五笔码表（custScheme_mobileSogou.txt，custScheme_mobileSogou_withPi.txt）
        - 导入常用语（custPhrases_mobileSogou.csv，custPhrases_mobileSogou_withPi.csv）
    - 导入PC搜狗五笔格式
        - 导入自定义码表（custChars_sogouWb.txt）
        - 导入用户词汇（custWords_sogouWb.txt，custWords_sogouWb_withPi.txt）
        - 导入自定义短语（custPhrases_sogouWb.txt，custPhrases_sogouWb_withPi.txt）
- 个人信息词汇与短语，可分别在custWubiLex\syms_pi.yaml与custWubiLex\words_pi.yaml两个文件中添加。