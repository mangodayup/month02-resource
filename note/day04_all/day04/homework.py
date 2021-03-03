"""
有一个列表，列表是一些正确的
文本文件的位置，现在需要编写一个程序
将这些文件合并为一个（名字自取）

[
"../day01/1.txt",
"../day02/2.txt",
]
"""
files = [
    "../day01/1.txt",
    "../day02/2.txt",
    "../day03/3.txt"
]


def union_file(files):
    """
    合并列表中的文件
    :param files: 文件列表
    """
    fw = open("union.txt", 'w')
    for file in files:
        # fw = open("union.txt", 'a')
        with open(file) as fr:
            fw.write(fr.read())
    fw.close()


union_file(files)
