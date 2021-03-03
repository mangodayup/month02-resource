"""
练习01：
编写一个函数，参数是一个单词，查询这个单词的
解释
提示： 考虑到查找不到的情况
      split()
"""

def find_word(word):
    """
    :param word: 要查找的单词
    :return: 该单词的解释 None
    """
    file = open("dict.txt") # 默认读
    # 每次提取一行
    for line in file:
        tmp = line.split(' ',1)
        # 如果遍历到的单词已经大于word就不用再找了
        if tmp[0] > word:
            file.close()
            return
        elif word == tmp[0]:
            file.close()
            return tmp[1].strip() # 去除字符串两侧空格

print(find_word("zzz"))