"""
正则表达式 re模块示例
"""
import re

text = "Alex:1996,Sunny:1998"

# 使用“  ” 替换匹配到的内容
msg = re.sub("\W+","##",text,2)
print(msg)

# 使用\W+匹配内容切割 text
# result = re.split('\W+',text,2)
# print(result)

# 使用正则表达式匹配字符串中符合规则的部分
# 如果正则表达式有组，则只能返回组对应的匹配部分
# result = re.findall("(\w+):(\d+)",text)
# print(result)

