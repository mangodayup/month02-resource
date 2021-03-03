"""
正则表达式 re模块 2
"""

import re

text = "  Alex:1996,Sunny:1998"

# 返回一个迭代对象
result = re.finditer("\w+",text)

# 每次迭代获取一处对应匹配到的match对象
for item in result:
    print(item.group())


# 匹配第一处符合规则的
# result = re.search("(\w+):(?P<year>\d+)",text)
# print(result.group())
# print(result.group(1))
# print(result.group("year"))



# 匹配目标字符串开头位置
# result = re.match("\w+:\d+",text)
# print(result) # match对象
# print(result.span()) # text[0:9] 是匹配到的
# print(result.group()) # 对应的内容