# eval的用法
# 1.以Python表达式的方式解析并执行字符串，并将返回结果输出。
# def func():
#     return 1+1+1
#
# print(eval('func()'))

# 2.可以把list,tuple,dict和string相互转化。
# 字符串 -->列表
# a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
# print("a-->str:",a)
# print(type(a))
# print("a-->list:",eval(a))
#
# print(type(eval(a)))

# 字符串 -->字典
# b = "{1: 'a', 2: 'b'}"
# print(type(b))
# print(eval(b))
# print(type(eval(b)))


# 字符串 -->元组;
# c = "([1,2], [3,4], [5,6], [7,8], (9,0))"
# print(type(c))
# print(eval(c))
# print(type(eval(c)))






# Python中format函数用法   %s,f{},.format()

age = 25
name = 'kimiy'
# print("*"*50)
print('{} is {} years old. '.format(age, name))  # 输出参数
print('{} 的年龄是 {}  '.format(name, age))  # 输出参数
print('{0} is a girl. '.format(name))
print('{0:.3} is a decimal. '.format(1 / 3))  # 小数点后三位
print('{0:_^11} is a 5 length. '.format(name))  # 使用_补齐空位 ^:表示居中
print('{first} is as {second}. '.format(first=name, second='Wendy'))  # 别名替换








