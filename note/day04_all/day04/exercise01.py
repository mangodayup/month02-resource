"""
基于inet.log完成： 编程一个程序
通过输入一个 网络接口名称 得到这个
接口对应运行状态中的 address is的值

思路：
1. 利用文件处理技术，根据输入得到目标段落
2. 在确定好的这段文字中进行匹配
"""
import re


# 判断一段是否为目标段落
def match_info(data):
    # 提取首个单词
    head = re.match("\S+", data).group()
    if iport == head:
        return data


# 将文档的每段提取出来提供给别人 (生成器)
def split_info():
    # 读方法打开
    file = open("inet.log")
    while True:
        data = ""  # 存储一段内容
        for line in file:
            # 遇到空行结束循环
            if line == "\n":
                break
            data += line
        if data:
            yield data  # 提供一段内容
        else:
            file.close()
            return


# 入口函数
def main():
    # 获取每一段内容
    for info in split_info():
        #　ｄａｔａ->None　说明不是这一段
        data = match_info(info)
        if data:
            result = re.search("([0-9a-f]{4}\.){2}[0-9a-f]{4}", data)
            return result.group()


if __name__ == '__main__':
    iport = input("网络接口名称:")
    print(main())
