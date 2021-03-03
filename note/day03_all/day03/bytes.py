"""
字节串使用示例

是否所有的字符串都能转换为字节串  是的
是否所有的字节串都能转换为字符串  不是
"""
# 定义一个ascii编码的字节串
byte1 = b"Hello world"
print(type(byte1))
print(byte1)

# 定义一个非ascii编码的字节串
byte2 = "你好".encode()
print(type(byte2))
print(byte2)

# 将字节串转换为字符串，与encode()相反
print(byte2.decode())
print(b'\xcc\xbf\xb5\xe5\xa5\xbd'.decode())